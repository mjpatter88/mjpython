import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtTest import QTest

from debug.dbg import Dbg


class TestDbg:
    def setup_method(self):
        self.app = QApplication(sys.argv)
        self.dbg = Dbg()
        QTest.qWaitForWindowActive(self.dbg)

    def teardown_method(self):
        self.app.exit()

    def test_app_is_active(self):
        assert self.dbg.isActiveWindow()
