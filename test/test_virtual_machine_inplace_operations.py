from virtual_machine import VirtualMachine
from frame import Frame

from unittest.mock import MagicMock

class TestVirtualMachineBinaryOperations:
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_instr_INPLACE_ADD__sets_top_of_stack_to_sum_of_s0_and_s1(self):
        a = 10
        b = 100
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_INPLACE_ADD()
        assert frame.stack == [a+b]
