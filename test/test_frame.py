from unittest.mock import MagicMock
from frame import Frame

import dis

class TestFrame:
    def test_init__sets_code_object(self):
        code = MagicMock()
        self.frame = Frame(code)
        assert self.frame.code == code

    def test_init__sets_stack_empty_list(self):
        code = MagicMock()
        self.frame = Frame(code)
        assert self.frame.stack == []

    def test_init__sets_instr_pointer_to_0(self):
        code = MagicMock()
        self.frame = Frame(code)
        assert self.frame.instr_pointer == 0

    def test_get_next_instr__returns_first_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        code.co_code = [dis.opmap[instr]]
        self.frame = Frame(code)
        assert self.frame.get_next_instr()[0] == instr

    def test_get_next_instr__increments_inst_pointer(self):
        code = MagicMock()
        code.co_code = [1]
        self.frame = Frame(code)
        self.frame.get_next_instr()
        assert self.frame.instr_pointer == 1

    def test_get_next_instr__returns_next_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        instr2 = "POP_TOP"
        code.co_code = [dis.opmap[instr], dis.opmap[instr2]]
        self.frame = Frame(code)
        self.frame.instr_pointer = 1
        assert self.frame.get_next_instr()[0] == instr2

    def test_get_next_instr__returns_const_args(self):
        code = MagicMock()
        code.co_consts = [None, 2]
        instr = "LOAD_CONST"
        code.co_code = [dis.opmap[instr], 1]
        self.frame = Frame(code)
        assert self.frame.get_next_instr()[1] == [2]
