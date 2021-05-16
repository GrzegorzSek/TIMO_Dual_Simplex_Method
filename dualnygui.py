from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import QObject, QVariant

"""
to do:
- włączanie lineEdit
- otrzymywanie inputu
- wypisanie outputu

"""


def bind(objectName, propertyName, type):
    def getter(self):
        return type(self.findChild(QObject, objectName).property(propertyName).toPyObject())

    def setter(self, value):
        self.findChild(QObject, objectName).setProperty(propertyName, QVariant(value))

    return property(getter, setter)


class Ui_MainWindow(object):
    iloscZm = 0
    iloscOgr = 0
    macierz = [0]

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

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(390, 51, 391, 201))
        self.textBrowser.setObjectName("textBrowser")

        self.labelTablice = QtWidgets.QLabel(self.centralwidget)
        self.labelTablice.setGeometry(QtCore.QRect(400, 30, 47, 13))
        self.labelTablice.setObjectName("labelTablice")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 270, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
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
        self.buttonStart.clicked.connect(self.utworzMacierz)

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

        self.labelZmienne.setText(_translate("MainWindow", "Ilość zmiennych"))
        self.labelLiczbaOgr.setText(_translate("MainWindow", "Ilość ograniczeń"))
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

    def ustawZmienne(self, value):
        print("Ilość zmiennych: ", value)
        self.iloscZm = value
        self.textBrowser.append("Ilość zmiennych:" + str(self.iloscZm))
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
        print("Ilość ograniczeń: ", value)
        self.iloscOgr = value
        self.textBrowser.append("Ilość ograniczeń: " + str(self.iloscOgr))
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

    def utworzMacierz(self):
        for i in range(self.iloscZm):
            self.macierz.append(int(self.aktywneZm[i].text()))
        self.textBrowser.append(str(self.macierz))


# start programu
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
