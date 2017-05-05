#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from debug.dbg import Dbg


class Main(QMainWindow):
    def __init__(self, test=False):
        super().__init__()
        self.setWindowTitle("mjpython debugger")
        self.setGeometry(100, 100, 1500, 800)

        self.dbg = Dbg()
        self.setCentralWidget(self.dbg)

        self.setup_toolbar(self.dbg)

        if not test:
            self.show()

    def setup_toolbar(self, dbg):
        toolbar = self.addToolBar('Open')
        toolbar.addAction(dbg.open_action())
        toolbar.addAction(dbg.step_action())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugger = Main()
    sys.exit(app.exec())
