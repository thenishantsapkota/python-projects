from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
import sys
import math
import time

from PyQt5.uic import loadUiType

ui,_ = loadUiType('calculator.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
        #self.Dark_Blue_Theme()
        
    
    def Handle_UI_Changes(self):
        self.lineEdit.setEnabled(False)
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Backspace)
        self.pushButton_2.clicked.connect(self.Press_C)
        #self.pushButton_2.clicked.connect(self.Backspace)
        self.pushButton_3.clicked.connect(self.Off)
        #self.pushButton_4.clicked.connect(self.Backspace)
        self.pushButton_5.clicked.connect(self.Press_8)
        self.pushButton_6.clicked.connect(self.Press_7)
        self.pushButton_7.clicked.connect(self.Press_9)
        self.pushButton_8.clicked.connect(self.Press_Plus)
        self.pushButton_9.clicked.connect(self.Press_5)
        self.pushButton_10.clicked.connect(self.Press_4)
        self.pushButton_11.clicked.connect(self.Press_6)
        self.pushButton_12.clicked.connect(self.Press_Minus)
        self.pushButton_13.clicked.connect(self.Press_2)
        self.pushButton_14.clicked.connect(self.Press_1)
        self.pushButton_15.clicked.connect(self.Press_3)
        self.pushButton_16.clicked.connect(self.Press_Multiply)
        self.pushButton_20.clicked.connect(self.Press_Divide)
        self.pushButton_18.clicked.connect(self.Press_0)
        self.pushButton_19.clicked.connect(self.Press_Equals)
        self.pushButton_17.clicked.connect(self.Press_Dot)
        self.pushButton_22.clicked.connect(self.Press_Sin)
        self.pushButton_21.clicked.connect(self.Press_Cos)
        self.pushButton_23.clicked.connect(self.Press_Tan)
        self.pushButton_24.clicked.connect(self.Press_Power)
        self.pushButton_28.clicked.connect(self.Press_SQRT)
        self.pushButton_30.clicked.connect(self.Bracket_Close)
        self.pushButton_29.clicked.connect(self.Bracket_Open)

    def Off(self):
        exit(0)
        

    def Backspace(self):
        self.lineEdit.backspace()
    
    def Press_C(self):
        self.lineEdit.clear()
    
    def Press_CE(self):
        self.lineEdit.clear()
    
    def PressPlusMinus(self):
        pass

    def Press_9(self):
        self.lineEdit.insert('9')
    
    def Press_8(self):
        self.lineEdit.insert('8')

    def Press_7(self):
        self.lineEdit.insert('7')

    def Press_6(self):
        self.lineEdit.insert('6')

    def Press_5(self):
        self.lineEdit.insert('5')

    def Press_4(self):
        self.lineEdit.insert('4')

    def Press_3(self):
        self.lineEdit.insert('3')

    def Press_2(self):
        self.lineEdit.insert('2')

    def Press_1(self):
        self.lineEdit.insert('1')

    def Press_0(self):
        self.lineEdit.insert('0')
    
    def Press_Plus(self):
        self.lineEdit.insert('+')
    
    def Press_Minus(self):
        self.lineEdit.insert('-')
    
    def Press_Multiply(self):
        self.lineEdit.insert('*')
    
    def Press_Divide(self):
        self.lineEdit.insert('/')
    
    def Press_Dot(self):
        self.lineEdit.insert('.')
    
    def Press_Sin(self):
        self.lineEdit.insert('sin ')
    
    def Press_Cos(self):
        self.lineEdit.insert('cos ')
    
    def Press_Tan(self):
        self.lineEdit.insert('tan ')
    
    def Press_Power(self):
        self.lineEdit.insert('^')
    
    def Press_SQRT(self):
        self.lineEdit.insert('√')
    
    def Bracket_Open(self):
        self.lineEdit.insert('(')
    
    def Bracket_Close(self):
        self.lineEdit.insert(')')
    

    def Press_Equals(self):
        string = self.lineEdit.text()
        #print(string)
        
        if '+' in string:
            result = float(eval(string))
            self.lineEdit.setText(str(result))

        if '-' in string:
            result = float(eval(string))
            self.lineEdit.setText(str(result))

        if '*' in string:
            result = float(eval(string))
            self.lineEdit.setText(str(result))
        
        if '/' in string:
            result = float(eval(string))
            self.lineEdit.setText(str(result))
        
        if 'sin' in string:
            try:
                partitioned_string = string.partition('sin')
                #print(partitioned_string)
                sine = math.sin(math.radians(float(partitioned_string[2])))
                if partitioned_string[0] == '':
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(sine))

                else:
                    final_sine = float(sine) * float(partitioned_string[0])
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(final_sine))
            except:
                pass
        if 'cos' in string:
            try:
                partitioned_string = string.partition('cos')
                #print(partitioned_string)
                cosine = math.cos(math.radians(float(partitioned_string[2])))
                if partitioned_string[0] == '':
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(cosine))

                else:
                    final_cosine = float(cosine) * float(partitioned_string[0])
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(final_cosine))
            except:
                pass
        
        if 'tan' in string:
            try:
                partitioned_string = string.partition('tan')
                #print(partitioned_string)
                tan = math.tan(math.radians(float(partitioned_string[2])))
                if partitioned_string[0] == '':
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(tan))

                else:
                    final_tan = float(tan) * float(partitioned_string[0])
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(final_tan))
            except:
                pass
        
        if '^' in string:
            try:
                partitioned_string = string.partition('^')
                #print(partitioned_string)
                power = pow(float(partitioned_string[0]), float(partitioned_string[2]))
                #print(power)
                self.lineEdit.clear()
                self.lineEdit.setText(str(power))
            
            except:
                pass
        
        if '√' in string:
            try:
                partitioned_string = string.partition('√')
                #print(partitioned_string)
                square_root = math.sqrt(float(partitioned_string[2]))
                if partitioned_string[0] == '':
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(square_root))
                
                else:
                    final_sqrt = float(square_root) * float(partitioned_string[0])
                    self.lineEdit.clear()
                    self.lineEdit.setText(str(final_sqrt))
                    test = self.lineEdit.text()

            except:
                pass
            
    #def Dark_Blue_Theme(self):
        #style = open('themes/darkblue.css' , 'r')
        #style = style.read()
        #self.setStyleSheet(style)

            
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
        
