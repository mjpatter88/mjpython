from virtual_machine import VirtualMachine, BIN_OPS
from frame import Frame

from unittest.mock import MagicMock

class TestVirtualMachineBinaryOperations:
    def setup_method(self):
        self.vm = VirtualMachine()
        self.a = 7
        self.b = 8
        frame = MagicMock()
        frame.stack = [self.a, self.b]
        self.vm.push_frame(frame)

    def test_instr_BINARY_ADD__sets_top_of_stack_to_sum_of_top_two_on_stack(self):
        func = BIN_OPS["BINARY_ADD"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a + self.b]

    def test_instr_BINARY_ADD__concatenates_two_strings(self):
        a = "Foo"
        b = "bar"
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        func = BIN_OPS["BINARY_ADD"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [a + b]

    def test_instr_BINARY_SUBTRACT__sets_top_of_stack_to_s1_minus_s0(self):
        func = BIN_OPS["BINARY_SUBTRACT"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a - self.b]

    def test_instr_BINARY_MULTIPLY__sets_top_of_stack_to_s1_times_s0(self):
        func = BIN_OPS["BINARY_MULTIPLY"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a * self.b]

    def test_instr_BINARY_POWER__sets_top_of_stack_to_s1_to_the_power_of_s0(self):
        func = BIN_OPS["BINARY_POWER"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a ** self.b]

    def test_instr_BINARY_FLOOR_DIVIDE__sets_top_of_stack_to_s1_divided_by_s0_rounded_down(self):
        func = BIN_OPS["BINARY_FLOOR_DIVIDE"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a // self.b]

    def test_instr_BINARY_TRUE_DIVIDE__sets_top_of_stack_to_s1_divided_by_s0(self):
        func = BIN_OPS["BINARY_TRUE_DIVIDE"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a / self.b]

    def test_instr_BINARY_MODULO__sets_top_of_stack_to_s1_modulus_s0(self):
        func = BIN_OPS["BINARY_MODULO"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a % self.b]

    def test_instr_BINARY_SUBSCR__sets_top_of_stack_to_s1_subscr_s0(self):
        a = [0,2,4,6]
        b = 2
        self.vm.current_frame.stack = [a, b]
        func = BIN_OPS["BINARY_SUBSCR"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [a[b]]

    def test_instr_BINARY_LSHIFT__sets_top_of_stack_to_s1_left_shifted_by_s0(self):
        func = BIN_OPS["BINARY_LSHIFT"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a << self.b]

    def test_instr_BINARY_RSHIFT__sets_top_of_stack_to_s1_right_shifted_by_s0(self):
        func = BIN_OPS["BINARY_RSHIFT"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a >> self.b]

    def test_instr_BINARY_AND__sets_top_of_stack_to_s1_anded_with_s0(self):
        func = BIN_OPS["BINARY_AND"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a & self.b]

    def test_instr_BINARY_XOR__sets_top_of_stack_to_s1_xored_with_s0(self):
        func = BIN_OPS["BINARY_XOR"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a ^ self.b]

    def test_instr_BINARY_OR__sets_top_of_stack_to_s1_ored_with_s0(self):
        func = BIN_OPS["BINARY_OR"]
        self.vm.binary_operation(func)
        assert self.vm.current_frame.stack == [self.a | self.b]
