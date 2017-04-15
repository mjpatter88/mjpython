from dis import Bytecode

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class Dbg(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        self.py_src = QListWidget()
        self.pyc = QListWidget()

        self.grid.addWidget(self.py_src, 1, 0, 1, 2)
        self.grid.addWidget(self.pyc, 1, 2, 1, 2)

        self.add_open_button()


    def add_open_button(self):
        open_button = QPushButton("Open File")
        open_button.setMinimumHeight(100)
        open_button.clicked.connect(self.show_open_dialog)

        self.grid.addWidget(open_button, 0, 1, 1, 2)

    def show_open_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')

        if file_name[0]:
            self.load_py_src(file_name[0])
            self.load_pyc(file_name[0])

    def load_py_src(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.read().splitlines()

        for line in lines:
            self.py_src.addItem(line)

    def load_pyc(self, file_name):
        with open(file_name, 'r') as f:
            pyc = compile(f.read(), file_name, 'exec')

        bc = Bytecode(pyc)

        for line in bc.dis().splitlines():
            self.pyc.addItem(line)
