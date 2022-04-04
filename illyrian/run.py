# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['run']

import sys
import illyrian

def run():
	print("#### Illyrian v{} ####".format(illyrian.__version__))
	print()

	cnt = len(sys.argv)

	if cnt == 1:			raise Exception('usage: illyrian config.json or illyrian /path/to/cmake ...')
	if cnt == 2:
		if sys.argv[1] == "--version":	exit(0)
		else:							illyrian.wheel	(sys.argv[1])
	else:								illyrian.env	(sys.argv[1:])