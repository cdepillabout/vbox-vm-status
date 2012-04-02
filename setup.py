#!/usr/bin/env python3

from distutils.core import setup

setup(name='vbox-vm-status',
      version='1.0',
      description='Show status off all vms.',
      author='(cdep) illabout',
      author_email='cdep.illabout@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      scripts=['scripts/vbox-vm-status'],
      data_files=[('etc/bash_completion.d', ['datafiles/bash_completion.d/vbox-vm-status'])],
     )

