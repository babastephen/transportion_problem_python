from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtGui import QIntValidator

import trans as ts
import Solution as sn
import numpy as np
from collections import defaultdict

i = 1
j = 1
p = 1
q = 1
a = 0
b = 0
sup_len = 0
Sum_supply = 0
Sum_demand = 0
dem_len = 0
cost = []
sup_array = []
dem_array = []
sup_Values = defaultdict(dict)
Dem_Values = defaultdict(dict)
s = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 700)
        MainWindow.setStyleSheet("background-color: rgb(75, 150, 115)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_p = QtWidgets.QLabel(self.centralwidget)
        self.label_p.setGeometry(QtCore.QRect(100, 30, 141, 40))
        self.label_p.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_p.setObjectName("label_p")
        # self.btn_MaxMin = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.verify_problem())
        # self.btn_MaxMin.setGeometry(QtCore.QRect(220, 640, 121, 41))
        # self.btn_MaxMin.setStyleSheet("background-color: rgb(85, 255, 127);\n"
        #                           "font: 75 12pt \"Candara\";\n"
        #                           "")
        # self.btn_MaxMin.setObjectName("btn_MaxMin")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 30, 161, 41))
        self.comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("Minimization")
        self.comboBox.addItem("Maximization")
        self.txt_rows = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_rows.setValidator(QIntValidator())
        self.txt_rows.setGeometry(QtCore.QRect(370, 100, 121, 41))
        self.txt_rows.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_rows.setMaxLength(5)
        self.txt_rows.setCursorPosition(0)
        self.txt_rows.setObjectName("txt_rows")
        self.btn_rc = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Get_Rows_Columns())
        self.btn_rc.setGeometry(QtCore.QRect(220, 250, 121, 41))
        self.btn_rc.setStyleSheet("background-color: rgb(85, 255, 127);\n""background-color: rgb(0, 170, 0);\n" "font: 75 12pt \"Candara\";")
        self.btn_rc.setObjectName("btn_rc")
        self.txt_columns = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_columns.setValidator(QIntValidator())
        self.txt_columns.setGeometry(QtCore.QRect(370, 180, 121, 41))
        self.txt_columns.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_columns.setMaxLength(5)
        self.txt_columns.setCursorPosition(0)
        self.txt_columns.setObjectName("txt_columns")
        self.txt_cost = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cost.setValidator(QIntValidator())
        self.txt_cost.setGeometry(QtCore.QRect(370, 430, 121, 41))
        self.txt_cost.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_cost.setMaxLength(5)
        self.txt_cost.setCursorPosition(0)
        self.txt_cost.setObjectName("txt_cost")
        self.btn_cost = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Get_Cost_Values())
        self.btn_cost.setGeometry(QtCore.QRect(230, 500, 121, 41))
        self.btn_cost.setStyleSheet("background-color: rgb(85, 255, 127);\n""background-color: rgb(0, 170, 0);\n" "font: 75 12pt \"Candara\";")
        self.btn_cost.setObjectName("btn_cost")
        self.txt_suppl_length = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_suppl_length.setValidator(QIntValidator())
        self.txt_suppl_length.setGeometry(QtCore.QRect(810, 100, 121, 41))
        self.txt_suppl_length.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_suppl_length.setMaxLength(5)
        self.txt_suppl_length.setCursorPosition(0)
        self.txt_suppl_length.setObjectName("txt_suppl_length")
        self.btnsup_De_length = QtWidgets.QPushButton(self.centralwidget,
                                                      clicked=lambda: self.Length_Suplly_Demand())
        self.btnsup_De_length.setGeometry(QtCore.QRect(680, 250, 121, 41))
        self.btnsup_De_length.setStyleSheet("background-color: rgb(85, 255, 127);\n""background-color: rgb(0, 170, 0);\n" "font: 75 12pt \"Candara\";")
        self.btnsup_De_length.setObjectName("btnsup_De_length")
        self.txt_demand_length = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_demand_length.setValidator(QIntValidator())
        self.txt_demand_length.setGeometry(QtCore.QRect(810, 180, 121, 41))
        self.txt_demand_length.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_demand_length.setMaxLength(5)
        self.txt_demand_length.setCursorPosition(0)
        self.txt_demand_length.setObjectName("txt_demand_length")
        self.btndemand_Supply_Values = QtWidgets.QPushButton(self.centralwidget,
                                                             clicked=lambda: self.Supply_Demand_Values())
        self.btndemand_Supply_Values.setGeometry(QtCore.QRect(680, 500, 121, 41))
        self.btndemand_Supply_Values.setStyleSheet("background-color: rgb(85, 255, 127);\n""background-color: rgb(0, 170, 0);\n" "font: 75 12pt \"Candara\";")
        self.btndemand_Supply_Values.setObjectName("btndemand_Supply_Values")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 141, 40))
        self.label.setStyleSheet("color: rgb(0,0,0);\n"
                                 "font: 12pt \"Impact\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 141, 40))
        self.label_2.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 430, 141, 40))
        self.label_3.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_3.setObjectName("label_3")
        self.lb_cost = QtWidgets.QLabel(self.centralwidget)
        self.lb_cost.setGeometry(QtCore.QRect(116, 352, 801, 41))
        self.lb_cost.setStyleSheet("color:rgb(85, 170, 127);\n"
                                   "background-color: rgb(170, 170, 255);\n"
                                   "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 255, 255);")
        self.lb_cost.setText("")
        self.lb_cost.setObjectName("lb_cost")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 100, 141, 40))
        self.label_4.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 180, 141, 40))
        self.label_5.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_5.setObjectName("label_5")
        self.btnfinish = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Output())
        self.btnfinish.setGeometry(QtCore.QRect(420, 620, 121, 41))
        self.btnfinish.setStyleSheet("background-color: rgb(85, 255, 127);\n""background-color: rgb(0, 170, 0);\n" "font: 75 12pt \"Candara\";")
        self.btnfinish.setObjectName("btnfinish")
        self.txt_sup_De_Values = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sup_De_Values.setValidator(QIntValidator())
        self.txt_sup_De_Values.setGeometry(QtCore.QRect(800, 430, 121, 41))
        self.txt_sup_De_Values.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "font: 14pt \"Bahnschrift Condensed\";")
        self.txt_sup_De_Values.setMaxLength(5)
        self.txt_sup_De_Values.setCursorPosition(0)
        self.txt_sup_De_Values.setObjectName("txt_sup_De_Values")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 430, 141, 40))
        self.label_6.setStyleSheet("color: rgb(0,0,0);\n"
                                   "font: 12pt \"Impact\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 70, 994, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_p.setText(_translate("MainWindow", "Type_Transportation"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose..."))
        self.comboBox.setItemText(1, _translate("MainWindow", "Minimization"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Maximization"))
        self.txt_rows.setPlaceholderText(_translate("MainWindow", "0"))
        self.btn_rc.setText(_translate("MainWindow", "Next"))
        # self.btn_MaxMin.setText(_translate("MainWindow", "Next"))
        self.txt_columns.setPlaceholderText(_translate("MainWindow", "0"))
        self.txt_cost.setPlaceholderText(_translate("MainWindow", "0"))
        self.btn_cost.setText(_translate("MainWindow", "Next"))
        self.txt_suppl_length.setPlaceholderText(_translate("MainWindow", "0"))
        self.btnsup_De_length.setText(_translate("MainWindow", "Next"))
        self.txt_demand_length.setPlaceholderText(_translate("MainWindow", "0"))
        self.btndemand_Supply_Values.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "Number Of Rows"))
        self.label_2.setText(_translate("MainWindow", "Number Of Columns"))
        self.label_3.setText(_translate("MainWindow", "Enter cost Values"))
        self.label_4.setText(_translate("MainWindow", "Supply Length"))
        self.label_5.setText(_translate("MainWindow", "Demand Length"))
        self.btnfinish.setText(_translate("MainWindow", "Finish..."))
        self.txt_sup_De_Values.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Supply_Demand Values"))
        self.lb_cost.setText("Enter Cost Value for Row  " + str(i) + " Column " + str(j))

    def Get_Rows_Columns(self):
        global a
        global b
        a = ts.sp_row = int(self.txt_rows.text())
        b = ts.dm_column = int(self.txt_columns.text())
        print(a, b)

    def Get_Cost_Values(self):
        global i
        global j
        global s
        global cost
        ts.userCostInput.costs = cost
        if i <= a:

            costs = int(self.txt_cost.text())
            self.txt_cost.setText("")
            s.append(costs)
            j = j + 1
            if j > b:
                cost.append(s)
                i = i + 1
                j = 1
                s = []

        self.lb_cost.setText("Enter Cost Value for Row  " + str(i) + " Column " + str(j))
        if i > a:
            self.lb_cost.setText("")
            self.comboBox.setEnabled(True)
            self.btn_rc.setEnabled(False)
            self.btnfinish.setEnabled(False)
            self.btndemand_Supply_Values.setEnabled(False)
            self.btnsup_De_length.setEnabled(False)
        if self.comboBox.currentIndex()==2:
            newCost = np.array(cost)
            maxVal = np.max(cost)
            newCost = maxVal - newCost
            cost = newCost.tolist()
            ts.userCostInput.costs = cost
            self.comboBox.setEnabled(False)
            self.btn_rc.setEnabled(True)
            self.btnfinish.setEnabled(True)
            self.btndemand_Supply_Values.setEnabled(True)
            self.btnsup_De_length.setEnabled(True)
            print(cost)
            # print(f'New Cost: {cost}')
            #cost = newCost.cost
        elif self.comboBox.currentIndex()==1:
            self.comboBox.setEnabled(False)
            self.btn_rc.setEnabled(True)
            self.btnfinish.setEnabled(True)
            self.btndemand_Supply_Values.setEnabled(True)
            self.btnsup_De_length.setEnabled(True)

    def Length_Suplly_Demand(self):
        global sup_len
        global dem_len
        sup_len = ts.supply = int(self.txt_suppl_length.text())
        dem_len = ts.demand = int(self.txt_demand_length.text())
        self.lb_cost.setText("Supply Value " + str(p))

    def Supply_Demand_Values(self):
        global p
        global q
        global Sum_demand
        global Sum_supply
        if p <= sup_len:
            sup_Values[p] = int(self.txt_sup_De_Values.text())
            self.txt_sup_De_Values.setText("")
            Sum_supply = Sum_supply + sup_Values[p]
            p = p + 1
            self.lb_cost.setText("Supply Value " + str(p))
            if p > sup_len:
                self.lb_cost.setText("Demand Value " + str(q))
        elif q <= dem_len:
            Dem_Values[q] = int(self.txt_sup_De_Values.text())
            Sum_demand = Sum_demand + Dem_Values[q]
            self.txt_sup_De_Values.setText("")
            q = q + 1
            self.lb_cost.setText("Demand Value " + str(q))
            if q > dem_len:
                self.lb_cost.setText("Click Next again and Finish")
        else:
            ts.total_supply = Sum_supply
            ts.total_demand = Sum_demand
            sup_list = list(sup_Values.values())
            Dem_list = list(Dem_Values.values())
            sup_array = np.array(sup_list)
            dem_array = np.array(Dem_list)
            # sup_copy = sup_array.copy()
            ts.model_supply = sup_array
            ts.model_demand = dem_array
            ts.userSupplyAndDemand.Supply = sup_array
            ts.userSupplyAndDemand.Demand = dem_array
            ts.Outputs()

    def Output(self):

        self.openNow = QtWidgets.QMainWindow()
        self.ui = sn.Ui_Dialog()
        self.ui.setupUi(self.openNow)

        self.openNow.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
