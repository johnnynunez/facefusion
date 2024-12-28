#!/usr/bin/env python3

import os

os.environ['OMP_NUM_THREADS'] = '1'
os.environ['TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL'] = '1'

from facefusion import core

if __name__ == '__main__':
	core.cli()
