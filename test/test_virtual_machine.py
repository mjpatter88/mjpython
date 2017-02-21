from virtual_machine import VirtualMachine
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
        self.frame.get_next_instr.side_effect = [("LOAD_CONST", [10]), ("RETURN_VALUE", []),
                                            ("LOAD_CONST", [15]), ("RETURN_VALUE", [])]
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.run_frame(self.frame)
        assert self.vm.return_value == 10

    def test_instr_LOAD_CONST__adds_arg_to_current_frames_stack(self):
        arg = 5
        self.frame.stack = []
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_CONST([arg])
        assert self.frame.stack[0] == arg

    def test_instr_STORE_FAST__removes_top_off_current_frames_stack(self):
        arg = 5
        self.frame.stack = [7]
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_FAST([arg])
        assert len(self.frame.stack) == 0

    def test_instr_STORE_FAST__adds_arg_and_top_of_current_frames_stack_to_current_frames_locals(self):
        arg = "foo"
        self.frame.stack = [7]
        self.frame.locals = {}
        self.vm.push_frame(self.frame)
        self.vm.instr_STORE_FAST([arg])
        assert self.frame.locals == {arg: 7}

    def test_instr_LOAD_FAST__loads_current_frames_local_val_to_current_frames_stack(self):
        arg = "foo"
        self.frame.stack = []
        self.frame.locals = {arg: 7}
        self.vm.push_frame(self.frame)
        self.vm.instr_LOAD_FAST([arg])
        assert self.frame.stack == [7]

    def test_instr_POP_JUMP_IF_FALSE__sets_current_instruction_to_arg_when_false(self):
        arg = 1000
        self.frame.stack =[False]
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_JUMP_IF_FALSE([arg])
        assert self.frame.instr_pointer == 1000

    def test_instr_POP_JUMP_IF_FALSE__does_not_set_current_instruction_to_arg_when_true(self):
        arg = 1000
        self.frame.instr_pointer = 0
        self.frame.stack =[True]
        self.vm.push_frame(self.frame)
        self.vm.instr_POP_JUMP_IF_FALSE([arg])
        assert self.frame.instr_pointer == 0

    def test_instr_RETURN_VALUE__sets_return_to_top_of_current_frames_stack(self):
        ret = 12
        self.frame.stack = [ret]
        self.vm.push_frame(self.frame)
        self.vm.instr_RETURN_VALUE()
        assert self.vm.return_value == ret

    def test_instr_RETURN_VALUE__returns_return_control_code(self):
        ret = 12
        self.frame.stack = [ret]
        self.vm.push_frame(self.frame)
        assert self.vm.instr_RETURN_VALUE() == "RETURN"
