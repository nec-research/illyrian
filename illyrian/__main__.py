#!python3
# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__version__ = '0.1'

import json
import zipfile
import sys
import re
import os
import glob
import hashlib
import base64

if len(sys.argv) != 2:
	print('usage: python3 -m illyrian config.json')
	exit(1)

try:
	with open(sys.argv[1], 'r') as f:
		config = json.load(f)
except Exception as e:
	print('IO error: {}'.format(e))
	exit(1)

assert 'name' in config
assert 'version' in config

# https://www.python.org/dev/peps/pep-0427/#id13
distribution	= re.sub('[^\w\d.]+', '_', config['name'], re.UNICODE)
tag				= 'py3-none-any'
wheel_file		= '{}-{}-{}.whl'.format(distribution, config['version'], tag)

#-------------------------------------------------------------------------------
def generate_meta_data():
	def required(key, fmt):
		return '{}: {}\n'.format(fmt, config[key])

	def optional(key, fmt):
		if key in config:
			return required(key, fmt)
		return ''

	meta  = 'Metadata-Version: 2.2\n'
	meta += required('name', 'Name')
	meta += required('version', 'Version')
	meta += required('author', 'Author')
	meta += required('author-email', 'Author-email')
	meta += required('python', 'Requires-Python')
	meta += optional('license', 'License')
	meta += optional('summary', 'Summary')
	meta += optional('platform', 'Platform')
	meta += optional('homepage', 'Home-page')

	if 'requires' in config:
		for requires in config['requires']:
			meta += 'Requires-External: {}\n'.format(requires)
	
	if 'readme' in config:
		meta += 'Description-Content-Type: text/markdown\n\n'
		with open(config['readme'], 'r') as f:
			meta += f.read()
	
	return meta

#-------------------------------------------------------------------------------
def generate_top_list():
	top_list = distribution
	return top_list

#-------------------------------------------------------------------------------
def generate_wheel():
	wheel  = 'Wheel-Version: 1.0\n'
	wheel += 'Generator: illyrian ({})\n'.format(__version__)
	wheel += 'Root-Is-Purelib: true\n'
	wheel += 'Tag: {}\n'.format(tag)
	return wheel

#-------------------------------------------------------------------------------
def hash(content):
	m = hashlib.sha256()
	m.update(content)
	return 'sha256={}'.format(base64.b64encode(m.digest()).decode('UTF-8'))

#-------------------------------------------------------------------------------
def generate_record(file_lists, string_list):
	record = ''
	for files in file_lists:
		for file in files:
			with open(file, 'rb') as f:
				content = f.read()
				record += '{}, {}, {}\n'.format(file, hash(content), len(content))

	for file, string in string_list:
		if string is None:
			h, l = '', ''
		else:
			content = string.encode('UTF-8')
			h, l = hash(content), len(content)
		record += '{}, {}, {}\n'.format(file, h, l)

	return record

#-------------------------------------------------------------------------------
def find_python():
	python_files = []
	if 'packages' in config:
		for package in config['packages']:
			for file in os.listdir(package):
				if os.path.splitext(file)[1] == '.py':
					python_files.append(os.path.join(package, file))
	return python_files

#-------------------------------------------------------------------------------
def find_payload():
	payload_files = []
	if 'payload' in config:
		for payload in config['payload']:
			payload_files += glob.glob(payload)
	return payload_files

#-------------------------------------------------------------------------------
def write_file(handle, f):
	if os.path.islink(f):
		handle.writestr(f, os.readlink(f))
		info = handle.getinfo(f)
		info.external_attr |= (0xA1FF) << 16
	else:
		handle.write(f)

#-------------------------------------------------------------------------------
python_files	= find_python()
payload_files	= find_payload()

with zipfile.ZipFile(wheel_file, mode='w', compression=zipfile.ZIP_DEFLATED) as handle:
	for f in python_files:	write_file(handle, f)
	for f in payload_files:	write_file(handle, f)

	dist_info = '{}-{}.dist-info'.format(distribution, config['version'])

	metadata_file	= os.path.join(dist_info, 'METADATA')
	toplist_file	= os.path.join(dist_info, 'top_list.txt')
	wheel_file		= os.path.join(dist_info, 'WHEEL')
	record_file		= os.path.join(dist_info, 'RECORD')

	metadata	= generate_meta_data()
	toplist		= generate_top_list()
	wheel		= generate_wheel()
	record		= generate_record(
		[python_files, payload_files],
		[
			(metadata_file,	metadata),
			(toplist_file,	toplist),
			(wheel_file,	wheel),
			(record_file,	None)
		]
	)

	handle.writestr(metadata_file, 	metadata)
	handle.writestr(toplist_file,	toplist)
	handle.writestr(wheel_file,		wheel)
	handle.writestr(record_file,	record)