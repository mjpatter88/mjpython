import sys
from virtual_machine import VirtualMachine

file_name = sys.argv[1]
# print(file_name + " ", end="")

with open(file_name) as script:
    code = compile(script.read(), file_name, 'exec')

# print("compiled")
# import dis
# print(dis.dis(code))
vm = VirtualMachine()
vm.run_code(code)
