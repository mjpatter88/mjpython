#!/usr/bin/env python3

import sys
from virtual_machine import VirtualMachine

file_name = sys.argv[1]

with open(file_name) as script:
    code = compile(script.read(), file_name, 'exec')

vm = VirtualMachine()
vm.run_code(code)
