from PyQt6.QtWidgets import QTableWidgetItem
from django.db.models.expressions import result


import numpy as np

from chapter6_library.exercise117.ui.MainWindow117 import Ui_MainWindow


class MainWindow117Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.process_statistic)
    def process_statistic(self):
        s=self.lineEditInput.text()
        arr_int=[int(i) for i in s.split(',')]
        arr_np=np.asarray(arr_int)
        min_label=f"MIN={np.min(arr_np)}"
        argmin_label=f"argmin={np.argmin(arr_np)}"
        max_label=f"argmax={np.max(arr_np)}"
        argmax_label=f"argmax={np.argmax(arr_np)}"
        mean_label=f"mean={np.mean(arr_np)}"
        median_label=f"median={np.median(arr_np)}"
        std_label=f"std={np.std(arr_np)}"
        result=min_label+"\n"+argmin_label+"\n"+\
               max_label+"\n"+argmax_label+"\n"+\
               mean_label+"\n"+median_label+"\n"+std_label
        self.labelOutput.setText(result)
        self.tableWidget.setRowCount(0)
        self.insert_row_statistic("MIN",np.min(arr_np))
        self.insert_row_statistic("argmin", np.argmin(arr_np))
        self.insert_row_statistic("argmax", np.argmax(arr_np))
        self.insert_row_statistic("median", np.median(arr_np))
        self.insert_row_statistic("std", np.std(arr_np))
    def insert_row_statistic(self,term_title,value):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(term_title))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(value)))


