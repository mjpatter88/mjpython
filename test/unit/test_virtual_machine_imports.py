from virtual_machine import VirtualMachine

from unittest.mock import MagicMock

class TestVirtualMachineImports:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.frame = MagicMock()
        self.frame.blocks = []

    def test_instr_IMPORT_NAME__decreases_stack_size_by_one(self):
        self.frame.stack = [1, 2]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_NAME("os")
        assert len(self.frame.stack) == 1

    def test_instr_IMPORT_NAME__adds_imported_module_to_top_of_stack(self):
        self.frame.stack = [1, 2]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_NAME("os")
        import os
        assert self.frame.stack[0] == os
