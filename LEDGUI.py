# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPiGUI-LED.ui'
#
# Created by: PyQt5 UI code generator 5.15.9

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        MyWindow.setObjectName("MyWindow")
        MyWindow.resize(555, 270)
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Labels
        self.label_green = QtWidgets.QLabel(self.centralwidget)
        self.label_green.setGeometry(QtCore.QRect(210, 10, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_green.setFont(font)
        self.label_green.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_green.setAlignment(QtCore.Qt.AlignCenter)
        self.label_green.setObjectName("label_green")
        
        self.label_print = QtWidgets.QLabel(self.centralwidget)
        self.label_print.setGeometry(QtCore.QRect(10, 160, 531, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_print.setFont(font)
        self.label_print.setAlignment(QtCore.Qt.AlignCenter)
        self.label_print.setObjectName("label_print")
        
        # Radio Buttons
        self.rad_green = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_green.setGeometry(QtCore.QRect(270, 40, 15, 30))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.rad_green.setFont(font)
        self.rad_green.setText("")
        self.rad_green.setObjectName("rad_green")
        
        self.rad_blue_green = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_blue_green.setGeometry(QtCore.QRect(240, 80, 15, 30))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.rad_blue_green.setFont(font)
        self.rad_blue_green.setText("")
        self.rad_blue_green.setObjectName("rad_blue_green")
        
        self.rad_red = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_red.setGeometry(QtCore.QRect(330, 120, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rad_red.setFont(font)
        self.rad_red.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rad_red.setObjectName("rad_red")
        
        self.rad_blue_red = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_blue_red.setGeometry(QtCore.QRect(270, 120, 15, 30))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.rad_blue_red.setFont(font)
        self.rad_blue_red.setText("")
        self.rad_blue_red.setObjectName("rad_blue_red")
        
        self.rad_red_green = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_red_green.setGeometry(QtCore.QRect(300, 80, 15, 30))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.rad_red_green.setFont(font)
        self.rad_red_green.setText("")
        self.rad_red_green.setObjectName("rad_red_green")
        
        self.rad_blue = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_blue.setGeometry(QtCore.QRect(100, 120, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rad_blue.setFont(font)
        self.rad_blue.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rad_blue.setChecked(False)
        self.rad_blue.setObjectName("rad_blue")
        
        self.rad_none = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_none.setGeometry(QtCore.QRect(10, 50, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rad_none.setFont(font)
        self.rad_none.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rad_none.setChecked(True)
        self.rad_none.setObjectName("rad_none")
        
        self.rad_all = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_all.setGeometry(QtCore.QRect(430, 50, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rad_all.setFont(font)
        self.rad_all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rad_all.setObjectName("rad_all")
        
        # only one LED on
        self.rad_green.clicked.connect(self.greenOnly)
        self.rad_red.clicked.connect(self.redOnly)
        self.rad_blue.clicked.connect(self.blueOnly)
        # two LEDs on
        # red and green
        self.rad_red_green.clicked.connect(self.redGreen)
        # blue and green
        self.rad_blue_green.clicked.connect(self.blueGreen)
        # blue and red
        self.rad_blue_red.clicked.connect(self.blueRed)
        # no LEDs on
        self.rad_none.clicked.connect(self.noneOn)
        # all LEDs on
        self.rad_all.clicked.connect(self.allOn)
        
        MyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 21))
        self.menubar.setObjectName("menubar")
        MyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyWindow)
        self.statusbar.setObjectName("statusbar")
        MyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyWindow)
        QtCore.QMetaObject.connectSlotsByName(MyWindow)

    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "Raspberry Pi 4 LED GUI"))
        # LABELS
        MyWindow.setWindowTitle(_translate("MyWindow", "Raspberry Pi 4 LED GUI"))
        self.label_green.setText(_translate("MyWindow", "Green"))
        self.rad_red.setText(_translate("MyWindow", "Red"))
        self.rad_blue.setText(_translate("MyWindow", "Blue"))
        self.rad_none.setText(_translate("MyWindow", "None"))
        self.rad_all.setText(_translate("MyWindow", "All"))
        self.label_print.setText(_translate("MyWindow", "No LEDs on."))
        
    def greenOnly(self):
        self.label_print.setText("Green LED on.")
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        
    def redOnly(self):
        self.label_print.setText("Red LED on.")
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        
    def blueOnly(self):
        self.label_print.setText("Blue LED on.")
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        
    def redGreen(self):
        self.label_print.setText("Red and Green LEDs on.")
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        
    def blueRed(self):
        self.label_print.setText("Red and Blue LEDs on.")
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        
    def blueGreen(self):
        self.label_print.setText("Blue and Green LEDs on.")
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        
    def noneOn(self):
        self.label_print.setText("No LEDs on.")
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        
    def allOn(self):
        self.label_print.setText("All LEDs on.")
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)


def window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = QtWidgets.QMainWindow()
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT) #blue
    GPIO.setup(13, GPIO.OUT) #red
    GPIO.setup(15, GPIO.OUT) #green
    
    ui = Ui_MyWindow()
    ui.setupUi(MyWindow)
    MyWindow.show()
    sys.exit(app.exec_())

    
    
window()
GPIO.cleanup()

