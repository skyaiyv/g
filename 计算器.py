# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python打的代码\QTwindow\计算器\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math as h

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 21, 101, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(101, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 20, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(90, 50, 251, 51))
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 120, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 170, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 170, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 220, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 220, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.lineEdit_2.editingFinished.connect(self.add)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.SetValue)
        self.pushButton_3.clicked.connect(self.jian)
        self.pushButton_4.clicked.connect(self.cheng)
        self.pushButton_5.clicked.connect(self.chu)
        self.pushButton_6.clicked.connect(self.yv)
        self.pushButton_7.clicked.connect(self.cube)
        self.pushButton_8.clicked.connect(self.ping)
        self.pushButton_9.clicked.connect(self.genhao)
        self.pushButton_10.clicked.connect(self.changtoer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算器"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))
        self.label.setText(_translate("MainWindow", "计算结果"))
        self.label_2.setText(_translate("MainWindow", "计算过程"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "/"))
        self.pushButton_6.setText(_translate("MainWindow", "%"))
        self.pushButton_7.setText(_translate("MainWindow", "x^3"))
        self.pushButton_8.setText(_translate("MainWindow", "x^2"))
        self.pushButton_9.setText(_translate("MainWindow", "x^0.5"))
        self.pushButton_10.setText(_translate("MainWindow", "变为n进制"))
        
    def SetValue(self):
        self.lcdNumber.setProperty("value",float(self.lineEdit_2.text())+\
            float(self.lineEdit_4.text()))
    def jian(self):
        self.lcdNumber.setProperty("value",float(self.lineEdit_2.text())- \
            int(self.lineEdit_4.text()))
    def cheng(self):
        self.lcdNumber.setProperty("value",float(self.lineEdit_2.text())*\
            float(self.lineEdit_4.text()))
    def chu(self):
        self.lcdNumber.setProperty("value",float(self.lineEdit_2.text())/\
            float(self.lineEdit_4.text()))
    def yv(self):
        self.lcdNumber.setProperty("value",int(self.lineEdit_2.text())%\
            int(self.lineEdit_4.text()))
    def cube(self):
        self.lcdNumber.setProperty("value",h.pow(float(self.lineEdit_2.text()),3))
    def ping(self):
        self.lcdNumber.setProperty("value",h.pow(float(self.lineEdit_2.text()),2))
    def genhao(self):
        self.lcdNumber.setProperty("value",h.sqrt(float(self.lineEdit_2.text())))
    def changtoer(self):
        a=0
        i=0
        b=int(self.lineEdit_2.text())
        c=int(self.lineEdit_4.text())
        while i<10:
            a=a+int(b%c)*int(h.pow(10,i))
            i=i+1
            b=b/c
        print(a)
        self.lcdNumber.setProperty("value",a)
import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   app.setStyle("Fusion") # 设置窗口风格
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程