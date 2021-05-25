import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QVariant
import sys
import math
from copy import deepcopy
import numpy as np
from prettytable import PrettyTable
import cgitb
import matplotlib.pyplot as plt

cgitb.enable(format='text')


def bind(objectName, propertyName, type):
    def getter(self):
        return type(self.findChild(QObject, objectName).property(propertyName).toPyObject())

    def setter(self, value):
        self.findChild(QObject, objectName).setProperty(propertyName, QVariant(value))

    return property(getter, setter)


class Ui_MainWindow(object):
    iloscZm = 0
    iloscOgr = 0
    macierz = []

    # zmienne globalne do rysowania
    a_global = np.array([])
    mtp_global = np.array([])
    cols_global = 0
    rows_global = 0
    wsol_global = 0
    asup_global = []
    agoal_global = []
    boundedsol_global = np.array([])
    is_bounded = False
    points = []  # punkty z kolejnych iteracji

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboZmienne = QtWidgets.QComboBox(self.centralwidget)
        self.comboZmienne.setGeometry(QtCore.QRect(10, 40, 41, 22))

        # combo
        self.comboZmienne.setObjectName("comboZmienne")
        self.comboZmienne.addItem("")
        self.comboZmienne.addItem("")
        self.comboZmienne.addItem("")
        self.comboZmienne.addItem("")
        self.comboZmienne.addItem("")
        self.comboZmienne.addItem("")

        self.comboOgr = QtWidgets.QComboBox(self.centralwidget)
        self.comboOgr.setGeometry(QtCore.QRect(10, 100, 41, 22))
        self.comboOgr.setObjectName("comboOgr")
        self.comboOgr.addItem("")
        self.comboOgr.addItem("")
        self.comboOgr.addItem("")
        self.comboOgr.addItem("")
        self.comboOgr.addItem("")
        self.comboOgr.addItem("")

        self.labelZmienne = QtWidgets.QLabel(self.centralwidget)
        self.labelZmienne.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.labelZmienne.setObjectName("labelZmienne")
        self.labelLiczbaOgr = QtWidgets.QLabel(self.centralwidget)
        self.labelLiczbaOgr.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.labelLiczbaOgr.setObjectName("labelLiczbaOgr")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(10, 160, 75, 31))
        self.buttonStart.setObjectName("buttonStart")
        self.labelMin = QtWidgets.QLabel(self.centralwidget)
        self.labelMin.setGeometry(QtCore.QRect(120, 30, 51, 20))
        self.labelMin.setObjectName("labelMin")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 20, 20, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 50, 261, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.labelOgr = QtWidgets.QLabel(self.centralwidget)
        self.labelOgr.setGeometry(QtCore.QRect(110, 70, 71, 16))
        self.labelOgr.setObjectName("labelOgr")

        # Line edit
        # f celu
        self.celuX1 = QtWidgets.QLineEdit(self.centralwidget)
        self.celuX1.setGeometry(QtCore.QRect(170, 30, 21, 20))
        self.celuX1.setObjectName("celuX1")
        self.celuX1.setEnabled(False)

        self.celuX2 = QtWidgets.QLineEdit(self.centralwidget)
        self.celuX2.setGeometry(QtCore.QRect(200, 30, 21, 20))
        self.celuX2.setObjectName("celuX2")
        self.celuX2.setEnabled(False)

        self.celuX3 = QtWidgets.QLineEdit(self.centralwidget)
        self.celuX3.setGeometry(QtCore.QRect(230, 30, 21, 20))
        self.celuX3.setObjectName("celuX3")
        self.celuX3.setEnabled(False)

        self.celuX4 = QtWidgets.QLineEdit(self.centralwidget)
        self.celuX4.setGeometry(QtCore.QRect(260, 30, 21, 20))
        self.celuX4.setObjectName("celuX4")
        self.celuX4.setEnabled(False)

        self.celuX5 = QtWidgets.QLineEdit(self.centralwidget)
        self.celuX5.setGeometry(QtCore.QRect(290, 30, 21, 20))
        self.celuX5.setObjectName("celuX5")
        self.celuX5.setEnabled(False)

        self.aktywneZm = [self.celuX1, self.celuX2, self.celuX3, self.celuX4, self.celuX5]

        # ograniczenia
        self.ogran11 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran11.setGeometry(QtCore.QRect(120, 110, 21, 21))
        self.ogran11.setObjectName("ogran11")
        self.ogran11.setEnabled(False)

        self.ogran12 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran12.setGeometry(QtCore.QRect(150, 110, 21, 20))
        self.ogran12.setObjectName("ogran12")
        self.ogran12.setEnabled(False)

        self.ogran13 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran13.setGeometry(QtCore.QRect(180, 110, 21, 20))
        self.ogran13.setObjectName("ogran13")
        self.ogran13.setEnabled(False)

        self.ogran14 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran14.setGeometry(QtCore.QRect(210, 110, 21, 20))
        self.ogran14.setObjectName("ogran14")
        self.ogran14.setEnabled(False)

        self.ogran15 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran15.setGeometry(QtCore.QRect(240, 110, 21, 20))
        self.ogran15.setObjectName("ogran15")
        self.ogran15.setEnabled(False)

        self.ogran16 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran16.setGeometry(QtCore.QRect(310, 110, 21, 20))
        self.ogran16.setObjectName("ogran16")
        self.ogran16.setEnabled(False)

        self.ogran21 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran21.setGeometry(QtCore.QRect(120, 140, 21, 21))
        self.ogran21.setObjectName("ogran21")
        self.ogran21.setEnabled(False)

        self.ogran22 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran22.setGeometry(QtCore.QRect(150, 140, 21, 20))
        self.ogran22.setObjectName("ogran22")
        self.ogran22.setEnabled(False)

        self.ogran23 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran23.setGeometry(QtCore.QRect(180, 140, 21, 20))
        self.ogran23.setObjectName("ogran23")
        self.ogran23.setEnabled(False)

        self.ogran24 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran24.setGeometry(QtCore.QRect(210, 140, 21, 20))
        self.ogran24.setObjectName("ogran24")
        self.ogran24.setEnabled(False)

        self.ogran25 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran25.setGeometry(QtCore.QRect(240, 140, 21, 20))
        self.ogran25.setObjectName("ogran25")
        self.ogran25.setEnabled(False)

        self.ogran26 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran26.setGeometry(QtCore.QRect(310, 140, 21, 20))
        self.ogran26.setObjectName("ogran26")
        self.ogran26.setEnabled(False)

        self.ogran31 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran31.setGeometry(QtCore.QRect(120, 170, 21, 21))
        self.ogran31.setObjectName("ogran31")
        self.ogran31.setEnabled(False)

        self.ogran32 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran32.setGeometry(QtCore.QRect(150, 170, 21, 20))
        self.ogran32.setObjectName("ogran32")
        self.ogran32.setEnabled(False)

        self.ogran33 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran33.setGeometry(QtCore.QRect(180, 170, 21, 20))
        self.ogran33.setObjectName("ogran33")
        self.ogran33.setEnabled(False)

        self.ogran34 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran34.setGeometry(QtCore.QRect(210, 170, 21, 20))
        self.ogran34.setObjectName("ogran34")
        self.ogran34.setEnabled(False)

        self.ogran35 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran35.setGeometry(QtCore.QRect(240, 170, 21, 20))
        self.ogran35.setObjectName("ogran35")
        self.ogran35.setEnabled(False)

        self.ogran36 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran36.setGeometry(QtCore.QRect(310, 170, 21, 20))
        self.ogran36.setObjectName("ogran36")
        self.ogran36.setEnabled(False)

        self.ogran41 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran41.setGeometry(QtCore.QRect(120, 200, 21, 21))
        self.ogran41.setObjectName("ogran41")
        self.ogran41.setEnabled(False)

        self.ogran42 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran42.setGeometry(QtCore.QRect(150, 200, 21, 20))
        self.ogran42.setObjectName("ogran42")
        self.ogran42.setEnabled(False)

        self.ogran43 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran43.setGeometry(QtCore.QRect(180, 200, 21, 20))
        self.ogran43.setObjectName("ogran43")
        self.ogran43.setEnabled(False)

        self.ogran44 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran44.setGeometry(QtCore.QRect(210, 200, 21, 20))
        self.ogran44.setObjectName("ogran44")
        self.ogran44.setEnabled(False)

        self.ogran45 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran45.setGeometry(QtCore.QRect(240, 200, 21, 20))
        self.ogran45.setObjectName("ogran45")
        self.ogran45.setEnabled(False)

        self.ogran46 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran46.setGeometry(QtCore.QRect(310, 200, 21, 20))
        self.ogran46.setObjectName("ogran46")
        self.ogran46.setEnabled(False)

        self.ogran51 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran51.setGeometry(QtCore.QRect(120, 230, 21, 21))
        self.ogran51.setObjectName("ogran51")
        self.ogran51.setEnabled(False)

        self.ogran52 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran52.setGeometry(QtCore.QRect(150, 230, 21, 20))
        self.ogran52.setObjectName("ogran52")
        self.ogran52.setEnabled(False)

        self.ogran53 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran53.setGeometry(QtCore.QRect(180, 230, 21, 20))
        self.ogran53.setObjectName("ogran53")
        self.ogran53.setEnabled(False)

        self.ogran54 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran54.setGeometry(QtCore.QRect(210, 230, 21, 20))
        self.ogran54.setObjectName("ogran54")
        self.ogran54.setEnabled(False)

        self.ogran55 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran55.setGeometry(QtCore.QRect(240, 230, 21, 20))
        self.ogran55.setObjectName("ogran55")
        self.ogran55.setEnabled(False)

        self.ogran56 = QtWidgets.QLineEdit(self.centralwidget)
        self.ogran56.setGeometry(QtCore.QRect(310, 230, 21, 20))
        self.ogran56.setObjectName("ogran56")
        self.ogran56.setEnabled(False)

        self.aktywneOgr = [[self.ogran11, self.ogran12, self.ogran13, self.ogran14, self.ogran15, self.ogran16],
                           [self.ogran21, self.ogran22, self.ogran23, self.ogran24, self.ogran25, self.ogran26],
                           [self.ogran31, self.ogran32, self.ogran33, self.ogran34, self.ogran35, self.ogran36],
                           [self.ogran41, self.ogran42, self.ogran43, self.ogran44, self.ogran45, self.ogran46],
                           [self.ogran51, self.ogran52, self.ogran53, self.ogran54, self.ogran55, self.ogran56]]

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 90, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 90, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 90, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 90, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 90, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 10, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 10, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 10, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 10, 16, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(290, 10, 16, 16))
        self.label_14.setObjectName("label_14")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(270, 60, 20, 221))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.labelGae = QtWidgets.QLabel(self.centralwidget)
        self.labelGae.setGeometry(QtCore.QRect(290, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelGae.setFont(font)
        self.labelGae.setObjectName("labelGae")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 20, 20, 261))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.buttonDraw = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDraw.setGeometry(QtCore.QRect(10, 212, 75, 31))
        self.buttonDraw.setObjectName("buttonDraw")
        self.buttonDraw.setEnabled(False)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(390, 51, 391, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(QtGui.QFont("Monospace"))

        self.labelTablice = QtWidgets.QLabel(self.centralwidget)
        self.labelTablice.setGeometry(QtCore.QRect(400, 30, 47, 13))
        self.labelTablice.setObjectName("labelTablice")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 270, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(290, 70, 61, 21))
        self.resetButton.setObjectName("resetButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboZmienne.setCurrentIndex(0)
        self.comboOgr.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ustawianie ilości zmiennych i ograniczeń
        self.comboZmienne.currentIndexChanged.connect(lambda: self.ustawZmienne(int(self.comboZmienne.currentIndex())))
        self.comboOgr.currentIndexChanged.connect(lambda: self.ustawOgraniczenia(int(self.comboOgr.currentIndex())))

        # na guzik start
        self.buttonStart.clicked.connect(self.algorytmDualnySimplex)

        # na guzik reset
        self.resetButton.clicked.connect(self.resetOkna)

        # na guzik rysuj
        self.buttonDraw.clicked.connect(self.rysujWykres)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dualny Simplex"))

        self.comboZmienne.setItemText(0, _translate("MainWindow", "0"))
        self.comboZmienne.setItemText(1, _translate("MainWindow", "1"))
        self.comboZmienne.setItemText(2, _translate("MainWindow", "2"))
        self.comboZmienne.setItemText(3, _translate("MainWindow", "3"))
        self.comboZmienne.setItemText(4, _translate("MainWindow", "4"))
        self.comboZmienne.setItemText(5, _translate("MainWindow", "5"))

        self.comboOgr.setItemText(0, _translate("MainWindow", "0"))
        self.comboOgr.setItemText(1, _translate("MainWindow", "1"))
        self.comboOgr.setItemText(2, _translate("MainWindow", "2"))
        self.comboOgr.setItemText(3, _translate("MainWindow", "3"))
        self.comboOgr.setItemText(4, _translate("MainWindow", "4"))
        self.comboOgr.setItemText(5, _translate("MainWindow", "5"))

        self.labelZmienne.setText(_translate("MainWindow", "L. zmiennych"))
        self.labelLiczbaOgr.setText(_translate("MainWindow", "L. ograniczeń"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.labelMin.setText(_translate("MainWindow", "min x0 ="))
        self.labelOgr.setText(_translate("MainWindow", "Ograniczenia"))
        self.label_5.setText(_translate("MainWindow", "x1"))
        self.label_6.setText(_translate("MainWindow", "x2"))
        self.label_7.setText(_translate("MainWindow", "x3"))
        self.label_8.setText(_translate("MainWindow", "x4"))
        self.label_9.setText(_translate("MainWindow", "x5"))
        self.label_10.setText(_translate("MainWindow", "x1"))
        self.label_11.setText(_translate("MainWindow", "x3"))
        self.label_12.setText(_translate("MainWindow", "x2"))
        self.label_13.setText(_translate("MainWindow", "x4"))
        self.label_14.setText(_translate("MainWindow", "x5"))
        self.labelGae.setText(_translate("MainWindow", "≥"))
        self.buttonDraw.setText(_translate("MainWindow", "Rysuj"))
        self.labelTablice.setText(_translate("MainWindow", "Tablice"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))

    def ustawZmienne(self, value):
        # print("Ilość zmiennych: ", value)
        self.iloscZm = value
        # self.textBrowser.append("Ilość zmiennych:" + str(self.iloscZm))
        for i in range(value):
            self.aktywneZm[i].setEnabled(True)

        x = 5 - value
        if x > 0:
            x = x + 1
            for j in range(x):
                y = (-1) * j
                if y == 0:
                    y = -1
                self.aktywneZm[y].setEnabled(False)
            for row in self.aktywneOgr:
                for element in row:
                    element.setEnabled(False)
            self.comboOgr.setCurrentIndex(0)

    def ustawOgraniczenia(self, value):
        # print("Ilość ograniczeń: ", value)
        self.iloscOgr = value
        # self.textBrowser.append("Ilość ograniczeń: " + str(self.iloscOgr))
        for i in range(value):
            self.aktywneOgr[i][5].setEnabled(True)
            for j in range(self.iloscZm):
                self.aktywneOgr[i][j].setEnabled(True)

        x = 5 - value
        if x > 0:
            x = x + 1
            for j in range(x):
                y = (-1) * j
                if y == 0:
                    y = -1
                for element in self.aktywneOgr[y]:
                    element.setEnabled(False)  # self.aktywneZm[y].setEnabled(False)

    def resetOkna(self):
        self.macierz = []
        self.textBrowser.clear()
        self.comboOgr.setCurrentIndex(0)
        self.comboZmienne.setCurrentIndex(0)
        self.iloscZm = 0
        self.iloscOgr = 0
        self.buttonDraw.setEnabled(False)
        self.buttonStart.setEnabled(True)

        self.a_global = np.array([])
        self.mtp_global = np.array([])
        self.cols_global = 0
        self.rows_global = 0
        self.wsol_global = 0
        self.boundedsol_global = np.array([])
        self.asup_global = []
        self.agoal_global = []
        self.is_bounded = False
        self.points = []

        for element in self.aktywneZm:
            element.clear()
            element.setEnabled(False)

        for row in self.aktywneOgr:
            for column in row:
                column.clear()
                column.setEnabled(False)

    def rysujWykres(self):
        if self.is_bounded:
            self.plot_graph(self.a_global, self.mtp_global, self.cols_global, self.rows_global, self.wsol_global,
                            self.boundedsol_global)
        else:
            self.plot_graph(self.a_global, self.mtp_global, self.cols_global, self.rows_global, self.wsol_global,
                            self.asup_global, self.agoal_global)

    def algorytmDualnySimplex(self):

        iloscCelu = int(self.iloscZm)
        iloscOgraniczen = int(self.iloscOgr)
        self.buttonStart.setEnabled(False)

        if self.iloscZm == 2:
            self.buttonDraw.setEnabled(True)

        tempZmienne = [0]
        tempOgraniczenia = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        for i in range(self.iloscZm):
            tempZmienne.append(float(self.aktywneZm[i].text()))
        # tworzenie temp macierzy
        for i in range(iloscOgraniczen):
            for j in range(iloscCelu):
                if self.aktywneOgr[i][j].text():  # jezeli nie jest puste
                    tempOgraniczenia[i][j] = float(self.aktywneOgr[i][j].text())
        for i in range(iloscOgraniczen):
            if self.aktywneOgr[i][5].text():  # jezeli nie jest puste
                tempOgraniczenia[i][5] = float(self.aktywneOgr[i][5].text())

        # wpisywanie elementów do macierzy simplex
        for i in range(iloscOgraniczen):
            self.macierz.append([])

        for i in range(iloscOgraniczen):
            self.macierz[i].append(-1 * tempOgraniczenia[i][-1])

        for i in range(iloscOgraniczen):
            for j in range(iloscCelu):
                self.macierz[i].append(-1 * tempOgraniczenia[i][j])

        self.macierz.insert(0, tempZmienne)

        # print(self.macierz)

        kopiamacierzy = deepcopy(self.macierz)
        a = np.array(kopiamacierzy)
        matrix_to_plot = deepcopy(a)  # kopia surowych danych z interfejsu (potrzebne do plotowania ogr.)
        a_dict = {}
        a_dict2 = {}
        a_dict3 = {}

        a_goal = [0]  # f celu
        for i in range(1, self.iloscZm + 1):
            a_goal.append(i)

        a_support = [0]  # zmienne pomocnicze
        for i in range(self.iloscZm + 1, self.iloscZm + self.iloscOgr + 1):
            a_support.append(i)

        rows = self.iloscOgr + 1
        cols = self.iloscZm + 1
        dim = self.iloscZm

        step_counter = 1  # liczy kroki - kolejne tabele simpleksowe

        bounded_solution = np.zeros((dim, dim))  # tabela do wyniku wielu rozw. na zbiorze ogr.

        is_a = self.is_acceptable(cols, a)

        self.textBrowser.append("Tablica: ")
        b_round = numpy.around(a, 2)
        self.print_solution(b_round, rows, cols, a_goal, a_support)
        self.textBrowser.append(' ')
        self.textBrowser.append('========================================')
        self.textBrowser.append(' ')

        if is_a:
            # print('Rozwiązanie jest dualnie dopuszcalne')
            self.textBrowser.append('Tablica jest dualnie dopuszczalna')
            self.textBrowser.append(' ')
            self.textBrowser.append('========================================')
            self.textBrowser.append(' ')
            is_b = self.is_optimal(rows, a)

            is_empty = False
            while not is_b:
                self.textBrowser.append('KROK: ' + str(step_counter))
                if step_counter == 10:
                    is_empty = True
                    break
                # self.textBrowser.append('Rozwiązanie jest nieoptymalne')
                row_of_variable_removed_from_base = self.variable_to_remove(rows, a)  # wiersz zmiennej do usunięcia
                col_of_variable_added_to_base = self.variable_to_add(cols, a, row_of_variable_removed_from_base)
                a = self.gaussian_elimination(a, row_of_variable_removed_from_base, col_of_variable_added_to_base, rows,
                                              cols)
                self.swap_x(a_goal, a_support, row_of_variable_removed_from_base, col_of_variable_added_to_base)
                # do rysowania punktów
                self.answer_dict(a, a_goal, a_support, a_dict3)
                values = [a_dict3[1], a_dict3[2]]
                self.points.append(values)
                # do rysowania punktów
                is_b = self.is_optimal(rows, a)
                step_counter += 1

                # self.textBrowser.append("Tablica: ")
                # self.textBrowser.append(' ')
                # or element in a:
                #     self.textBrowser.append(str(element))

                # print(a)
                # print('goal:')
                # print(a_goal)
                # print('support')
                # print(a_support)
                e_round = numpy.around(a, 2)
                self.print_solution(e_round, rows, cols, a_goal, a_support)
                self.textBrowser.append(' ')
                self.textBrowser.append('========================================')
                self.textBrowser.append(' ')

                # print("tabele pomocnicze")
                # print("f celu: ")
                # print(a_goal)
                # print("zm pomocnicze: ")
                # print(a_support)
                # print()

                # print("wynik jako dictionary")
                # self.answer_dict(a, a_goal, a_support, a_dict3)
                # print(a_dict3)

                # print("wynik jako wektor")
                # ans3 = []
                # self.answer_array(a_dict3, ans3)
                # print(ans3)
                # print()

            # print(self.points)
            # print("macierz wyników")
            self.textBrowser.append('WYNIK ALGORYTMU: ')
            c_round = numpy.around(a, 2)
            self.print_solution(c_round, rows, cols, a_goal, a_support)
            self.textBrowser.append(' ')
            self.textBrowser.append('========================================')
            self.textBrowser.append(' ')
            # print(a)
            # print()

            # print("tabele pomocnicze")
            # print("f celu: ")
            # print(a_goal)
            # print("zm pomocnicze: ")
            # print(a_support)
            # print()

            # print("wynik jako dictionary")
            self.answer_dict(a, a_goal, a_support, a_dict)
            # print(a_dict)

            # print("wynik jako wektor")
            ans1 = []
            self.answer_array(a_dict, ans1)
            # print(ans1)
            # print()

            if is_empty == False:
                i_s_c = self.inf_solutions_condition(a, cols)
                if i_s_c:  # Zadanie spełnia warunki na nieskończenie wiele rozwiązań
                    on_limited_set = self.is_on_limited_set(a, rows, cols)
                    on_unlimited_set = self.is_on_unlimited_set(a, rows, cols)
                    if on_limited_set != 0:
                        which_solution = 1
                        # print('A_DICT: ')
                        # print(a_dict)
                        bounded_solution[0, 0] = a_dict[1]
                        bounded_solution[0, 1] = a_dict[2]
                        for d in range(1, dim):  # pętla, bo musi przeliczyć tyle razy ile ma wymiar zadania
                            self.textBrowser.append(
                                'Zadanie posiada nieskończenie wiele rozwiązań na zbiorze ograniczonym')
                            self.textBrowser.append(' ')
                            self.textBrowser.append("Dodatkowy krok :" + str(d))
                            self.textBrowser.append(' ')

                            col_no = self.col_to_opt(a, cols)
                            row_no = self.row_to_simplex(a, rows, col_no)
                            a = self.gaussian_elimination(a, row_no, col_no, rows, cols)
                            self.swap_x(a_goal, a_support, row_no, col_no)

                            # print(a)
                            # print("wynik jako dictionary")
                            self.answer_dict(a, a_goal, a_support, a_dict2)
                            # do rysowania punktów
                            values = [a_dict2[1], a_dict2[2]]
                            self.points.append(values)
                            # do rysowania punktów
                            # print(a_dict2)

                            # print("wynik jako wektor")
                            ans2 = []
                            self.answer_array(a_dict2, ans2)
                            # print(ans2)
                            # print()

                            bounded_solution[d, 0] = a_dict2[1]
                            bounded_solution[d, 1] = a_dict2[2]
                            d_round = numpy.around(a, 2)
                            self.print_solution(d_round, rows, cols, a_goal, a_support)
                            self.textBrowser.append(" ")
                            self.textBrowser.append('========================================')
                            self.textBrowser.append(' ')

                        self.print_bounded_solution(bounded_solution)
                        self.textBrowser.append(" ")
                        self.textBrowser.append("min x0 = " + str(-1 * a[0, 0]))
                        # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, bounded_solution)
                        self.a_global = deepcopy(a)
                        self.mtp_global = deepcopy(matrix_to_plot)
                        self.cols_global = deepcopy(cols)
                        self.rows_global = deepcopy(rows)
                        self.wsol_global = deepcopy(which_solution)
                        self.boundedsol_global = deepcopy(bounded_solution)
                        self.is_bounded = True

                    elif on_unlimited_set != 0:
                        which_solution = 2
                        # print('Zadanie posiada wiele rozwiązań na zbiorze nieograniczonym')
                        self.print_unbounded_solution(a, a_support, a_goal)
                        # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, a_support, a_goal)
                        self.a_global = deepcopy(a)
                        self.mtp_global = deepcopy(matrix_to_plot)
                        self.cols_global = deepcopy(cols)
                        self.rows_global = deepcopy(rows)
                        self.wsol_global = deepcopy(which_solution)
                        self.boundedsol_global = deepcopy(bounded_solution)
                        self.asup_global = deepcopy(a_support)
                        self.agoal_global = deepcopy(a_goal)
                        self.is_bounded = False
                    else:
                        self.textBrowser.append('Zadanie posiada tylko jedno rozwiązanie')
                        self.textBrowser.append("min x0 = " + str(-1 * a[0, 0]))
                        which_solution = 3
                        # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, a_support, a_goal)
                        self.a_global = deepcopy(a)
                        self.mtp_global = deepcopy(matrix_to_plot)
                        self.cols_global = deepcopy(cols)
                        self.rows_global = deepcopy(rows)
                        self.wsol_global = deepcopy(which_solution)
                        self.boundedsol_global = deepcopy(bounded_solution)
                        self.asup_global = deepcopy(a_support)
                        self.agoal_global = deepcopy(a_goal)
                        self.is_bounded = False
                else:
                    unlimited_task = self.is_on_unlimited_task(a, rows, cols)
                    if unlimited_task:
                        self.textBrowser.append('Zadanie nieograniczone - brak rozwiązań')
                        which_solution = 4
                        # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, a_support, a_goal)
                        self.a_global = deepcopy(a)
                        self.mtp_global = deepcopy(matrix_to_plot)
                        self.cols_global = deepcopy(cols)
                        self.rows_global = deepcopy(rows)
                        self.wsol_global = deepcopy(which_solution)
                        self.boundedsol_global = deepcopy(bounded_solution)
                        self.asup_global = deepcopy(a_support)
                        self.agoal_global = deepcopy(a_goal)
                        self.is_bounded = False
                    else:
                        self.textBrowser.append('Zadanie posiada tylko jedno rozwiązanie')
                        self.textBrowser.append("min x0 = " + str(-1 * a[0, 0]))
                        which_solution = 3
                        # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, a_support, a_goal)
                        self.a_global = deepcopy(a)
                        self.mtp_global = deepcopy(matrix_to_plot)
                        self.cols_global = deepcopy(cols)
                        self.rows_global = deepcopy(rows)
                        self.wsol_global = deepcopy(which_solution)
                        self.boundedsol_global = deepcopy(bounded_solution)
                        self.asup_global = deepcopy(a_support)
                        self.agoal_global = deepcopy(a_goal)
                        self.is_bounded = False
            else:
                self.textBrowser.append('Brak rozwiązań!')
                which_solution = 4
                # self.plot_graph(a, matrix_to_plot, cols, rows, which_solution, a_support, a_goal)
                self.a_global = deepcopy(a)
                self.mtp_global = deepcopy(matrix_to_plot)
                self.cols_global = deepcopy(cols)
                self.rows_global = deepcopy(rows)
                self.wsol_global = deepcopy(which_solution)
                self.boundedsol_global = deepcopy(bounded_solution)
                self.asup_global = deepcopy(a_support)
                self.agoal_global = deepcopy(a_goal)
                self.is_bounded = False
        else:
            self.textBrowser.append('tablica nie jest dualnie dopuszczalna. Skorzystaj z innego algorytmu')
            self.buttonDraw.setEnabled(False)

    def plot_graph(self, a, matrix_to_plot, cols, rows, which_solution, *args):

        x = np.arange(-100, 100, 0.1)
        # plt.ylim(-5, 10)
        # plt.xlim(-5, 10)

        if which_solution == 1:  # wiele na ograniczonym
            for p in range(0, len(self.points)):
                if p >= len(self.points) - 2:
                    plt.plot(self.points[p][0], self.points[p][1], 'ro')
                else:
                    plt.plot(self.points[p][0], self.points[p][1], 'bo')
            for ar in args:  # bounded_solution
                b_s = ar  # b_s jako bounded solution

            # ograniczenia zakresu wykresu
            plt.xlim(self.points[-1][0] - 5, self.points[-1][0] + 5)
            plt.ylim(self.points[-1][1] - 5, self.points[-1][1] + 5)

            for i in range(1, rows):  # rysowanie ograniczen
                if matrix_to_plot[i, 2] == 0:
                    if -matrix_to_plot[i, 1] < 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                    if -matrix_to_plot[i, 1] > 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)

                else:
                    y = -1 * (matrix_to_plot[i, 1] * x + (-matrix_to_plot[i, 0])) / matrix_to_plot[i, 2]
                    plt.plot(x, y)
                    if -matrix_to_plot[i, 2] > 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, 100, 10000, alpha=0.2)
                        else:
                            plt.fill_between(x, y, 10000, alpha=0.2)
                    elif -matrix_to_plot[i, 2] < 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, y, -100, alpha=0.2)
                        else:
                            plt.fill_between(x, y, -10000, alpha=0.2)

            plt.plot([b_s[0][0], b_s[1][0]], [b_s[0][1], b_s[1][1]], 'k-')  # rysowanie odcinka

            if matrix_to_plot[0, 2] != 0:
                y = (-matrix_to_plot[0, 1] * x + (-a[0, 0])) / matrix_to_plot[0, 2]  # rysowanie funkcji celu
                plt.plot(x, y, 'k-')
            else:
                a2 = -x
                x[:] = -a[0, 0] / matrix_to_plot[0, 1]
                plt.plot(x, a2)
            # y = (-matrix_to_plot[0, 1] * x + (-a[0, 0])) / matrix_to_plot[0, 2]     # rysowanie funkcji celu
        elif which_solution == 2:  # wiele na nieogr
            for p in range(0, len(self.points)):
                if p < len(self.points) - 1:
                    plt.plot(self.points[p][0], self.points[p][1], 'bo')
            support = args[0]
            goal = args[1]
            # print(support)
            # print(goal)
            x_1 = 0  # współrzędne x1 i x2
            x_2 = 0
            for j in range(0, cols):  # pobranie wartości x1, x2 (jesli jest) z kolumny
                if goal[j] == 1:
                    x_1 = a[0, j]
                if goal[j] == 2:
                    x_2 = a[0, j]

            for i in range(2, rows + 1):  # pobranie wartości x1, x2 (jesli jest) z wiersza
                if support[i] == 1:
                    x_1 = a[i - 1, 0]
                if support[i] == 2:
                    x_2 = a[i - 1, 0]

            plt.plot(x_1, x_2, 'ro')  # rysowanie punktu półprostej

            # ograniczenia zakresu wykresu
            plt.ylim(x_2-5, x_2+5)
            plt.xlim(x_1-5, x_1+5)

            for i in range(1, rows):  # rysowanie ograniczen
                if matrix_to_plot[i, 2] == 0:
                    if -matrix_to_plot[i, 1] < 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                    if -matrix_to_plot[i, 1] > 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)

                else:
                    y = -1 * (matrix_to_plot[i, 1] * x + (-matrix_to_plot[i, 0])) / matrix_to_plot[i, 2]
                    plt.plot(x, y)
                    if -matrix_to_plot[i, 2] > 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, 100, 10000, alpha=0.2)
                        else:
                            plt.fill_between(x, y, 10000, alpha=0.2)
                    elif -matrix_to_plot[i, 2] < 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, y, -100, alpha=0.2)
                        else:
                            plt.fill_between(x, y, -10000, alpha=0.2)

            if matrix_to_plot[0, 2] != 0:
                y = (-matrix_to_plot[0, 1] * x + (-a[0, 0])) / matrix_to_plot[0, 2]  # rysowanie funkcji celu
                plt.plot(x, y, 'k-')
            else:
                a2 = -x
                x[:] = -a[0, 0] / matrix_to_plot[0, 1]
                plt.plot(x, a2)
            # y = (-matrix_to_plot[0, 1] * x + (-a[0, 0])) / matrix_to_plot[0, 2]     # rysowanie funkcji celu
        elif which_solution == 4:  # zadanie nieograniczone / brak rozwiązań
            for p in range(0, len(self.points)):
                plt.plot(self.points[p][0], self.points[p][1], 'bo')

            # ograniczenia zakresu wykresu
            plt.xlim(self.points[-1][0]-5, self.points[-1][0]+5)
            plt.ylim(self.points[-1][1]-5, self.points[-1][1]+5)

            for i in range(1, rows):  # rysowanie ograniczen
                if matrix_to_plot[i, 2] == 0:
                    if -matrix_to_plot[i, 1] < 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                    if -matrix_to_plot[i, 1] > 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)

                else:
                    y = -1 * (matrix_to_plot[i, 1] * x + (-matrix_to_plot[i, 0])) / matrix_to_plot[i, 2]
                    plt.plot(x, y)
                    if -matrix_to_plot[i, 2] > 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, 100, 10000, alpha=0.2)
                        else:
                            plt.fill_between(x, y, 10000, alpha=0.2)
                    elif -matrix_to_plot[i, 2] < 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, y, -100, alpha=0.2)
                        else:
                            plt.fill_between(x, y, -10000, alpha=0.2)

            if matrix_to_plot[0, 2] != 0:
                y = (-matrix_to_plot[0, 1] * x + (-3)) / matrix_to_plot[0, 2]  # rysowanie funkcji celu
                plt.plot(x, y, 'k-')
            else:
                a2 = -x
                x[:] = -a[0, 0] / matrix_to_plot[0, 1]
                plt.plot(x, a2)

            # y = (-matrix_to_plot[0, 1] * x + (-3)) / matrix_to_plot[0, 2]     # rysowanie funkcji celu
        elif which_solution == 3:  # jedno rozwiązanie
            support = args[0]
            goal = args[1]
            # print(support)
            # print(goal)
            x_1 = 0  # współrzędne x1 i x2
            x_2 = 0
            for j in range(0, cols):  # pobranie wartości x1, x2 (jesli jest) z kolumny
                if goal[j] == 1:
                    x_1 = a[0, j]
                if goal[j] == 2:
                    x_2 = a[0, j]

            for i in range(1, rows):  # pobranie wartości x1, x2 (jesli jest) z wiersza
                if support[i] == 1:
                    x_1 = a[i, 0]
                if support[i] == 2:
                    x_2 = a[i, 0]
            # print('x1:', x_1)
            # print('x1:', x_2)
            plt.plot(x_1, x_2, 'ro')  # rysowanie punktu rozwiązania

            # ograniczenia zakresu wykresu
            plt.ylim(x_2 - 5, x_2 + 5)
            plt.xlim(x_1 - 5, x_1 + 5)

            for i in range(1, rows):  # rysowanie ograniczen
                if matrix_to_plot[i, 2] == 0:
                    if -matrix_to_plot[i, 1] < 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.plot(x_values, a1)

                            b = -(-matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1]))
                            plt.axvspan(b, -100, alpha=0.5)
                    if -matrix_to_plot[i, 1] > 0:
                        if -matrix_to_plot[i, 0] < 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)
                        if -matrix_to_plot[i, 0] > 0:
                            x_values = np.arange(-100, 100, 0.1)
                            a1 = -x
                            x_values[:] = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.plot(x_values, a1)

                            b = -matrix_to_plot[i, 0] / (-matrix_to_plot[i, 1])
                            plt.axvspan(b, 100, alpha=0.5)

                else:
                    y = -1 * (matrix_to_plot[i, 1] * x + (-matrix_to_plot[i, 0])) / matrix_to_plot[i, 2]
                    plt.plot(x, y)
                    if -matrix_to_plot[i, 2] > 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, 100, 10000, alpha=0.2)
                        else:
                            plt.fill_between(x, y, 10000, alpha=0.2)
                    elif -matrix_to_plot[i, 2] < 0:
                        if matrix_to_plot[i, 1] == 0:
                            plt.fill_between(x, y, -100, alpha=0.2)
                        else:
                            plt.fill_between(x, y, -10000, alpha=0.2)

            if matrix_to_plot[0, 2] != 0:
                y = (-matrix_to_plot[0, 1] * x + (-a[0, 0])) / matrix_to_plot[0, 2]  # rysowanie funkcji celu
                plt.plot(x, y, 'k-')
            else:
                a2 = -x
                x[:] = -a[0, 0] / matrix_to_plot[0, 1]
                plt.plot(x, a2)
        plt.grid(linestyle='--', linewidth=0.5)
        plt.show()

    def print_unbounded_solution(self, a, a_support, a_goal):
        b = deepcopy(a)
        a_support.insert(0, 0)
        b = np.row_stack([a_goal, b])
        b = np.column_stack([a_support, b])

        rows = b.shape[0]
        cols = b.shape[1]
        col = 0
        solution = []
        for j in range(2, cols):
            if b[1, j] == 0:
                col = j
                break

        for i in range(1, cols):  # pętla po x1, x2, ...
            for w in range(2, rows):  # pętla po wierszach
                if i == b[w, 0]:
                    # print(b[w, col])
                    solution.append(b[w, col])
                    break

        self.textBrowser.append('Rozwiązanie: ')
        self.textBrowser.append('x + ' + str(solution) + 't')

    def print_solution(self, a, rows, cols, a_goal, a_support):
        s = PrettyTable(['X', str(a_goal)])

        for i in range(0, rows):
            s.add_row([str(a_support[i]), a[i]])
        self.textBrowser.append(str(s))

    def inf_solutions_condition(self, a, cols):  # sprawdza czy zadanie spełnia warunki na nieskończenie wiele rozwiązań
        for j in range(1, cols):  # jest to warunek y_0 j >= 0
            if a[0, j] < 0:
                return False
        # self.textBrowser.append('Zadanie może mieć nieskonczenie wiele rozwiazan')
        return True

    def print_bounded_solution(self, bounded_solution):
        dim = bounded_solution.shape[0]
        # print('Rozwiązanie zdania dla nieskończenie wielu rozwiązań na zbiorze ograniczonym: ')
        lambdy_str = ""
        for d in range(0, dim):
            if d < dim - 1:
                # print(bounded_solution[d], end="")
                # print('*\u03BB' + str(d + 1) + ' + ', end="")
                self.textBrowser.append(str(bounded_solution[d]) + '*\u03BB' + str(d + 1) + ' + ')
            else:
                # print(bounded_solution[d], end="")
                # print('*\u03BB' + str(d + 1))
                self.textBrowser.append(str(bounded_solution[d]) + '*\u03BB' + str(d + 1))

        for d in range(0, dim):
            if d < dim - 1:
                lambdy_str += '\u03BB' + str(d+1) + " + "
            else:
                lambdy_str += '\u03BB' + str(d+1)

        lambdy_str += " = 1"
        self.textBrowser.append("")
        self.textBrowser.append(lambdy_str)
        self.textBrowser.append("")

    def is_on_limited_set(self, a, rows,
                          cols):  # sprawdza czy zadanie posiada nieskończenie wiele rozwiązań na zb. ogr.
        col = 0
        # print('sprawdzamy ograniczone zadanie')
        # print(a)
        for j in range(1, cols):  # sprawdza czy w pierwszym wierszu występuje zero - warunek: y_0 j_0 = 0
            if a[0, j] == 0:
                col = j
                # self.textBrowser.append('Jest 0 w pierwszym wierszu, w kolumnie ' + str(col))

        if col == 0:
            # self.textBrowser.append('nie ma 0 w pierwszym wierszu')
            return col

        for i in range(1, rows):  # sprawdza kolejne dwa warunki y_i_0 0 > 0 oraz y_i_0 j_0 >0
            if a[i, 0] > 0:
                # self.textBrowser.append('a[' + str(i) + ', 0] > 0')
                if a[i, col] > 0:
                    # self.textBrowser.append('a[' + str(i) + ', ' + str(col) + '] > 0')
                    return col

        return 0

    def is_on_unlimited_set(self, a, rows, cols):  # spradza czy zadanie ma wiele rozw. na zb. nieogr.
        row = 0  # zmienna licząca wiersze z degeneracją
        col = 0
        for j in range(1, cols):  # sprawdza czy w wierszu występuje zero - warunek: y_0 j_0 = 0
            if a[0, j] == 0:
                col = j
            else:
                return col

        for i in range(1, rows):  # sprawdza czy w zadaniu występuje degeneracja - warunek y_i0 = 0 dla i=1, ..., m
            if a[i, 0] == 0:
                row = row + 1

        if row == rows - 1:
            self.textBrowser.append('Zachodzi degeneracja')
            return col

        for i in range(1, rows):  # sprawdza warunek: y_i j_0 <= 0 dla i=1, ..., m
            if a[i, col] > 0:
                return 0

        return col

    def is_on_unlimited_task(self, a, rows, cols):  # sprawdza czy zadanie jest nieograniczone
        for j in range(0, cols):
            if a[0, j] < 0:
                for i in range(1, rows):
                    if a[i, j] > 0:
                        return False
        return True

    def answer_dict(self, a, a_goal, a_support, a_dict):
        for j in range(1, len(a_goal)):
            a_dict[a_goal[j]] = a[0, j]

        for i in range(1, len(a_support)):
            a_dict[a_support[i]] = a[i, 0]

    def answer_array(self, a_dict, ans):
        for i in range(1, len(a_dict) + 1):
            ans.append(a_dict.get(i))

    def swap_x(self, goal, support, row, col):
        temp = goal[col]
        goal[col] = support[row]
        support[row] = temp

    def is_acceptable(self, cols, a):  # test dualnej dopuszczalności zaczyna się od wiersza zerowego
        for j in range(cols):
            if a[0, j] < 0:
                return False
        return True

    def is_optimal(self, rows, a):  # test optymalności zaczyna się od wiersza 1 nie od zerowego
        for i in range(1, rows):
            if a[i, 0] < 0:
                return False
        self.textBrowser.append(' ')
        self.textBrowser.append('Rozwiązanie optymalne')
        self.textBrowser.append(' ')
        return True

    def col_to_opt(self, a, cols):  # bierzemy kolumnę, dla której w pierwszym wierszu jest zero
        for j in range(1, cols):
            if a[0, j] == 0:
                return j

    def row_to_simplex(self, a, rows, col):  # szukamy jakie zmienne musimy ze sobą zamienić dla wielu rozw.
        x = 0
        x_i = 0
        row_output = 0

        for i in range(1, rows):
            if a[i, 0] / a[i, col] >= 0:
                x = a[i, 0] / a[i, col]
                row_output = i
                x_i = i + 1

        if x_i <= rows:
            for j in range(x_i, rows):
                if a[j, 0] / a[j, col] >= 0:
                    y = a[j, 0] / a[j, col]
                    if y < x:
                        x = a[j, 0] / a[j, col]
                        row_output = j

        return row_output

    def variable_to_remove(self, rows, a):  # usuwamy wiersz, który min < 0
        row = 1
        x = 0
        new_starting_point = 0
        for i in range(1, rows):  # bierze pierwszy element z 0 kolumny < 0
            if a[i, 0] < 0:
                x = a[i, 0]
                new_starting_point += 1
                row = new_starting_point
                break
            else:
                new_starting_point += 1

        for i in range(new_starting_point, rows - 1):
            if a[i + 1, 0] < 0 and a[i + 1, 0] < x:
                x = a[i + 1, 0]
                row = i + 1

        # print('Usuwamy wiersz: ' + str(row))
        # print(x)
        return row

    def variable_to_add(self, cols, a, row):
        new_starting_point = 0
        x = 0
        col = 1
        temp = 0

        for j in range(1, cols):  # tutaj bierze pierwszą napotkaną wartość y_0j/y_rj < 0
            if a[row, j] < 0:
                x = a[0, 1] / a[row, j]
                temp = a[row, j]
                new_starting_point += 1
                # print('Nowy punkt startowy to: ')
                # print(new_starting_point)
                col = new_starting_point
                break
            else:
                new_starting_point += 1

        for j in range(new_starting_point, cols - 1):
            if a[row, j + 1] < 0 and a[0, j + 1] / a[row, j + 1] > x:
                temp = a[row, j + 1]
                x = a[0, j] / a[row, j + 1]
                col = j + 1
        # print('Dodajemy kolumnę: ' + str(col))
        # print(temp)
        return col

    def gaussian_elimination(self, a, row, col, rows, cols):
        b = deepcopy(a)
        for i in range(0, rows):  # wiersze
            for j in range(0, cols):  # kolumny
                if i == row and j == col:
                    # print('1 /', b[i][j], '=')
                    a[i, j] = 1 / b[i, j]
                    # print(a[i][j])
                    # print(a)
                elif i == row and j != col:
                    # print(b[row][j], ' / ', b[row][col], '=')
                    a[i, j] = b[row, j] / b[row, col]
                    # print(a[i][j])
                    # print(a)
                elif i != row and j == col:
                    # print('-', b[i][col], ' / ', b[row][col], ' = ', a[i][j], '=')
                    a[i, j] = -b[i, col] / b[row, col]
                    # print(a[i][j])
                    # print(a)
                else:
                    # print(b)
                    # print(b[i][j], '- (', b[i][col], '*', b[row][j], '/', b[row][col], ') = ')
                    a[i, j] = b[i, j] - b[i, col] * b[row, j] / b[row, col]
                    # print(a[i][j])
                    # print(a)
        # print('print b: ', b)
        return a


# start programu
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
