# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['wheel']

import json
import zipfile
import re
import os
import glob
import illyrian
import subprocess
from illyrian import cpython, manylinux, util
from illyrian.util import L_EMPH, L_RESET

class File:
	def __init__(self, src, dst=None, chmod=None, content=None):
		self.src = src
		self.dst = src if dst is None else dst
		self.chmod = chmod
		self.content = content

	def __str__(self):
		out = f'{self.src}'
		if self.src != self.dst:	out += f' > {self.dst}'
		if self.chmod is not None:	out += f' ({oct(self.chmod)})'
		return out

	def __ref__(self):
		return str(self)

	def __lt__(self, o):
		assert isinstance(o, File)
		if self.src < o.src:	return True
		if self.src > o.src:	return False
		if self.dst < o.dst:	return True
		if self.dst > o.dst:	return False
		if self.chmod is None:
			if o.chmod is None:	return False
			else:				return True
		else:
			if o.chmod is None:	return False
			else:				return self.chmod < o.chmod

	def write(self, handle):
		if self.content is None:
			if os.path.islink(self.src):
				raise Exception(f'{self.src} is a symlink. Symlinks are not supported by PIP!')
			handle.write(self.src, arcname=self.dst)
		else:
			handle.writestr(self.dst, self.content)
		
		info = handle.getinfo(self.dst)
		info.external_attr |= 0x80000000 # required to mark this as a real file?

		if self.chmod:
			info.external_attr |= self.chmod << 16

	def read(self):
		if self.content is None:
			if os.path.exists(self.src):
				return open(self.src, 'rb').read()
			return None
		return self.content.encode('UTF-8')

