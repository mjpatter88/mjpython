from virtual_machine import VirtualMachine, BIN_OPS, VirtualMachineError
from frame import Frame
from block import Block

from unittest.mock import MagicMock, patch
import pytest

class TestVirtualMachine:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.frame = MagicMock()
        self.frame.blocks = []

    def test_instr_CALL_FUNCTION__calls_function_on_top_of_stack(self):
        func = MagicMock()
        arg = 0
        self.frame.stack = [func]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION(arg)
        func.assert_called()

    def test_instr_CALL_FUNCTION__sets_TOS_to_funcs_return(self):
        func = MagicMock()
        func.return_value = 2
        arg = 0
        self.frame.stack = [func]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION(arg)
        assert self.frame.stack == [2]

    def test_instr_CALL_FUNCTION__passes_one_positional_arg(self):
        func = MagicMock()
        arg = 1
        func_arg = "foo"
        self.frame.stack = [func, func_arg]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION(arg)
        func.assert_called_with(func_arg)

    def test_instr_CALL_FUNCTION__passes_multiple_positional_arg(self):
        func = MagicMock()
        arg = 3
        self.frame.stack = [func, 3, 2, 1]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION(arg)
        func.assert_called_with(1, 2, 3)
