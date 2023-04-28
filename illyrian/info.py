# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['info']

import zipfile
import re
import pydot
from illyrian import util
from illyrian.util import  L_EMPH, L_RED, L_GREEN, L_RESET

def read_raw(file, filename):
	with file.open(filename) as p:
		return p.read()

def read(file, filename):
	return read_raw(file, filename).decode('utf-8')

def info(whl_file, graph, nodes):
	file = zipfile.ZipFile(whl_file)

	all_files, dist_info = set(), dict()
	for x in file.infolist():
		if not x.is_dir():
			all_files.add(x.filename)
			xn = x.filename
			if '.dist-info/' in xn:
				dist_info[xn] = read(file, xn).strip()

	for k, v in dist_info.items():
		print(f'{L_EMPH}## {k}{L_RESET}')

		if 'RECORD' in k.upper():
			def color(success, label):
				return f'{L_GREEN if success else L_RED}{label}{L_RESET}'

			def check_size(size, content):
				return int(size) == len(content)

			def check_hash(sha, content):
				algo, _ = (x.strip() for x in sha.split('=', 1))
				enc = util.hash(content, algo)
				return enc == sha

			def check_file(filename):
				try:
					content = read_raw(file, file.getinfo(filename))
					return content, '__pycache__' not in filename
				except KeyError:
					return None, False

			files = v.split('\n')
			for x in files:
				filename, sha, size = (y.strip() for y in x.split(','))
				is_record = filename.endswith('.dist-info/RECORD')
				all_files.remove(filename)
				content, exists	= check_file(filename)
				filename		= color(exists, filename)
				if is_record:
					sha			= '' if sha  == '' else color(False, 'error')
					size		= '' if size == '' else color(False, 'error')
				else:
					sha			= color(check_hash(sha, content), sha)
					size		= color(check_size(size, content), size)
				print(f'{filename}, {sha}, {size}')

			for x in all_files:
				print(f'{L_RED}{x}{L_RESET}')
		else:
			print(v)
		print()
	
	# Render dependencies ------------------------------------------------------
	metadata = None
	for k, v in dist_info.items():
		if k.endswith('METADATA'):
			metadata = v
			break

	if metadata:
		name, dependencies = None, list()
		for line in metadata.strip().split('\n'):
			if line.startswith('Name:'):
				assert name is None
				name = line.split(' ', 1)[1]
			elif line.startswith('Requires-Dist:'):
				dependencies.append(line.split(' ', 1)[1])

		assert name is not None
		
		split = re.compile(r'([A-Za-z0-9\-]+)(.*)?')
		def add_node(name, is_global=True):
			if name not in nodes:
				node		= pydot.Node(name)
				nodes[name]	= node
				graph.add_node(node)
			else:
				node = nodes[name]

			if not is_global:
				attrs = node.obj_dict['attributes']
				attrs['shape'] = 'box'
				attrs['color'] = 'green'

			return node

		src = add_node(name, False)

		for d in dependencies:
			match	= split.match(d)
			name	= match[1]
			version	= match[2]
			if version is not None:
				version = version.strip()
			
			dst	= add_node(name)
			graph.add_edge(pydot.Edge(src, dst, label=version, dir='forward'))
