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

    def test_instr_COMPARE_OP__not_in_sets_top_of_stack_to_false(self):
        a = 5
        b = [5, 10]
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([7])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__not_in_sets_top_of_stack_to_true(self):
        a = 5
        b = [7, 10]
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([7])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__is_sets_top_of_stack_to_false(self):
        a = MagicMock()
        b = 5
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([8])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__is_sets_top_of_stack_to_true(self):
        a = MagicMock()
        b = a
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([8])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__not_is_sets_top_of_stack_to_false(self):
        a = MagicMock()
        b = a
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([9])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__not_is_sets_top_of_stack_to_true(self):
        a = MagicMock()
        b = 5
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([9])
        assert frame.stack == [True]

    def test_instr_COMPARE_OP__is_subclass_sets_top_of_stack_to_false(self):
        a = MagicMock
        b = int
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([10])
        assert frame.stack == [False]

    def test_instr_COMPARE_OP__is_subclass_sets_top_of_stack_to_true(self):
        a = MagicMock
        b = object
        frame = MagicMock()
        frame.stack = [a, b]
        self.vm.push_frame(frame)
        self.vm.instr_COMPARE_OP([10])
        assert frame.stack == [True]
