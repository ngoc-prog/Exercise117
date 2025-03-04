from PyQt6.QtWidgets import QApplication, QMainWindow

from chapter6_library.exercise117.ui.MainWindow117Ext import MainWindow117Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow117Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()