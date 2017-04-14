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

        self.python_source = QListWidget()

        l2 = QListWidget()
        for x in range(100):
            l2.addItem("Another Item {}".format(x))
        self.grid.addWidget(self.python_source, 1, 0, 1, 2)
        self.grid.addWidget(l2, 1, 2, 1, 2)

        self.add_open_button()

        self.setLayout(self.grid)

    def add_open_button(self):
        open_button = QPushButton("Open File")
        open_button.setMinimumHeight(100)
        open_button.clicked.connect(self.show_open_dialog)

        self.grid.addWidget(open_button, 0, 1, 1, 2)

    def show_open_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')

        if file_name[0]:
            self.load_source_code(file_name[0])

    def load_source_code(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.read().splitlines()

        for line in lines:
            self.python_source.addItem(line)
