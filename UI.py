# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1159, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_SerialPorts = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_SerialPorts.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.comboBox_SerialPorts.setObjectName("comboBox_SerialPorts")
        self.pushButton_UpdatePorts = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UpdatePorts.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton_UpdatePorts.setObjectName("pushButton_UpdatePorts")
        self.comboBox_Baudrate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Baudrate.setGeometry(QtCore.QRect(20, 110, 69, 22))
        self.comboBox_Baudrate.setObjectName("comboBox_Baudrate")
        self.comboBox_Baudrate.addItem("")
        self.comboBox_Baudrate.addItem("")
        self.comboBox_Baudrate.addItem("")
        self.comboBox_Baudrate.addItem("")
        self.pushButton_StartProgram = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StartProgram.setGeometry(QtCore.QRect(20, 160, 75, 23))
        self.pushButton_StartProgram.setObjectName("pushButton_StartProgram")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(30, 90, 51, 16))
        self.label_41.setObjectName("label_41")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(10, 230, 91, 16))
        self.label_35.setObjectName("label_35")
        self.doubleSpinBox_UpdateTime = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_UpdateTime.setGeometry(QtCore.QRect(20, 250, 62, 22))
        self.doubleSpinBox_UpdateTime.setDecimals(3)
        self.doubleSpinBox_UpdateTime.setProperty("value", 0.01)
        self.doubleSpinBox_UpdateTime.setObjectName("doubleSpinBox_UpdateTime")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 0, 1061, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graphicsView_2 = PlotWidget(self.tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(70, 300, 481, 241))
        self.graphicsView_2.setAutoFillBackground(True)
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView_2.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView = PlotWidget(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(70, 20, 481, 241))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 41, 16))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 350, 41, 16))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 400, 41, 16))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(270, 0, 51, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(270, 280, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.label_5.setObjectName("label_5")
        self.graphicsView_3 = PlotWidget(self.tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(560, 20, 481, 241))
        self.graphicsView_3.setAutoFillBackground(True)
        self.graphicsView_3.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView_3.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setForegroundBrush(brush)
        self.graphicsView_3.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = PlotWidget(self.tab)
        self.graphicsView_4.setGeometry(QtCore.QRect(560, 300, 481, 241))
        self.graphicsView_4.setAutoFillBackground(True)
        self.graphicsView_4.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView_4.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_4.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_4.setForegroundBrush(brush)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(740, 0, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(780, 280, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 330, 41, 16))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 51, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 430, 41, 16))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 400, 71, 41))
        self.label_11.setObjectName("label_11")
        self.tabWidget.raise_()
        self.comboBox_SerialPorts.raise_()
        self.pushButton_UpdatePorts.raise_()
        self.comboBox_Baudrate.raise_()
        self.pushButton_StartProgram.raise_()
        self.label_2.raise_()
        self.label_41.raise_()
        self.label_35.raise_()
        self.doubleSpinBox_UpdateTime.raise_()
        self.lineEdit_5.raise_()
        self.label_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_UpdatePorts.setText(_translate("MainWindow", "Update Ports"))
        self.comboBox_Baudrate.setItemText(0, _translate("MainWindow", "250000"))
        self.comboBox_Baudrate.setItemText(1, _translate("MainWindow", "115200"))
        self.comboBox_Baudrate.setItemText(2, _translate("MainWindow", "345600"))
        self.comboBox_Baudrate.setItemText(3, _translate("MainWindow", "9600"))
        self.pushButton_StartProgram.setText(_translate("MainWindow", "Start Program"))
        self.label_2.setText(_translate("MainWindow", "Serial Port"))
        self.label_41.setText(_translate("MainWindow", "Baud Rate"))
        self.label_35.setText(_translate("MainWindow", "Update Time [s]"))
        self.label.setText(_translate("MainWindow", "Tensão (V)"))
        self.label_3.setText(_translate("MainWindow", "Corrente (A)"))
        self.label_4.setText(_translate("MainWindow", "Pico (V)"))
        self.label_5.setText(_translate("MainWindow", "RMS (V)"))
        self.label_8.setText(_translate("MainWindow", "Potencia instantanea (W)"))
        self.label_9.setText(_translate("MainWindow", "Energia (J)"))
        self.label_10.setText(_translate("MainWindow", "Pico (V)"))
        self.label_6.setText(_translate("MainWindow", "RMS (V)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_11.setText(_translate("MainWindow", "S. Frequency"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
