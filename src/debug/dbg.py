from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget


class Dbg(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        grid.setSpacing(10)

        l = QListWidget()
        l2 = QListWidget()
        for x in range(100):
            l.addItem("Item {}".format(x))
            l2.addItem("Another Item {}".format(x))
        grid.addWidget(l, 0, 0)
        grid.addWidget(l2, 0, 1)

        self.setLayout(grid)


