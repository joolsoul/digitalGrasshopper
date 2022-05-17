# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWundowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.level_number = QtWidgets.QSpinBox(self.centralwidget)
        self.level_number.setValue(1)
        self.level_number.setMinimum(1)
        self.level_number.setMaximum(3)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.level_number.sizePolicy().hasHeightForWidth())
        self.level_number.setSizePolicy(sizePolicy)
        self.level_number.setObjectName("spinBox")
        self.gridLayout.addWidget(self.level_number, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.new_game_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_game_Button.sizePolicy().hasHeightForWidth())
        self.new_game_Button.setSizePolicy(sizePolicy)
        self.new_game_Button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.new_game_Button.setStatusTip("")
        self.new_game_Button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.new_game_Button.setObjectName("pushButton")
        self.gridLayout.addWidget(self.new_game_Button, 0, 2, 1, 1)
        self.game_field = QtWidgets.QTableView(self.centralwidget)
        self.game_field.horizontalHeader().setVisible(False)
        self.game_field.horizontalHeader().setCascadingSectionResizes(False)
        self.game_field.horizontalHeader().setDefaultSectionSize(50)
        self.game_field.verticalHeader().setVisible(False)
        self.game_field.verticalHeader().setCascadingSectionResizes(False)
        self.game_field.verticalHeader().setDefaultSectionSize(50)
        self.game_field.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.game_field.horizontalHeader().setMinimumSectionSize(24)
        self.game_field.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_field.sizePolicy().hasHeightForWidth())
        self.game_field.setSizePolicy(sizePolicy)
        self.game_field.setObjectName("tableView")
        self.gridLayout.addWidget(self.game_field, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Digital grasshopper", "Digital grasshopper"))
        self.label.setText(_translate("MainWindow", "Level:"))
        self.new_game_Button.setText(_translate("MainWindow", "New Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())