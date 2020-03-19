from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
import sys
from chatApp import Ui_Form
from socket import*
conn =None
class main1 (QWidget,Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        s=socket(AF_INET , SOCK_STREAM)
        host="127.0.0.1"
        port=7001
        s.bind((host ,port))
        s.listen(5)
        global conn
        conn,ad= s.accept()
        print( "connection from" ,ad[0]) 
        self.send.clicked.connect(self.sendText) 
        self.rec.clicked.connect(self.recText)          
    def sendText(self):
        y=self.t1.text()
        global conn
        conn.send(y.encode("utf-8")) 
        self.t1.setText('')  
    def recText(self):
        global conn
        x=conn.recv(1024).decode("utf-8")
        self.l1.setText(x)  

app=QApplication(sys.argv)
window=main1()
window.show()
app.exec_() 
s.close()
