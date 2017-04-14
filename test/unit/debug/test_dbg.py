import sys
from unittest import mock
from unittest.mock import patch

from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
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
