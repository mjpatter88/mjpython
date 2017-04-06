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

    def test_init__sets_blocks_empty_list(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.blocks == []

    def test_init__sets_instr_pointer_to_0(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.instr_pointer == 0

    def test_init__sets_built_ins_to_built_ins(self):
        code = MagicMock()
        frame = Frame(code)
        assert frame.built_ins == __builtins__

    def test_init__sets_name_in_locals(self):
        code = MagicMock()
        name = "foo"
        frame = Frame(code, name)
        assert frame.locals["__name__"] == name

    def test_set_local_adds_name_and_value_in_locals(self):
        frame = Frame(MagicMock())
        name = "foo"
        value = 7
        frame.set_local(name, value)
        assert frame.locals[name] == value

    def test_get_next_instr__returns_first_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        code.co_code = [dis.opmap[instr], 0]
        frame = Frame(code)
        assert frame.get_next_instr()[0] == instr

    def test_get_next_instr__increments_inst_pointer_by_two(self):
        code = MagicMock()
        code.co_code = [1, 0]
        frame = Frame(code)
        frame.get_next_instr()
        assert frame.instr_pointer == 2

    def test_get_next_instr__returns_next_instruction(self):
        code = MagicMock()
        instr = "RETURN_VALUE"
        instr2 = "POP_TOP"
        code.co_code = [dis.opmap[instr], 0, dis.opmap[instr2], 0]
        frame = Frame(code)
        frame.instr_pointer = 2
        assert frame.get_next_instr()[0] == instr2

    def test_get_next_instr__returns_local_arg(self):
        code = MagicMock()
        code.co_varnames = ['foo']
        instr = "STORE_FAST"
        code.co_code = [dis.opmap[instr], 0]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == 'foo'

    def test_get_next_instr__returns_cmp_arg(self):
        code = MagicMock()
        instr = "COMPARE_OP"
        code.co_code = [dis.opmap[instr], 5]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == 5

    def test_get_next_instr__returns_jump_absolute_arg(self):
        code = MagicMock()
        instr = "POP_JUMP_IF_FALSE"
        code.co_code = [dis.opmap[instr], 2000]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == 2000

    def test_get_next_instr__returns_jump_relative_arg(self):
        code = MagicMock()
        instr = "SETUP_LOOP"
        code.co_code = [dis.opmap[instr], 500]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == 500

    def test_get_next_instr__returns_named_arg(self):
        code = MagicMock()
        code.co_names = ['foo']
        instr = "LOAD_NAME"
        code.co_code = [dis.opmap[instr], 0]
        frame = Frame(code)
        assert frame.get_next_instr()[1] == 'foo'