def wheel(config_file):
	global config

	# Load Config File ---------------------------------------------------------
	supported = {'author', 'author-email', 'classifier', 'download-url', 'homepage',
		'keywords', 'license', 'license-file', 'maintainer', 'maintainer-email',
		'obsoletes-dist', 'platform', 'project-url', 'provides-dist',
		'requires-dist', 'requires-external', 'supported-platform', 'requires-python',
		'summary', 'readme', 'name', 'version', 'abi-tag', 'platform-tag',
		'__include__', 'packages', 'scripts', 'payload', 'python-tag', 'provides-extra',
		'links'}

	def read_json(file):
		j = None
		try:
			j = json.load(open(file, 'r'))
		except Exception as e:
			raise Exception(f'Cannot open {config_file}: {e}')
	
		if not isinstance(j, dict):
			raise Exception(f'Root element needs to be a dict, but is: {type(j)}')
		
		for k in j.keys():
			if k not in supported:
				raise Exception(f'Unsupported key \'{k}\'. Only {sorted(supported)} are supported.')
		
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
			raise Exception(f'Missing field "{name}" in {config_file}')
		
		value = config.pop(name).strip()
		if len(value) == 0:
			raise Exception(f'Empty field "{name}" in {config_file}')
		
		return value

	def check_version(version):
		# remove leading zeros
		version = re.sub(r'^[0]+([0-9]+)', '\1', version)
		version = re.sub(r'\.[0]+([0-9]+)', '\.\1', version)
		if re.match(r'^([0-9]+!)?[0-9]+(\.[0-9]+)*((a|b|rc)[0-9]+)?(\.post[0-9]+)?(\.dev[0-9]+)?$', version) is None:
			raise Exception(f'{version} is no valid python version in format: [N!]N(.N)*[{"a|b|rc"}N][.postN][.devN] (see PEP440)')
		return version

	name			= check('name')
	version			= check_version(check('version'))
	abi_tag			= config.pop('abi-tag', 'auto')
	platform_tag	= config.pop('platform-tag', 'auto')

	# https://www.python.org/dev/peps/pep-0427/#id13
	distribution	= re.sub("[^\w\d.]+", "_", name, re.UNICODE)

	#---------------------------------------------------------------------------
	def generate_meta_data(dist_info):
		def process(value, key, fmt, can_be_list=False, regex=None):
			def format(value):
				if not isinstance(value, str):
					raise Exception(f'Expected str for {fmt} but found {type(value)}')

				value = value.strip()

				if len(value) == 0:
					raise Exception(f'Empty str found for {fmt}')

				if regex:
					if regex.search(value) is None:
						raise Exception(f'Illegal value "{value}" in for {fmt}')
				
				return f'{fmt}: {value}\n'

			if isinstance(value, (list, tuple)):
				if not can_be_list:
					raise Exception(f'{key} can\'t be a list')
				out = ''
				for v in value:
					out += format(v)
				return out

			return format(value)

		def required(key, fmt, can_be_list=False, regex=None):
			return process(config[key], key, fmt, can_be_list, regex)			

		def optional(key, fmt, can_be_list=False, regex=None):
			if key in config:
				return required(key, fmt, can_be_list, regex)
			return ''

		def git(key, git):
			value = config.get(key, None)
			if value == '__GIT__':
				p = subprocess.run(['git', 'config', git], stdout=subprocess.PIPE)
				if p.returncode != 0:
					raise Exception(f'Unable to fetch {git} from git')
				config[key] = p.stdout.decode('utf-8')

		git('author',		'user.name')
		git('author-email',	'user.email')

		meta  = 'Metadata-Version: 2.1\n'
		meta += f'Name: {name}\n'
		meta += f'Version: {version}\n'
		meta += required('requires-python',		'Requires-Python', regex=re.compile(r'^[>=<\s]+[\.0-9]+[>=<\s,\.0-9]*$'))
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
		meta += optional('provides-extra',		'Provides-Extra',		True, regex=re.compile('^([a-z0-9]|[a-z0-9]([a-z0-9\-](?!--))*[a-z0-9])$'))
		meta += optional('requires-dist', 		'Requires-Dist',		True)
		meta += optional('requires-external',	'Requires-External',	True)
		meta += optional('supported-platform',	'Supported-Platform',	True)

		print(f'{L_EMPH}## METADATA{L_RESET}')
		print(meta)

		if 'readme' in config:
			meta += 'Description-Content-Type: text/markdown\n\n'
			meta += open(config['readme'], 'r').read()
		else:
			meta += 'Description-Content-Type: text/markdown\n\n'

		return File(os.path.join(dist_info, 'METADATA'), content=meta)

	#---------------------------------------------------------------------------
	def generate_top_list(dist_info):
		top_list = distribution
		return File(os.path.join(dist_info, 'top_list.txt'), content=top_list)

	#---------------------------------------------------------------------------
	def generate_wheel(dist_info):
		wheel_  = 'Wheel-Version: 1.0\n'
		wheel_ += f'Generator: illyrian ({illyrian.__version__})\n'
		wheel_ += 'Root-Is-Purelib: true\n'
		wheel_ += f'Tag: {abi_tag}-{platform_tag}\n'
		print(f'{L_EMPH}## WHEEL{L_RESET}')
		print(wheel_)
		print()
		return File(os.path.join(dist_info, 'WHEEL'), content=wheel_)

	#---------------------------------------------------------------------------
	def generate_record(files):
		self = File(os.path.join(dist_info, 'RECORD'))
		record = ''

		def add(file, content):
			nonlocal record
			if content is None:	h, l = '', ''
			else:				h, l = util.hash(content), len(content)
			record += f'{file.dst}, {h}, {l}\n'

		for file in files:
			add(file, file.read())
		add(self, None)

		self.content = record
		return self

	#---------------------------------------------------------------------------
	def get_condition(name):
		split = name.strip().split('?')
		if len(split) == 1:	return name, lambda x: x > 0, lambda x: f'{x} > 0'
		if len(split) > 2:	raise Exception(f'Illegal search literal: {name}')

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
								dir_list.append(File(os.path.join(package, file)))
					except Exception as e:
						if not condition(0):
							raise Exception(f'Unable to find package "{package}"')

					cnt = len(dir_list)
					if not condition(cnt):
						raise Exception(f'{msg(cnt)} failed for {package}')

					python_files += dir_list

				python_files.sort()
				print(f'{L_EMPH}## Python Files{L_RESET}')
				print(*python_files, sep='\n')
				print()
		return python_files

	#---------------------------------------------------------------------------
	def find_headers(dist_info):
		header_files = []
		if 'license-file' in config:
			license_file = config['license-file']
			header_files.append(File(license_file, os.path.join(dist_info, 'LICENSE')))

		if len(header_files):
			print(f'{L_EMPH}## Header Files{L_RESET}')
			print(*header_files, sep='\n')
			print()
		return header_files

	#---------------------------------------------------------------------------
	def find_scripts(data_path):
		script_files = []
		if 'scripts' in config:
			for script in config['scripts']:
				script_files.append(File(script, os.path.join(data_path, 'scripts', os.path.basename(script)), 0o777))

			script_files.sort()
		
		if len(script_files):
			print(f'{L_EMPH}## Script Files{L_RESET}')
			print(*script_files, sep='\n')
			print()
		return script_files

	#---------------------------------------------------------------------------
	def run_objdump(files):
		VERSION				= re.compile(r'[a-z0-9\s]+([A-Z]+)_([0-9\.]+)')
		PYTHON_SYMBOL		= re.compile(r'.*\s([_]?Py[A-Za-z0-9_]+)')
		
		p   				= subprocess.run(['objdump', '-x'] + [f.src for f in files], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
		# we can't check the return_code, as it is non-zero if we add any non lib files, which is very likely.
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
				
				for f in files:
					x = File(f)
					if x in payload_files:
						raise Exception(f'File {f} cannot be added twice by multiple payload rules!')
					payload_files.append(x)

			payload_files.sort()

			if platform_tag == 'auto' or abi_tag == 'auto':
				symbols, versions = run_objdump(payload_files)
				if platform_tag == 'auto':	platform_tag	= manylinux.check(versions)
				if abi_tag      == 'auto':	abi_tag			= cpython  .check(symbols)

			print(f'{L_EMPH}## Payload Files{L_RESET}')
			print(*payload_files, sep='\n')
			print()

		if platform_tag	== 'auto':	platform_tag	= 'any'
		if abi_tag		== 'auto':	abi_tag			= 'py3-none'

		return payload_files, abi_tag, platform_tag

	#---------------------------------------------------------------------------
	def find_links(data_path):
		link_files = []
		if 'links' in config:
			links = config['links']
			for src in links:
				script = f"""#!python3
# Generated by Illrian {illyrian.__version__}
import site
import os
import subprocess
import sys
sitepackages = site.getsitepackages()
if site.ENABLE_USER_SITE:
	sitepackages += [site.getusersitepackages()]
for path in sitepackages:
	file = os.path.join(path, '{src}')
	if os.path.exists(file):
		exit(subprocess.run([file] + sys.argv[1:]).returncode)
raise Exception('Unable to find {src}')
"""
				link_files.append(File(src, os.path.join(data_path, 'scripts', os.path.basename(src)), 0o777, script))

			link_files.sort()

			print(f'{L_EMPH}## Link Files{L_RESET}')
			print(*link_files, sep='\n')
			print()

		return link_files

	#---------------------------------------------------------------------------
	data_path		= f'{distribution}-{version}.data'
	dist_info		= f'{distribution}-{version}.dist-info'
	python_files	= find_python()
	script_files	= find_scripts(data_path)
	header_files	= find_headers(dist_info)
	link_files		= find_links(data_path)
	payload_files, abi_tag, platform_tag = find_payload(abi_tag, platform_tag)

	whl_file = f'{distribution}-{version}-{abi_tag}-{platform_tag}.whl'

	if os.path.exists(whl_file):
		os.remove(whl_file)

	with zipfile.ZipFile(whl_file, mode='w', compression=zipfile.ZIP_DEFLATED) as handle:
		for f in python_files:	f.write(handle)
		for f in payload_files:	f.write(handle)
		for f in script_files:	f.write(handle)
		for f in header_files:	f.write(handle)
		for f in link_files:	f.write(handle)

		metadata	= generate_meta_data(dist_info)
		wheel_		= generate_wheel	(dist_info)
		toplist		= generate_top_list	(dist_info)
		record		= generate_record(
			python_files + 
			payload_files + 
			script_files + 
			header_files + 
			link_files +
			[metadata, toplist, wheel_]
		)

		metadata.write(handle)
		wheel_.write(handle)
		toplist.write(handle)
		record.write(handle)

	print(f'Generated: {whl_file}')
	print()
