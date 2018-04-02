
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
#import threading

#def HelloPrint():
#	print("Hello Print")

class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 1000, 700)
		

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        
        btn1 = QPushButton("Login", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)
		#print("Hello")

        btn2 = QPushButton("Check State", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)
		print("Hello")

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")

    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
        else :
            self.statusBar().showMessage("Connected")


print("Go")
if __name__ == "__main__":
    print("Hello World")
    app = QApplication(sys.argv)
    myWin = HelloWindow()
    myWin.show()
    app.exec_()