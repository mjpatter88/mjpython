from virtual_machine import VirtualMachine, BIN_OPS
from frame import Frame

from unittest.mock import MagicMock

class TestVirtualMachine:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.frame = MagicMock()

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

    def test_run_code__returns_the_result_of_execution(self):
        code = MagicMock()
        self.vm.return_value = 10
        assert self.vm.run_code(code) == 10

    def test_run_frame__stops_execution_at_return(self):
        self.frame.get_next_instr.side_effect = [("LOAD_CONST", 10), ("RETURN_VALUE", 0),
                                            ("LOAD_CONST", 15), ("RETURN_VALUE", 0)]
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.run_frame(self.frame)
        assert self.vm.return_value == 10

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

    def test_instr_SETUP_LOOP__sets_end_of_loop_on_current_frame_to_arg_offset(self):
        arg = 1000
        current_instr_pointer = 8
        self.vm.push_frame(self.frame)
        self.frame.instr_pointer = current_instr_pointer
        self.vm.instr_SETUP_LOOP(arg)
        expected_end_of_loop = arg + current_instr_pointer
        assert self.frame.end_of_loop == expected_end_of_loop

    def test_instr_BREAK_LOOP__sets_current_instruction_to_current_frame_loop_end(self):
        self.frame.end_of_loop = 3000
        self.vm.push_frame(self.frame)
        self.vm.instr_BREAK_LOOP(0)
        assert self.frame.instr_pointer == 3000

    def test_instr_RETURN_VALUE__returns_return_control_code(self):
        ret = 12
        self.frame.stack = [ret]
        self.vm.push_frame(self.frame)
        assert self.vm.instr_RETURN_VALUE(0) == "RETURN"
