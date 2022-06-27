__all__ = ['check']

import json
import re
import platform
import importlib.resources
from collections import OrderedDict

arch        = platform.machine()
manylinux   = None

def check(obj_versions):
	global manylinux

	if len(obj_versions) == 0:
		return 'any'

	if manylinux is None:
		manylinux_json	= json.load(importlib.resources.open_text('auditwheel.policy', 'manylinux-policy.json'))
		manylinux_json	= sorted(manylinux_json, key=lambda x: x['priority'], reverse=True)
		manylinux		= OrderedDict()
		for m in manylinux_json:
			symbol_versions = m.get('symbol_versions').get(arch, None)
			manylinux[m['name']] = {} if symbol_versions is None else dict((k, set(v)) for k, v in symbol_versions.items())

	def check_item(symbol_versions):
		for k, v in obj_versions.items():
			versions = symbol_versions.get(k, None)
			if versions is None:			continue		# symbol not releveant to manylinux distro
			if not v.issubset(versions):	return False
		return True

	for name, symbol_versions in manylinux.items():
		if check_item(symbol_versions):
			return f'{name}_{arch}'

	raise Exception('Unable to find suiting manylinux distro')