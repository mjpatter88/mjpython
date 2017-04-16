import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget

from debug.dbg import Dbg


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

    def test_open_action__names_action_open(self):
        open_action = self.dbg.open_action()
        assert open_action.text() == 'Open'
