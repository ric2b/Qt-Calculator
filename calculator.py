import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from calculator_design import Ui_MainWindow
# pyuic5 -x calculator_design.ui -o calculator_design.py

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
