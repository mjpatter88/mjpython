import sys
from unittest.mock import Mock, patch

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget

from debug.dbg import Dbg
from frame import Frame


class TestDbg:
    def setup_method(self):
        self.app = QApplication(sys.argv)
        self.dbg = Dbg()

    def teardown_method(self):
        self.app.exit()

    def test_init__is_a_qt_widget(self):
        assert isinstance(self.dbg, QWidget)

    def test_init__sets_a_grid_layout(self):
        assert isinstance(self.dbg.layout(), QGridLayout)

    def test_init__adds_four_widgets_to_grid(self):
        assert self.dbg.layout().count() == 8

    def test_init__creates_new_vm(self):
        assert self.dbg.vm

    def test_init__sets_current_instruction_to_zero(self):
        assert self.dbg.current_pyc_instr == 0

    def test_open_action__names_action_open(self):
        open_action = self.dbg.open_action()
        assert open_action.text() == 'Open'

    def test_step_action__names_action_step(self):
        step_action = self.dbg.step_action()
        assert step_action.text() == 'Step'

    def test_set_local_vars__sets_local_vars_from_vm_current_frame(self):
        f = Frame(None)
        f.locals = {"foo": "bar"}
        self.dbg.vm.push_frame(f)
        self.dbg.set_local_vars()
        assert self.dbg.local_vars.item(0).text() == "foo = <class 'str'> bar"

    def test_set_local_vars__sets_multiple_local_vars_from_vm_current_frame(self):
        f = Frame(None)
        f.locals = {"foo": "bar", "a": "b"}
        self.dbg.vm.push_frame(f)
        self.dbg.set_local_vars()
        assert self.dbg.local_vars.count() == 2

    def test_step__advances_vm(self):
        vm = Mock()
        vm.current_frame.locals = {}
        self.dbg.vm = vm
        self.dbg.step()
        vm.step.assert_called()

    def test_step__advances_to_next_pyc_instruction_that_isnt_blank(self):
        vm = Mock()
        vm.current_frame.locals = {}
        self.dbg.vm = vm
        self.dbg.pyc.addItem("foo")
        self.dbg.pyc.addItem("")
        self.dbg.pyc.addItem("bar")

        self.dbg.step()

        assert self.dbg.current_pyc_instr == 2
        assert self.dbg.pyc.item(2).isSelected()
