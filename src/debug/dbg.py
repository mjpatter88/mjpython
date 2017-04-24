from dis import Bytecode

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget

from virtual_machine import VirtualMachine

PY_SRC_LABEL_POS = (1, 0)
PY_SRC_LABEL_SPAN = (1, 1)

PYC_LABEL_POS = (1, 2)
PYC_LABEL_SPAN = (1, 1)

PY_SRC_POS = (2, 0)
PY_SRC_SPAN = (1, 2)

PYC_POS = (2, 2)
PYC_SPAN = (1, 2)

CALL_STACK_LABEL_POS = (3, 0)
CALL_STACK_LABEL_SPAN = (1, 1)

LOCAL_VARS_LABEL_POS = (3, 2)
LOCAL_VARS_LABEL_SPAN = (1, 1)

CALL_STACK_POS = (4, 0)
CALL_STACK_SPAN = (1, 2)

LOCAL_VARS_POS = (4, 2)
LOCAL_VARS_SPAN = (1, 2)


class Dbg(QWidget):
    def __init__(self):
        super().__init__()

        self.vm = VirtualMachine()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        py_src_label = QLabel('Python Source')
        pyc_label = QLabel('CPython Bytecode')
        self.py_src = QListWidget()
        self.pyc = QListWidget()

        self.grid.addWidget(py_src_label, *PY_SRC_LABEL_POS, *PY_SRC_LABEL_SPAN)
        self.grid.addWidget(pyc_label, *PYC_LABEL_POS, *PYC_LABEL_SPAN)
        self.grid.addWidget(self.py_src, *PY_SRC_POS, *PY_SRC_SPAN)
        self.grid.addWidget(self.pyc, *PYC_POS, *PYC_SPAN)
        self.grid.setRowStretch(PY_SRC_POS[0], 2)

        call_stack_label = QLabel('Call Stack')
        local_vars_label = QLabel('Locals')
        self.call_stack = QListWidget()
        self.local_vars = QListWidget()

        self.grid.addWidget(call_stack_label, *CALL_STACK_LABEL_POS, *PY_SRC_LABEL_SPAN)
        self.grid.addWidget(local_vars_label, *LOCAL_VARS_LABEL_POS, *PYC_LABEL_SPAN)
        self.grid.addWidget(self.call_stack, *CALL_STACK_POS, *PY_SRC_SPAN)
        self.grid.addWidget(self.local_vars, *LOCAL_VARS_POS, *PYC_SPAN)

    def open_action(self):
        open_icon = QIcon.fromTheme('folder')
        open_action = QAction(open_icon, 'Open', self)
        open_action.triggered.connect(self.show_open_dialog)
        return open_action

    def show_open_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')

        if file_name[0]:
            self.load_py_src(file_name[0])
            self.load_pyc(file_name[0])
            self.init_vm(file_name[0])
            self.set_local_vars()

    def load_py_src(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.read().splitlines()

        for line in lines:
            self.py_src.addItem(line)

    def load_pyc(self, file_name):
        pyc = compile_file(file_name)
        bc = Bytecode(pyc)

        for line in bc.dis().splitlines():
            self.pyc.addItem(line)

    def init_vm(self, file_name):
        pyc = compile_file(file_name)
        self.vm.set_code(pyc)

    def set_local_vars(self):
        for item in self.vm.current_frame.locals.items():
            self.local_vars.addItem("{} = {} {}".format(item[0], type(item[1]), item[1]))


def compile_file(file_name):
    with open(file_name, 'r') as f:
        pyc = compile(f.read(), file_name, 'exec')
    return pyc
