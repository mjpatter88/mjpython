from virtual_machine import VirtualMachine

from unittest.mock import MagicMock

class TestVirtualMachineImports:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.frame = MagicMock()
        self.frame.blocks = []

    def test_instr_IMPORT_NAME__decreases_stack_size_by_one(self):
        self.frame.stack = [0, ()]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_NAME("os")
        assert len(self.frame.stack) == 1

    def test_instr_IMPORT_NAME__adds_imported_module_to_top_of_stack(self):
        self.frame.stack = [0, ()]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_NAME("os")
        import os
        assert self.frame.stack[0] == os

    def test_instr_IMPORT_FROM__adds_imported_attribute_to_top_of_stack(self):
        import random
        self.frame.stack = [random]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_FROM("shuffle")
        from random import shuffle
        assert self.frame.stack == [random, shuffle]

    def test_instr_IMPORT_FROM__adds_imported_module_to_top_of_stack(self):
        import datetime as dt
        self.frame.stack = [dt]
        self.vm.push_frame(self.frame)
        self.vm.instr_IMPORT_FROM("datetime")
        from datetime import datetime
        assert self.frame.stack == [dt, datetime]
