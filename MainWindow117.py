# Form implementation generated from reading ui file 'D:\KTLT_CLASS\chapter6_library\exercise117\ui\MainWindow117.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 373)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label.setObjectName("label")
        self.lineEditInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditInput.setGeometry(QtCore.QRect(10, 40, 441, 20))
        self.lineEditInput.setObjectName("lineEditInput")
        self.pushButtonCalculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(195, 80, 81, 20))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.labelOutput = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(10, 120, 201, 191))
        self.labelOutput.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.labelOutput.setText("")
        self.labelOutput.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.labelOutput.setObjectName("labelOutput")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 120, 231, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter data:"))
        self.lineEditInput.setText(_translate("MainWindow", "45,5,7,86,234,567,86,3"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Statistic"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
