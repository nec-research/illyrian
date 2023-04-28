# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['run']

import sys
import os
import illyrian
import glob
from illyrian.util import L_EMPH, L_RESET
import pydot
import shutil

def run():
	print(f'{L_EMPH}#### Illyrian v{illyrian.__version__} ####{L_RESET}')
	print()

	cnt = len(sys.argv)
	if cnt == 1:
		print('usage:')
		print('    - build:  illyrian config.json')
		print('    - info:   illyrian wheel.whl')
		print('    - cmake:  illyrian /path/to/cmake ...')
		print('    - verify: illyrian /path/to/install/folder')
		return

	cmake = shutil.which(sys.argv[1])
	if cmake is not None and cmake.endswith(('cmake', 'cmake3')) and os.path.isfile(cmake) and os.access(cmake, os.X_OK):
		illyrian.env(sys.argv[1:])
		return

	graph, nodes = None, None

	for x in sys.argv[1:]:
		if x == "--version":
			exit(0)

		for y in glob.glob(x):
			if os.path.isdir(y):
				illyrian.verify(y)
			elif os.path.isfile(y):
				if y.endswith('.whl'):
					if graph is None:
						graph, nodes = pydot.Dot('Illyrian dependency graph', graph_type='graph'), dict()
					illyrian.info(x, graph, nodes)
				elif y.endswith('.json'):
					illyrian.wheel(x)
				else:
					raise Exception(f'Unsupported file type: {y}')

	if graph is not None:
		try:
			graph.write_svg('illyrian_dependencies.svg')
		except OSError:
			pass # it seems no dot is available