from unittest.mock import MagicMock
from frame import Frame

import dis

class TestFrame:
    def test_init__sets_code_object(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.code == code

    def test_init__sets_stack_empty_list(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.stack == []

    def test_init__sets_instr_pointer_to_0(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.instr_pointer == 0

    def test_init__sets_locals_to_empty_dict(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.locals == {}

    def test_set_local_adds_name_and_value_in_locals(self):
        frame = Frame(MagicMock())
        name = "foo"
        value = 7
        frame.set_local(name, value)
        assert frame.locals == {name: value}

    def test_get_next_instr__returns_first_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        code.co_code = [dis.opmap[instr]]
        frame = Frame(code)
        assert frame.get_next_instr()[0] == instr

    def test_get_next_instr__increments_inst_pointer(self):
        code = MagicMock()
        code.co_code = [1]
        frame = Frame(code)
        frame.get_next_instr()
        assert frame.instr_pointer == 1

    def test_get_next_instr__returns_next_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        instr2 = "POP_TOP"
        code.co_code = [dis.opmap[instr], dis.opmap[instr2]]
        frame = Frame(code)
        frame.instr_pointer = 1
        assert frame.get_next_instr()[0] == instr2

    def test_get_next_instr__returns_local_args(self):
        code = MagicMock()
        code.co_varnames = ['foo']
        instr = "STORE_FAST"
        code.co_code = [dis.opmap[instr], 0]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == ['foo']
