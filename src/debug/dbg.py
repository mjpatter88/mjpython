import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


class Content(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        grid.setSpacing(10)

        l = QListWidget()
        l.addItem("Test")
        l.addItem("Test2")
        grid.addWidget(l, 0, 0)

        l2 = QListWidget()
        l2.addItem("Test3")
        l2.addItem("Test4")
        grid.addWidget(l2, 0, 1)

        self.setLayout(grid)


class Dbg(QMainWindow):
    def __init__(self, test=False):
        super().__init__()
        self.setWindowTitle("mjpython debugger")
        self.setGeometry(100, 100, 1500, 800)

        self.setCentralWidget(Content())

        if not test:
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugger = Dbg()
    sys.exit(app.exec())
