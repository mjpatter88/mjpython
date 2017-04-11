import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Dbg(QMainWindow):
    def __init__(self, test=False):
        super().__init__()
        self.setWindowTitle("mjpython debugger")
        self.setGeometry(100, 100, 1500, 800)

        if not test:
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugger = Dbg()
    sys.exit(app.exec())
