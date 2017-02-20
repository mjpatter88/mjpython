from virtual_machine import VirtualMachine
from frame import Frame

from unittest.mock import MagicMock

class TestVirtualMachine:
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_instr_COMPARE_OP__lt_sets_top_of_stack_to_false(self):
        a = 10
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([0])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__lt_sets_top_of_stack_to_true(self):
        a = 7
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([0])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__le_sets_top_of_stack_to_false(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([1])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__le_sets_top_of_stack_to_true(self):
        a = 10
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([1])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__eq_sets_top_of_stack_to_false(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([2])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__eq_sets_top_of_stack_to_true(self):
        a = 10
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([2])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__ne_sets_top_of_stack_to_false(self):
        a = 10
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([3])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__ne_sets_top_of_stack_to_true(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([3])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__gt_sets_top_of_stack_to_false(self):
        a = 7
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([4])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__gt_sets_top_of_stack_to_true(self):
        a = 10
        b = 7
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([4])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__ge_sets_top_of_stack_to_false(self):
        a = 7
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([5])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__ge_sets_top_of_stack_to_true(self):
        a = 10
        b = 10
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([5])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__in_sets_top_of_stack_to_false(self):
        a = 7
        b = [10]
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([6])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__in_sets_top_of_stack_to_true(self):
        a = 10
        b = [7, 10]
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([6])
        assert frame.stack == [True]
