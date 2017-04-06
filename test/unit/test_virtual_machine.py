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

    def test_init__frames_empty_list(self):
        assert self.vm.frames == []

    def test_init__no_current_frame(self):
        assert self.vm.current_frame == None

    def test_init__no_return_value(self):
        assert self.vm.return_value == None

    def test_push_frame__adds_frame_to_frame_stack(self):
        self.vm.push_frame(self.frame)
        assert self.vm.frames[0] == self.frame

    def test_push_frame__sets_current_frame(self):
        self.vm.push_frame(self.frame)
        assert self.vm.frames[0] == self.vm.current_frame

    def test_run_code__creates_a_new_frame(self):
        code = compile("None", "<string", 'eval')
        self.vm.run_code(code)
        assert len(self.vm.frames) == 1

    def test_run_code__sets_current_frame_to_the_new_frame(self):
        code = compile("None", "<string", 'eval')
        self.vm.run_code(code)
        assert self.vm.frames[0] == self.vm.current_frame

    def test_run_code__assigns_given_code_to_the_new_frame(self):
        code = compile("None", "<string>", "eval")
        self.vm.run_code(code)
        assert self.vm.frames[0].code == code

    def test_run_code__assigns_main_as_new_frames_name(self):
        code = compile("None", "<string>", "eval")
        self.vm.run_code(code)
        assert self.vm.frames[0].locals["__name__"] == "__main__"

    @patch('virtual_machine.Frame')
    def test_run_code__returns_the_result_of_execution(self, frame):
        code = MagicMock()
        f = MagicMock()
        f.get_next_instr.return_value = ("RETURN_VALUE", 0)
        f.stack = [10]
        frame.return_value = f
        assert self.vm.run_code(code) == 10

    def test_run_frame__stops_execution_at_return(self):
        self.frame.get_next_instr.side_effect = [("LOAD_CONST", 10), ("RETURN_VALUE", 0),
                                            ("LOAD_CONST", 15), ("RETURN_VALUE", 0)]
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.run_frame(self.frame)
        assert self.vm.return_value == 10

    def test_run_frame__raises_unsupported_instr_ex_when_instr_not_recognized(self):
        self.frame.get_next_instr.return_value = ("FAKE_INSTR", 0)
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        with pytest.raises(VirtualMachineError):
            self.vm.run_frame(self.frame)

    def test_get_func__returns_instr_function(self):
        instr = "LOAD_CONST"
        arg = 0
        assert self.vm.get_func_and_arg(instr, arg) == (self.vm.instr_LOAD_CONST, arg)

    def test_get_func__returns_binary_function_with_op_arg(self):
        instr = "BINARY_ADD"
        arg = 0
        assert self.vm.get_func_and_arg(instr, arg) == (self.vm.binary_operation, BIN_OPS["ADD"])

    def test_get_func__returns_binary_function_with_op_arg_when_inplace(self):
        instr = "INPLACE_ADD"
        arg = 0
        assert self.vm.get_func_and_arg(instr, arg) == (self.vm.binary_operation, BIN_OPS["ADD"])

    def test_get_func__returns_binary_function_with_op_arg_when_inplace_two_words(self):
        instr = "INPLACE_FLOOR_DIVIDE"
        arg = 0
        assert self.vm.get_func_and_arg(instr, arg) == (self.vm.binary_operation, BIN_OPS["FLOOR_DIVIDE"])

    def test_instr_LOAD_CONST__adds_arg_to_current_frames_stack(self):
        arg = 5
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_CONST(arg)
        assert self.frame.stack[0] == arg

    def test_instr_LOAD_GLOBAL__loads_from_builtins_to_current_frames_stack(self):
        arg = 'foo'
        self.frame.stack = []
        self.frame.built_ins = {arg: 12}
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_GLOBAL(arg)
        assert self.frame.stack == [12]

    def test_instr_LOAD_GLOBAL__raises_exception_if_name_not_found(self):
        arg = 'foo'
        self.frame.stack = []
        self.frame.built_ins = {}
        self.vm.push_frame(self.frame)
        with pytest.raises(VirtualMachineError):
            self.vm.instr_LOAD_GLOBAL(arg)

    def test_instr_LOAD_NAME__loads_from_builtins_to_current_frames_stack(self):
        arg = 'foo'
        self.frame.stack = []
        self.frame.built_ins = {arg: 12}
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_NAME(arg)
        assert self.frame.stack == [12]

    def test_instr_LOAD_NAME__loads_from_locals_to_current_frames_stack(self):
        arg = 'foo'
        self.frame.stack = []
        self.frame.locals = {arg: 12}
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_NAME(arg)
        assert self.frame.stack == [12]

    def test_instr_LOAD_NAME__raises_exception_if_name_not_found(self):
        arg = 'foo'
        self.frame.stack = []
        self.frame.built_ins = {}
        self.vm.push_frame(self.frame)
        with pytest.raises(VirtualMachineError):
            self.vm.instr_LOAD_NAME(arg)

    def test_instr_LOAD_ATTR__sets_TOS_to_attr_from_TOS(self):
        arg = 'foo'
        val = 10
        tos = MagicMock()
        setattr(tos, arg, val)
        self.frame.stack = [tos]

        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_ATTR(arg)
        assert self.frame.stack == [val]

    def test_instr_STORE_FAST__removes_top_off_current_frames_stack(self):
        self.frame.stack = [7]
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_FAST(5)
        assert len(self.frame.stack) == 0

    def test_instr_STORE_FAST__adds_arg_and_top_of_current_frames_stack_to_current_frames_locals(self):
        arg = "foo"
        self.frame.stack = [7]
        self.frame.locals = {}
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_FAST(arg)
        assert self.frame.locals == {arg: 7}

    def test_instr_STORE_NAME__removes_top_off_current_frames_stack(self):
        self.frame.stack = [7]
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_NAME(5)
        assert len(self.frame.stack) == 0

    def test_instr_STORE_NAME__adds_arg_and_top_of_current_frames_stack_to_current_frames_locals(self):
        arg = "foo"
        self.frame.stack = [7]
        self.frame.locals = {}
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_NAME(arg)
        assert self.frame.locals == {arg: 7}

    def test_instr_LOAD_FAST__loads_current_frames_local_val_to_current_frames_stack(self):
        arg = "foo"
        self.frame.stack = []
        self.frame.locals = {arg: 7}
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_FAST(arg)
        assert self.frame.stack == [7]

    def test_instr_POP_JUMP_IF_FALSE__sets_current_instruction_to_arg_when_false(self):
        arg = 1000
        self.frame.stack =[False]
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_JUMP_IF_FALSE(arg)
        assert self.frame.instr_pointer == 1000

    def test_instr_POP_JUMP_IF_FALSE__does_not_set_current_instruction_to_arg_when_true(self):
        arg = 1000
        self.frame.instr_pointer = 0
        self.frame.stack =[True]
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_JUMP_IF_FALSE(arg)
        assert self.frame.instr_pointer == 0

    def test_instr_JUMP_ABSOLUTE__sets_current_instruction_to_arg(self):
        arg = 1000
        self.vm.push_frame(self.frame)
        self.vm.instr_JUMP_ABSOLUTE(arg)
        assert self.frame.instr_pointer == arg

    def test_instr_RETURN_VALUE__sets_return_to_top_of_current_frames_stack(self):
        ret = 12
        self.frame.stack = [ret]
        self.vm.push_frame(self.frame)
        self.vm.instr_RETURN_VALUE(0)
        assert self.vm.return_value == ret

    def test_instr_SETUP_LOOP__appends_new_block_to_current_frame(self):
        arg = 1000
        current_instr_pointer = 8
        self.vm.push_frame(self.frame)
        self.frame.instr_pointer = current_instr_pointer
        self.vm.instr_SETUP_LOOP(arg)
        assert len(self.vm.current_frame.blocks) == 1

    def test_instr_SETUP_LOOP__sets_new_block_start_to_current_instr(self):
        arg = 1000
        current_instr_pointer = 8
        self.vm.push_frame(self.frame)
        self.frame.instr_pointer = current_instr_pointer
        self.vm.instr_SETUP_LOOP(arg)
        assert self.frame.blocks[0].start == 8

    def test_instr_SETUP_LOOP__sets_new_block_end_to_arg_plus_current_instr(self):
        arg = 1000
        current_instr_pointer = 8
        self.vm.push_frame(self.frame)
        self.frame.instr_pointer = current_instr_pointer
        self.vm.instr_SETUP_LOOP(arg)
        assert self.frame.blocks[0].end == 1008

    def test_instr_POP_BLOCK__pops_block_off_of_current_frame(self):
        self.frame.blocks.append(Block(1,2))
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_BLOCK(0)
        assert len(self.frame.blocks) == 0

    def test_instr_BREAK_LOOP__sets_current_instruction_to_end_of_block(self):
        end = 1000
        self.frame.blocks.append(Block(1,end))
        self.vm.push_frame(self.frame)
        self.vm.instr_BREAK_LOOP(0)
        assert self.frame.instr_pointer == end

    def test_instr_RETURN_VALUE__returns_return_control_code(self):
        ret = 12
        self.frame.stack = [ret]
        self.vm.push_frame(self.frame)
        assert self.vm.instr_RETURN_VALUE(0) == "RETURN"

    def test_instr_POP_TOP__removes_the_current_frames_top_of_stack(self):
        self.frame.stack = ["foo"]
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_TOP(0)
        assert self.frame.stack == []

    def test_instr_LOAD_BUILD_CLASS(self):
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_BUILD_CLASS(0)
        assert self.frame.stack == [__builtins__['__build_class__']]
