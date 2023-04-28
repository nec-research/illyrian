# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['verify']

import zipfile
import os
from illyrian import util
from illyrian.util import  L_EMPH, L_RED, L_GREEN, L_RESET

def read_raw(file, filename):
	with file.open(filename) as p:
		return p.read()

def read(file, filename):
	return read_raw(file, filename).decode('utf-8')

def verify(dir):
	whls, srcs = [], []

	# list files ---------------------------------------------------------------
	for x in os.listdir(dir):
		if os.path.islink(x):
			pass
		elif os.path.isfile(x):
			if x.endswith('.whl'):
				whls.append(x)
		elif os.path.isdir(x):
			srcs.append(x)

	if len(whls) == 0 or len(srcs) == 0:
		raise Exception(f'Unable to find WHLs and SRCs in {dir}')

	print(f'{L_EMPH}## SRCs{L_RESET}')
	for k in srcs:
		print(k)
	print()

	print(f'{L_EMPH}## WHLs{L_RESET}')
	for k in whls:
		print(k)
	print()

	# traverse srcs ------------------------------------------------------------
	src_files = dict()
	def traverse_src(x):
		if os.path.isfile(x):
			with open(x, 'rb') as file:
				content = file.read()
				src_files[x] = (len(content), util.hash(content))
		elif os.path.isdir(x):
			for y in os.listdir(x):
				traverse_src(os.path.join(x, y))
		else:
			raise Exception(f'{x} is neither a file nor a directory and cannot be part of a Python wheel')

	for x in srcs:
		traverse_src(x)

	# traverse whls ------------------------------------------------------------
	whl_files		= dict()
	whl_duplicates	= dict()
	def traverse_whl(x):
		z = zipfile.ZipFile(x)
		for y in z.infolist():
			fn = y.filename
			if not y.is_dir():
				if '.dist-info/' not in fn:
					with z.open(y) as file:
						content = file.read()
						if fn in whl_files:
							ll = whl_duplicates.setdefault(fn, [])
							ll.append(x)
						else:
							whl_files[fn] = (len(content), util.hash(content))

	for x in whls:
		traverse_whl(x)

	# compare src > whl --------------------------------------------------------
	not_found_in_whl	= []
	mismatches			= {}

	for k, v in src_files.items():
		w = whl_files.get(k, None)
		if w is None:
			not_found_in_whl.append(k)
		else:
			del whl_files[k]
			if v != w:
				mismatches[k] = (v, w)

	# compare whl > src --------------------------------------------------------
	not_found_in_src = list(whl_files.keys())

	if len(whl_duplicates):
		print(f'{L_EMPH}## File duplicates in WHLs{L_RESET}')
		for k, v in whl_duplicates.items():
			print(f'{k}: {v}')
		print()

	if len(not_found_in_whl):
		print(f'{L_EMPH}## Files not found in WHLs{L_RESET}')
		for k in not_found_in_whl:
			print(k)
		print()

	if len(not_found_in_src):
		print(f'{L_EMPH}## Files not found in SRCs{L_RESET}')
		for k in not_found_in_src:
			print(k)
		print()

	if len(mismatches):
		print(f'{L_EMPH}## Files not matching between SRCs and WHLs{L_RESET}')
		for k, v in mismatches.items():
			print(f'{k}:', end='')
			(asize, ahash), (bsize, bhash) = v
			if asize != bsize:	print(f' {L_RED}size: {asize} != {bsize}{L_RESET}', end='')
			if ahash != bhash:	print(f' {L_RED}hash: {ahash} != {bhash}{L_RESET}', end='')
			print()
		print()

	if len(whl_duplicates) == 0 and len(not_found_in_whl) == 0 and len(not_found_in_src) == 0 and len(mismatches) == 0:
		print(f'{L_GREEN}SRCs and WHLs are matching!{L_RESET}')