# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['wheel']

import json
import zipfile
import re
import os
import glob
import hashlib
import base64
import illyrian
import subprocess
from illyrian import cpython, manylinux

def wheel(config_file):
	global config

	# Load Config File ---------------------------------------------------------
	supported = {'author', 'author-email', 'classifier', 'download-url', 'homepage', 'keywords', 'license', 'maintainer', 'maintainer-email',
		'obsoletes-dist', 'platform', 'project-url', 'provides-dist', 'requires-dist', 'requires-external', 'supported-platform',
		'requires-python', 'summary', 'readme', 'name', 'version', 'abi-tag', 'platform-tag', '__include__', 'packages', 'scripts',
		'payload', 'python-tag'}

	def read_json(file):
		j = None
		try:
			j = json.load(open(file, 'r'))
		except Exception as e:
			raise Exception('Cannot open {}: {}'.format(config_file, e))
	
		if not isinstance(j, dict):
			raise Exception('Root element needs to be a dict, but is: {}'.format(type(j)))
		
		for k in j.keys():
			if k not in supported:
				raise Exception('Unsupported key \'{}\'. Only {} are supported.'.format(k, sorted(supported)))
		
		return j

	config = read_json(config_file)

	# Handle Includes ----------------------------------------------------------
	def merge(A, B):
		for k, v in B.items():
			if k in A:
				val = A[k]
				if not isinstance(val, list):
					val = [val]

				if isinstance(v, list):	val = val + v
				else:					val.append(v)

				A[k] = val
			else:
				A[k] = v
		return A

	while True:
		includes = config.pop('__include__', None)

		if includes is None:
			break

		if isinstance(includes, (list, tuple)):
			for i in includes:
				config = merge(config, read_json(i))
		elif isinstance(includes, str):
			config = merge(config, read_json(includes))

	#---------------------------------------------------------------------------
	def check(name):
		global config

		if name not in config:
			raise Exception('Missing field "{}" in {}'.format(name, config_file))
		
		value = config.pop(name).strip()
		if len(value) == 0:
			raise Exception('Empty field "{}" in {}'.format(name, config_file))
		
		return value

	name			= check('name')
	version			= check('version')
	abi_tag			= config.pop('abi-tag', 'auto')
	platform_tag	= config.pop('platform-tag', 'auto')

	# https://www.python.org/dev/peps/pep-0427/#id13
	distribution	= re.sub("[^\w\d.]+", "_", name, re.UNICODE)

	#---------------------------------------------------------------------------
	def generate_meta_data():
		def required(key, fmt, can_be_list=False, regex=None):
			def format(v):
				if not isinstance(v, str):
					raise Exception('Expected str for {} but found {}'.format(fmt, type(v)))

				v = v.strip()

				if len(v) == 0:
					raise Exception('Empty str found for {}'.format(fmt))

				if regex:
					if re.search(regex, value) is None:
						raise Exception('Illegal value "{}" in for {}'.format(value, fmt))
				
				return '{}: {}\n'.format(fmt, v)

			value = config[key]

			if isinstance(value, (list, tuple)):
				if not can_be_list:
					raise Exception('{} can\'t be a list'.format(key))
				out = ''
				for v in value:
					out += format(v)
				return out

			return format(value)

		def optional(key, fmt, can_be_list=False):
			if key in config:
				return required(key, fmt, can_be_list)
			return ''

		meta  = 'Metadata-Version: 2.1\n'
		meta += 'Name: {}\n'.format(name)
		meta += 'Version: {}\n'.format(version)
		meta += required('requires-python',		'Requires-Python', regex='^[>=<\s]+[\.0-9]+[>=<\s,\.0-9]*$')
		meta += required('summary',				'Summary')
		meta += optional('author',				'Author')
		meta += optional('author-email',		'Author-email')
		meta += optional('classifier',			'Classifier',			True)
		meta += optional('download-url',		'Download-URL')
		meta += optional('homepage',			'Home-page')
		meta += optional('keywords',			'Keywords')
		meta += optional('license',				'License')
		meta += optional('maintainer',			'Maintainer')
		meta += optional('maintainer-email',	'Maintainer-Email')
		meta += optional('obsoletes-dist',		'Obsoletes-Dist',		True)
		meta += optional('platform',			'Platform',				True)
		meta += optional('project-url',			'Project-URL',			True)
		meta += optional('provides-dist',		'Provides-Dist',		True)
		meta += optional('requires-dist', 		'Requires-Dist',		True)
		meta += optional('requires-external',	'Requires-External',	True)
		meta += optional('supported-platform',	'Supported-Platform',	True)
		
		print('## METADATA')
		print(meta)

		if 'readme' in config:
			meta += 'Description-Content-Type: text/markdown\n\n'
			meta += open(config['readme'], 'r').read()
		else:
			meta += 'Description-Content-Type: text/markdown\n\n'

		return meta

	#---------------------------------------------------------------------------
	def generate_top_list():
		top_list = distribution
		return top_list

	#---------------------------------------------------------------------------
	def generate_wheel():
		wheel_  = 'Wheel-Version: 1.0\n'
		wheel_ += 'Generator: illyrian ({})\n'.format(illyrian.__version__)
		wheel_ += 'Root-Is-Purelib: true\n'
		wheel_ += 'Tag: {}-{}\n'.format(abi_tag, platform_tag)
		print("## WHEEL")
		print(wheel_)
		print()
		return wheel_

	#---------------------------------------------------------------------------
	def hash(content):
		m = hashlib.sha256()
		m.update(content)
		return 'sha256={}'.format(base64.b64encode(m.digest()).decode('UTF-8'))

	#---------------------------------------------------------------------------
	def generate_record(file_lists, string_list):
		record = ''
		for files in file_lists:
			for file in files:
				if isinstance(file, tuple):	src, dst = file[:2]
				else:						src, dst = file, file
				content = open(src, 'rb').read()
				record += '{}, {}, {}\n'.format(dst, hash(content), len(content))

		for file, string in string_list:
			if string is None:
				h, l = '', ''
			else:
				content = string.encode('UTF-8')
				h, l = hash(content), len(content)
			record += '{}, {}, {}\n'.format(file, h, l)

		return record

	#---------------------------------------------------------------------------
	def get_condition(name):
		split = name.strip().split('?')
		if len(split) == 1:
			return name, lambda x: x > 0, lambda x: f'{x} > 0'
		if len(split) > 2:
			raise Exception(f'Illegal search literal: {name}')

		name, conditions = split
		if conditions == '':
			conditions = '>=1' if '*' in name else '==1'

		def parse(condition):
			cond = re.match(r'\s*([!=><][=]?)\s*([0-9]+)', condition)
			if cond is None:
				raise Exception(f'Illegal condition: {condition}')
			operator, value = cond[1], int(cond[2])
			if operator == '!=':	return name, lambda x: x != value, lambda x: f'{x} != {value}'
			if operator == '<':		return name, lambda x: x <  value, lambda x: f'{x} < {value}'
			if operator == '<=':	return name, lambda x: x <= value, lambda x: f'{x} <= {value}'
			if operator == '==':	return name, lambda x: x == value, lambda x: f'{x} == {value}'
			if operator == '>':		return name, lambda x: x >  value, lambda x: f'{x} > {value}'
			if operator == '>=':	return name, lambda x: x >= value, lambda x: f'{x} >= {value}'
			raise Exception(f'Illegal condition operator: {condition}')

		output = None
		for condition in conditions.split('&&'):
			cond = parse(condition)
			if output is None:	output = cond
			else:				output = lambda x: output(x) and cond(x)
		return output

	#---------------------------------------------------------------------------
	def find_python():
		python_files = []
		if 'packages' in config:
			packages = config['packages']
			assert isinstance(packages, (list, tuple))
			if len(packages):
				for package in packages:
					package, condition, msg = get_condition(package.replace('.', '/'))
					dir_list = []

					try:
						for file in os.listdir(package):
							if os.path.isfile(os.path.join(package, file)) and os.path.splitext(file)[1] == '.py':
								dir_list.append(os.path.join(package, file))
					except Exception as e:
						if not condition(0):
							raise Exception(f'Unable to find package "{package}"')

					cnt = len(dir_list)
					if not condition(cnt):
						raise Exception(f'{msg(cnt)} failed for {package}')

					python_files += dir_list

				python_files.sort()
				print('## Python Files')
				print(*python_files, sep='\n')
				print()
		return python_files

	#---------------------------------------------------------------------------
	def find_scripts(data_path):
		script_files = []
		if 'scripts' in config:
			for script in config['scripts']:
				script_files.append((script, os.path.join(data_path, 'scripts', os.path.basename(script)), 0o777))

			script_files.sort()
			print('## Script Files')
			print(*tuple(f[0] for f in script_files), sep='\n')
			print()
		return script_files

	#---------------------------------------------------------------------------
	def check_platform_tag(platform_tag, platform_tag_):
		if platform_tag == 'auto':			return platform_tag_
		if platform_tag != platform_tag_:	raise Exception(f'Platform tag {platform_tag} is incompatible to {platform_tag_}')
		return platform_tag

	#---------------------------------------------------------------------------
	def run_objdump(files):
		VERSION				= re.compile(r'[a-z0-9\s]+([A-Z]+)_([0-9\.]+)')
		PYTHON_SYMBOL		= re.compile(r'.*\s([_]?Py[A-Za-z0-9_]+)')
		
		p   				= subprocess.run(['objdump', '-x'] + files, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
		# we can't check the return_code, as it is non-zero if we add any non lib files, which is very likely.
		objdump				= p.stdout.decode('utf-8').split('\n')
		symbols, versions	= set(), dict()

		for line in p.stdout.decode('utf-8').split('\n'):
			m = PYTHON_SYMBOL.match(line)
			if m: symbols.add(m[1]);							continue
			m = VERSION.match(line)
			if m: versions.setdefault(m[1], set()).add(m[2]);	continue

		return symbols, versions

	#---------------------------------------------------------------------------
	def find_payload(abi_tag, platform_tag):
		payload_files	= []
		if 'payload' in config:
			for payload in config['payload']:
				payload, condition, msg = get_condition(payload)
				files	= glob.glob(payload, recursive=True)
				files	= list(filter(lambda f: os.path.isfile(f), files))
				cnt		= len(files)
				if not condition(cnt):
					raise Exception(f'{msg(cnt)} failed for {payload}')
				
				payload_files += files

			payload_files.sort()

			if platform_tag == 'auto' or abi_tag == 'auto':
				symbols, versions = run_objdump(payload_files)
				if platform_tag == 'auto':	platform_tag	= manylinux.check(versions)
				if abi_tag      == 'auto':	abi_tag			= cpython  .check(symbols)

			print('## Payload Files')
			print(*payload_files, sep='\n')
			print()

		if platform_tag	== 'auto':	platform_tag	= 'any'
		if abi_tag		== 'auto':	abi_tag			= 'py3-none'

		return payload_files, abi_tag, platform_tag

	#---------------------------------------------------------------------------
	def write_file(handle, f):
		if isinstance(f, tuple):
			if len(f) == 2:			src, dst, attr = f, None
			else:					src, dst, attr = f
		else:						src, dst, attr = f, f, None

		if os.path.islink(src):
			raise Exception('{} is a symlink. Symlinks are not supported by PIP!'.format(f))
			#handle.writestr(f, os.readlink(f))
			#info = handle.getinfo(f)
			#info.external_attr |= (0xA1FF) << 16
		else:
			handle.write(src, arcname=dst)
			if attr:
				info = handle.getinfo(dst)
				info.external_attr |= attr << 16

	#---------------------------------------------------------------------------
	data_path		= '{}-{}.data'.format(distribution, version)
	dist_info		= '{}-{}.dist-info'.format(distribution, version)
	python_files	= find_python()
	script_files	= find_scripts(data_path)
	payload_files, abi_tag, platform_tag = find_payload(abi_tag, platform_tag)

	whl_file = f'{distribution}-{version}-{abi_tag}-{platform_tag}.whl'

	if os.path.exists(whl_file):
		os.remove(whl_file)

	with zipfile.ZipFile(whl_file, mode='w', compression=zipfile.ZIP_DEFLATED) as handle:
		for f in python_files:	write_file(handle, f)
		for f in payload_files:	write_file(handle, f)
		for f in script_files:	write_file(handle, f)

		metadata_file	= os.path.join(dist_info, 'METADATA')
		toplist_file	= os.path.join(dist_info, 'top_list.txt')
		wheel_file		= os.path.join(dist_info, 'WHEEL')
		record_file		= os.path.join(dist_info, 'RECORD')

		metadata	= generate_meta_data()
		wheel_		= generate_wheel()
		toplist		= generate_top_list()
		record		= generate_record(
			[python_files, payload_files, script_files],
			[
				(metadata_file,	metadata),
				(toplist_file,	toplist),
				(wheel_file,	wheel_),
				(record_file,	None)
			]
		)

		handle.writestr(metadata_file, 	metadata)
		handle.writestr(toplist_file,	toplist)
		handle.writestr(wheel_file,		wheel_)
		handle.writestr(record_file,	record)

	print('Generated: {}'.format(whl_file))
