import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from debug.dbg import Dbg


class Main(QMainWindow):
    def __init__(self, test=False):
        super().__init__()
        self.setWindowTitle("mjpython debugger")
        self.setGeometry(100, 100, 1500, 800)

        self.setCentralWidget(Dbg())

        if not test:
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugger = Main()
    sys.exit(app.exec())
