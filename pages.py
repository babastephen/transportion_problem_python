# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pages.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(527, 462)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        StackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        StackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        StackedWidget.addWidget(self.page_3)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.pushButton.setText(_translate("StackedWidget", "Next"))
        self.pushButton_2.setText(_translate("StackedWidget", "Next1"))
        self.pushButton_3.setText(_translate("StackedWidget", "next2"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QStackedWidget
    ui = Ui_StackedWidget()
    ui.setupUi(MainWindow)
    app.exec_()