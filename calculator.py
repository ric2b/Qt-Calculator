import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from calculator_design import Ui_MainWindow
# pyuic5 -x calculator_design.ui -o calculator_design.py

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for button in self.ui.numbers.buttons():
            button.clicked.connect(self.add_digit)

        self.number_string = '0'
        self.show()

    def add_digit(self):
        number = self.sender().objectName().split('_')[1]
        self.ui.lcd.display(self.number_string)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
