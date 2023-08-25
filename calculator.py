from GUI import Ui_MainWindow as interface
from PyQt5 import QtWidgets
from math import *
import sys
import re

class Calculator(interface):  
    def __innit__(self):
        self.zero_btn.clicked.connect(lambda: self.write(self.zero_btn.text()))
        self.one_btn.clicked.connect(lambda: self.write(self.one_btn.text()))
        self.two_btn.clicked.connect(lambda: self.write(self.two_btn.text()))
        self.three_btn.clicked.connect(lambda: self.write(self.three_btn.text()))
        self.four_btn.clicked.connect(lambda: self.write(self.four_btn.text()))
        self.five_btn.clicked.connect(lambda: self.write(self.five_btn.text()))
        self.six_btn.clicked.connect(lambda: self.write(self.six_btn.text()))
        self.seven_btn.clicked.connect(lambda: self.write(self.seven_btn.text()))
        self.eight_btn.clicked.connect(lambda: self.write(self.eight_btn.text()))
        self.nine_btn.clicked.connect(lambda: self.write(self.nine_btn.text()))
        self.comma_btn.clicked.connect(lambda: self.write(self.comma_btn.text()))
        self.plus_btn.clicked.connect(lambda: self.write(self.plus_btn.text()))
        self.minus_btn.clicked.connect(lambda: self.write(self.minus_btn.text()))
        self.division_btn.clicked.connect(lambda: self.write(self.division_btn.text()))
        self.multy_btn.clicked.connect(lambda: self.write(self.multy_btn.text()))
        
        self.equals_btn.clicked.connect(self.equals) #work
        self.sqrt_btn.clicked.connect(self.sqrt) #work
        self.power_btn.clicked.connect(self.power) #worl
        self.percent_btn.clicked.connect(self.percent) #work
        self.del_btn.clicked.connect(self.delete) #work
        self.absolut_negative_btn.clicked.connect(self.absolut_negative) #need to fix
        self.fraction_btn.clicked.connect(self.fraction) #work
        self.clea_all_btn.clicked.connect(self.clear_all) #work
        self.clear_btn.clicked.connect(self.clear) #work

    def start(self, window):
        interface.setupUi(self, window)
        interface.retranslateUi(self, window)
        self.__innit__()

    def clear(self):
        string = self.spliteString()
        if len(string) != 1:
            self.result_label.setText(self.result_label.text().rstrip(str(string))) 
        else:
            self.result_label.setText("0")

    def clear_all(self):
        self.result_label.setText("0")

    def delete(self):
        if len(self.result_label.text()) == 1:
            self.result_label.setText("0") 
        else:
            self.result_label.setText(self.result_label.text()[:-1])

    def charaCheck(self, number):
        string = self.result_label.text() + number
        return True if string[len(string)-1].isdigit() == True else False
    
    def spliteString(self):
        res = re.split("\/|\*|-|\+", self.result_label.text())
        return res
        
    def write(self, number):
        if self.result_label.text() == "0" and self.charaCheck(number) == True:
            self.result_label.setText(number)
        elif self.charaCheck(number) == False and self.result_label.text()[len(self.result_label.text())-1].isdigit() == False:
            string = self.result_label.text()[:-1]
            self.result_label.setText(string + number)
        else:
            self.result_label.setText(self.result_label.text() + number)
    
    def equals(self):
        if self.result_label.text()[len(self.result_label.text())-1].isdigit():
            res = eval(self.result_label.text())
            self.result_label.setText(str(res))

    def percent(self):
        string = self.spliteString()
        if len(string) > 1:
            res = float(string[len(string)-1])*0.1    
            self.result_label.setText(self.result_label.text().rstrip(str(string)) + str(res))

    def absolut_negative(self):
        string = self.spliteString()
        res = float(string[len(string)-1])*-1    
        self.result_label.setText(self.result_label.text().rstrip(str(string)) + str(res))

    def fraction(self):
        string = self.spliteString()
        res = 1/float(string[len(string)-1])
        self.result_label.setText(self.result_label.text().rstrip(str(string)) + str(res))

    def power(self):
        string = self.spliteString()
        res = pow(float(string[len(string)-1]),2)
        res = str(int(res)) if res % 1 == 0 else str(res)
        self.result_label.setText(self.result_label.text().rstrip(str(string)) + str(res))
    
    def sqrt(self):
        # string = [x for x in self.spliteString()] <--тоже работает, чисто поржать
        string = self.spliteString()
        res = sqrt(float(string[len(string)-1]))
        res = str(int(res)) if res % 1 == 0 else str(res)
        self.result_label.setText(self.result_label.text().rstrip(str(string)) + str(res))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    calc = Calculator()
    calc.start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())