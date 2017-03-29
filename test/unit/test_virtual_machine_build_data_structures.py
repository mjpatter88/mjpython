from virtual_machine import VirtualMachine, BIN_OPS, VirtualMachineError
from frame import Frame
from block import Block

from unittest.mock import MagicMock, patch
import pytest

class TestVirtualMachineBuildDataStructures:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.frame = MagicMock()
        self.frame.blocks = []

    def test_instr_BUILD_CONST_KEY_MAP__consumes_count_elements_from_stack(self):
        count = 3
        self.frame.stack = [1, 2, 3, ('a', 'b', 'c')]
        self.vm.push_frame(self.frame)
        self.vm.instr_BUILD_CONST_KEY_MAP(count)
        assert len(self.frame.stack) == 1

    def test_instr_BUILD_CONST_KEY_MAP__builds_map_on_TOS(self):
        count = 3
        self.frame.stack = [1, 2, 3, ('a', 'b', 'c')]
        key_map = {'a': 1, 'b': 2, 'c': 3}
        self.vm.push_frame(self.frame)
        self.vm.instr_BUILD_CONST_KEY_MAP(count)
        assert self.frame.stack[0] == key_map
