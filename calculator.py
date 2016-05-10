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

        for button in self.ui.operations.buttons():
            button.clicked.connect(self.operation)

        self.ui.clear.clicked.connect(self.clear_lcd)
        self.ui.equals.clicked.connect(self.equals)
        self.ui.dot.clicked.connect(self.add_dot)

        self.operation = None
        self.new_operation = False
        self.number_string = '0'
        self.A = 0
        self.B = 0    
        self.show()

    def add_digit(self):
        if len(self.number_string) >= 8:
            return

        number = self.sender().objectName().split('_')[1]

        if self.number_string == '0':
            self.number_string = number
        else: 
            self.number_string += number
        self.ui.lcd.display(self.number_string)

    def add_dot(self):
        if '.' not in self.number_string:
            self.number_string += '.'
        print(self.number_string)

    def operation(self):
        self.operation = self.sender().objectName()
        self.new_operation = True
        self.A = float(self.number_string)
        self.number_string = '0'

    def equals(self):
        if self.operation == None:
            print('empty')
            return

        if self.new_operation:
            self.B = float(self.number_string)

        if self.operation == 'add':
            self.A += self.B
        if self.operation == 'subtract':
            self.A -= self.B
        if self.operation == 'multiply':
            self.A *= self.B
        if self.operation == 'divide':
            self.A /= self.B

        self.number_string = '0'
        self.ui.lcd.display(self.A)
        self.previous_operation = self.operation
        self.new_operation = False

    def clear_lcd(self):
        self.number_string = '0'
        self.ui.lcd.display('0')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
