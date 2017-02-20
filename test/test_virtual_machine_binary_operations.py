from virtual_machine import VirtualMachine
from frame import Frame

from unittest.mock import MagicMock

class TestVirtualMachineBinaryOperations:
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_instr_BINARY_ADD__sets_top_of_stack_to_sum_of_top_two_on_stack(self):
        a = 7
        b = 8
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_BINARY_ADD()
        assert frame.stack == [a+b]

    def test_instr_BINARY_ADD__concatenates_two_strings(self):
        a = "Foo"
        b = "bar"
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_BINARY_ADD()
        assert frame.stack == [a+b]

    def test_instr_BINARY_SUBTRACT__sets_top_of_stack_to_s1_minus_s0(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_BINARY_SUBTRACT()
        assert frame.stack == [a-b]

    def test_instr_BINARY_MULTIPLY__sets_top_of_stack_to_s1_times_s0(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_BINARY_MULTIPLY()
        assert frame.stack == [a*b]
