# Copyright 2022 NEC Laboratories Europe
# Author: Nicolas Weber <nicolas.weber@neclab.eu>

__all__ = ['env']
import subprocess
import os

def env(args):
	cmd = [args[0], '-DCMAKE_MODULE_PATH={}'.format(os.path.join(os.path.dirname(__file__), 'cmake'))] + list(args[1:])
	subprocess.run(cmd)
