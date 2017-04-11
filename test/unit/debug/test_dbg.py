import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtTest import QTest

from debug.dbg import Dbg


class TestDbg:
    def setup_method(self):
        self.app = QApplication(sys.argv)
        self.dbg = Dbg(test=True)

    def teardown_method(self):
        self.app.exit()

    def test_init__is_a_qt_main_window(self):
        assert isinstance(self.dbg, QMainWindow)
        self.dbg.layout()

    def test_init__sets_window_title(self):
        assert self.dbg.windowTitle() == "mjpython debugger"

    def test_init__sets_geometry(self):
        rect = self.dbg.geometry()
        assert (rect.x(), rect.y(), rect.width(), rect.height()) == (100, 100, 1500, 800)
