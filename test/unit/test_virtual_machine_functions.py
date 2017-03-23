from virtual_machine import VirtualMachine, BIN_OPS, VirtualMachineError
from frame import Frame
from block import Block

from unittest.mock import MagicMock, patch, ANY
import pytest

class TestVirtualMachineFunctions:
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

    def test_instr_CALL_FUNCTION_KW__passes_keyword_args(self):
        func = MagicMock()
        self.frame.stack = [func, 1, 2, 3, ('a', 'b', 'c')]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION_KW(0)
        func.assert_called_with(a=1, b=2, c=3)

    def test_instr_CALL_FUNCTION_KW__passes_keyword_args_and_pos_args(self):
        func = MagicMock()
        arg = 4
        self.frame.stack = [func, 0, 1, 2, 3, ('a', 'b', 'c')]
        self.vm.push_frame(self.frame)
        self.vm.instr_CALL_FUNCTION_KW(arg)
        func.assert_called_with(0, a=1, b=2, c=3)

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_and_adds_it_to_TOS(self, make_func):
        func = MagicMock()
        make_func.return_value = func
        self.frame.stack = ["foo_code", "foo"]
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(0)
        assert self.frame.stack == [func]

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_with_code_from_TOS_1(self, make_func):
        code = MagicMock()
        self.frame.stack = [code, "foo"]
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(0)
        make_func.assert_called_with(code, ANY, name=ANY, argdefs=ANY)

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_with_builtins_from_current_frame(self, make_func):
        built_ins = {"foo": "bar"}
        self.frame.stack = ["foo", "foo"]
        self.frame.built_ins = built_ins
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(0)
        make_func.assert_called_with(ANY, built_ins, name=ANY, argdefs=ANY)

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_with_default_pos_arg_values(self, make_func):
        def_args = (1, 4, 9)
        self.frame.stack = [def_args, "foo", "foo"]
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(1)
        make_func.assert_called_with(ANY, ANY, name=ANY, argdefs=def_args)

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_with_default_keyword_arg_values(self, make_func):
        def_args = {'a':1, 'b':4, 'c':9}
        self.frame.stack = [def_args, "foo", "foo"]
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(2)
        assert self.frame.stack[0].__kwdefaults__ == def_args

    @patch('virtual_machine.FunctionType')
    def test_instr_MAKE_FUNCTION__creates_new_function_with_name_from_TOS(self, make_func):
        name = "func_name"
        self.frame.stack = ["foo", name]
        self.vm.push_frame(self.frame)
        self.vm.instr_MAKE_FUNCTION(0)
        make_func.assert_called_with(ANY, ANY, name=name, argdefs=ANY)
