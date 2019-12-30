from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QLineEdit, \
    QComboBox, QMenuBar, QMenu, QAction
import sys
from classifier import *
import webbrowser


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("DDOS Detector")
        self.resize(800, 600)
        self.Componnent()
        self.show()

    def Componnent(self):

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 561, 32))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.btnBrowse = QPushButton(self)
        self.btnBrowse.setGeometry(QtCore.QRect(680, 30, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setObjectName("btnBrowse")

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(100, 80, 271, 32))
        self.comboBox.setObjectName("comboBox")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 140, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.image = QLabel(self)
        self.image.setGeometry(QtCore.QRect(300, 200, 256, 256))
        self.image.setObjectName("image")

        self.btnReport = QPushButton(self)
        self.btnReport.setGeometry(QtCore.QRect(310, 510, 171, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnReport.setFont(font)
        self.btnReport.setObjectName("btnReport")

        self.btnCalculation = QPushButton(self)
        self.btnCalculation.setGeometry(QtCore.QRect(510, 510, 231, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCalculation.setFont(font)
        self.btnCalculation.setObjectName("btnCalculation")

        self.btnScan = QPushButton(self)
        self.btnScan.setGeometry(QtCore.QRect(390, 80, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnScan.setFont(font)
        self.btnScan.setObjectName("btnScan")

        self.result = QLabel(self)
        self.result.setGeometry(QtCore.QRect(330, 140, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setObjectName("result")

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUsage = QAction(self)
        self.actionUsage.setObjectName("actionUsage")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUsage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.label.setText("Filename")
        self.label_2.setText("Server IP")
        self.btnBrowse.setText("Browse")
        self.label_3.setText("Scan Result")
        self.image.setText("")
        self.btnReport.setText("View Scan Report")
        self.btnCalculation.setText("View Calculation Report")
        self.btnScan.setText("SCAN")
        self.btnScan.setDisabled(True)
        self.result.setText("Load file first")
        self.menuFile.setTitle("File")
        self.menuHelp.setTitle("Help")
        self.actionOpen.setText("Open")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionExit.setText("Exit")
        self.actionExit.setShortcut("Alt+F4")
        self.actionAbout.setText("About")
        self.actionAbout.setShortcut("Ctrl+A")
        self.actionUsage.setText("Usage")
        self.actionUsage.setShortcut("Ctrl+U")
        self.comboBox.setDisabled(True)

        self.btnBrowse.clicked.connect(self.openFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExit.triggered.connect(self.closeApp)
        self.btnScan.clicked.connect(self.scan)
        self.btnReport.clicked.connect(self.view_scan_report)
        self.btnCalculation.clicked.connect(self.view_calc_report)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "CSV Files (*.csv)")
        if fname != ('', ''):
            self.filePath = fname[0]
            self.lineEdit.setText(self.filePath)
            self.df = load_csv(self.filePath)
            self.result.setText("Set Server IP then SCAN")
            self.comboBox.setDisabled(False)
            self.btnScan.setDisabled(False)
            self.fetchServer()

    def fetchServer(self):
        server = self.df.Destination.unique()
        self.comboBox.clear()
        self.comboBox.addItems(server)
        self.selectionchange(0)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self, i):
        self.server_ip = self.comboBox.currentText()

    def scan(self):
        self.df = filter_server(self.df, self.server_ip)
        check = QPixmap('res/check.png')
        cross = QPixmap('res/cross.png')
        report_dict, keanggotaan_length, keanggotaan_source, keanggotaan_packet, rule_dict, Z, Z_class, klasifikasi = calculate(
            self.df)
        if klasifikasi == 'POD':
            self.image.setPixmap(cross)
            self.result.setText("DDOS PING OF DEATH DETECTED!!!")
        else:
            self.image.setPixmap(check)
            self.result.setText("DDOS PING OF DEATH NOT DETECTED!!!")
        generate_report(report_dict, self.filePath, self.server_ip, klasifikasi)
        generate_calculation(report_dict, keanggotaan_length, keanggotaan_source, keanggotaan_packet, rule_dict,
                             self.filePath,
                             self.server_ip, klasifikasi)

    def view_scan_report(self):
        path = self.filePath.split('/')[-1]
        output = path.split('.')[0] + '-scan.html'
        output_path = self.filePath.strip(path) + output
        webbrowser.open(output_path, new=2)

    def view_calc_report(self):
        path = self.filePath.split('/')[-1]
        output = path.split('.')[0] + '-calculation.html'
        output_path = self.filePath.strip(path) + output
        webbrowser.open(output_path, new=2)

    def closeApp(self):
        sys.exit()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
