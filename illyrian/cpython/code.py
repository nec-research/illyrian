__all__ = ['check']

from illyrian.cpython.cpython37 import CPYTHON37
from illyrian.cpython.cpython38 import CPYTHON38
from illyrian.cpython.cpython39 import CPYTHON39
from illyrian.cpython.cpython310 import CPYTHON310
import re

NONE		= ('py3-none', set())
available	= (NONE, CPYTHON37, CPYTHON38, CPYTHON39, CPYTHON310)

def check(required_symbols):
	supported	= []

	if len(required_symbols) == 0:
		return NONE[0]

	for abi_tag, symbols in available:
		if required_symbols.issubset(symbols):
			supported.append(abi_tag)

	if len(supported) == 0:	raise Exception('No compatible CPython version found')
	if len(supported) > 1:	raise Exception(f'Found multiple compatible CPython version, please specify manually: {supported}')
	return supported[0]
	