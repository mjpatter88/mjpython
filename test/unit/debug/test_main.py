import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from debug.main import Main


class TestMain:
    def setup_method(self):
        self.app = QApplication(sys.argv)
        self.main = Main(test=True)

    def teardown_method(self):
        self.app.exit()

    def test_init__is_a_qt_main_window(self):
        assert isinstance(self.main, QMainWindow)

    def test_init__sets_window_title(self):
        assert self.main.windowTitle() == "mjpython debugger"

    def test_init__sets_geometry(self):
        rect = self.main.geometry()
        assert (rect.x(), rect.y(), rect.width(), rect.height()) == (100, 100, 1500, 800)
