# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(789, 431)
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(App)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(App)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOpen_file = QtWidgets.QAction(App)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionExit = QtWidgets.QAction(App)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "App"))
        self.label.setText(_translate("App", "PATH"))
        self.menuFile.setTitle(_translate("App", "File"))
        self.menuHelp.setTitle(_translate("App", "Help"))
        self.actionAbout.setText(_translate("App", "About"))
        self.actionHelp.setText(_translate("App", "Help"))
        self.actionOpen_file.setText(_translate("App", "Open file"))
        self.actionOpen_file.setStatusTip(_translate("App", "Open csv file from your disk"))
        self.actionOpen_file.setShortcut(_translate("App", "Ctrl+O"))
        self.actionExit.setText(_translate("App", "Exit"))
