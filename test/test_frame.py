from unittest.mock import MagicMock
from frame import Frame

class TestFrame:
    def test_init__sets_code_object(self):
        code = MagicMock()
        self.frame = Frame(code)
        assert self.frame.code == code

    def test_init__sets_stack_empty_list(self):
        code = MagicMock()
        self.frame = Frame(code)
        assert self.frame.stack == []
