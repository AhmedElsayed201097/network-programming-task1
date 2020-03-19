from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
import sys
from chatApp import Ui_Form
from socket import*
s=None
class main1 (QWidget,Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        global s
        s=socket(AF_INET,SOCK_STREAM)
        host="127.0.0.1"
        port=7001
        s.connect((host,port))
        self.send.clicked.connect(self.sendText)
        self.rec.clicked.connect(self.recText)
    def sendText(self):
        y=self.t1.text()
        global s
        s.send(y.encode("utf-8"))
        self.t1.setText('')
    def recText(self):
        global s
        x=s.recv(1024)
        self.l1.setText(x.decode("utf-8"))
           
        

app=QApplication(sys.argv)
window=main1()
window.show()
app.exec_()   
s.close()

