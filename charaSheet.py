from PyQt5 import QtCore, QtGui, QtWidgets
#from infoSheet import Ui_infoSheet
#from notes import Ui_notes
#from saves import Ui_saves
import init
import math
import random

class Ui_charaSheet(object):
    '''def infoSheet(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_infoSheet()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def notes(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_notes()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def saves(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_saves()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def charaSheet(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_charaSheet()
        self.ui.setupUi(self.window2)
        self.window2.show()'''
    def setupUi(self, charaSheet):
        charaSheet.setObjectName("charaSheet")
        charaSheet.resize(861, 430)
        charaSheet.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.centralwidget = QtWidgets.QWidget(charaSheet)
        self.centralwidget.setObjectName("centralwidget")
        self.raceSelect = QtWidgets.QComboBox(self.centralwidget)
        self.raceSelect.setGeometry(QtCore.QRect(260, 10, 111, 21))
        self.raceSelect.setObjectName("raceSelect")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.raceSelect.addItem("")
        self.classSelect = QtWidgets.QComboBox(self.centralwidget)
        self.classSelect.setGeometry(QtCore.QRect(380, 10, 121, 21))
        self.classSelect.setObjectName("classSelect")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.classSelect.addItem("")
        self.characterName = QtWidgets.QLineEdit(self.centralwidget)
        self.characterName.setGeometry(QtCore.QRect(100, 10, 121, 21))
        self.characterName.setObjectName("characterName")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 81, 371))
        self.groupBox.setObjectName("groupBox")
        self.doNothing = QtWidgets.QPushButton(self.groupBox)
        self.doNothing.setGeometry(QtCore.QRect(10, 10, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.doNothing.setFont(font)
        self.doNothing.setObjectName("doNothing")
        self.toInfo = QtWidgets.QPushButton(self.groupBox)
        self.toInfo.setGeometry(QtCore.QRect(10, 100, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toInfo.setFont(font)
        self.toInfo.setObjectName("toInfo")
        #self.toInfo.clicked.connect(self.infoSheet)
        #self.toInfo.clicked.connect(charaSheet.close)
        self.toNotes = QtWidgets.QPushButton(self.groupBox)
        self.toNotes.setGeometry(QtCore.QRect(10, 190, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toNotes.setFont(font)
        self.toNotes.setObjectName("toNotes")
        #self.toNotes.clicked.connect(self.notes)
        #self.toNotes.clicked.connect(charaSheet.close)
        self.toSaves = QtWidgets.QPushButton(self.groupBox)
        self.toSaves.setGeometry(QtCore.QRect(10, 280, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toSaves.setFont(font)
        self.toSaves.setObjectName("toSaves")
        #self.toSaves.clicked.connect(self.saves)
        #self.toSaves.clicked.connect(charaSheet.close)
        self.rollLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.rollLog.setGeometry(QtCore.QRect(740, 140, 111, 241))
        self.rollLog.setReadOnly(True)
        self.rollLog.setObjectName("rollLog")
        self.selectDice = QtWidgets.QComboBox(self.centralwidget)
        self.selectDice.setGeometry(QtCore.QRect(800, 101, 51, 20))
        self.selectDice.setObjectName("selectDice")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.selectDice.addItem("")
        self.rollButt = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.rollFunc()) 
        self.rollButt.setGeometry(QtCore.QRect(740, 70, 51, 51))
        self.rollButt.setObjectName("rollButt")
        self.rollModi = QtWidgets.QLineEdit(self.centralwidget)
        self.rollModi.setGeometry(QtCore.QRect(800, 70, 51, 21))
        self.rollModi.setObjectName("rollModi")
        self.levelOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.levelOutput.setGeometry(QtCore.QRect(230, 10, 21, 21))
        self.levelOutput.setReadOnly(True)
        self.levelOutput.setObjectName("levelOutput")
        self.strInp = QtWidgets.QLineEdit(self.centralwidget)
        self.strInp.setGeometry(QtCore.QRect(250, 40, 31, 21))
        self.strInp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.strInp.setObjectName("strInp")
        self.dexInp = QtWidgets.QLineEdit(self.centralwidget)
        self.dexInp.setGeometry(QtCore.QRect(330, 40, 31, 21))
        self.dexInp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dexInp.setObjectName("dexInp")
        self.conInp = QtWidgets.QLineEdit(self.centralwidget)
        self.conInp.setGeometry(QtCore.QRect(410, 40, 31, 21))
        self.conInp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.conInp.setObjectName("conInp")
        self.intInp = QtWidgets.QLineEdit(self.centralwidget)
        self.intInp.setGeometry(QtCore.QRect(490, 40, 31, 21))
        self.intInp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.intInp.setObjectName("intInp")
        self.chaInp = QtWidgets.QLineEdit(self.centralwidget)
        self.chaInp.setGeometry(QtCore.QRect(570, 40, 31, 21))
        self.chaInp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.chaInp.setObjectName("chaInp")
        self.wisInp = QtWidgets.QLineEdit(self.centralwidget)
        self.wisInp.setGeometry(QtCore.QRect(650, 40, 31, 21))
        self.wisInp.setObjectName("wisInp")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 40, 101, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 40, 31, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(290, 40, 31, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(370, 40, 31, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(450, 40, 31, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(530, 40, 31, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(610, 40, 31, 20))
        self.lineEdit_15.setAutoFillBackground(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.strR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.strRoll())
        self.strR.setGeometry(QtCore.QRect(100, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.strR.setFont(font)
        self.strR.setObjectName("strR")
        self.dexR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dexRoll())
        self.dexR.setGeometry(QtCore.QRect(180, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dexR.setFont(font)
        self.dexR.setObjectName("dexR")
        self.conR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.conRoll())
        self.conR.setGeometry(QtCore.QRect(260, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.conR.setFont(font)
        self.conR.setObjectName("conR")
        self.intR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.intRoll())
        self.intR.setGeometry(QtCore.QRect(340, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.intR.setFont(font)
        self.intR.setObjectName("intR")
        self.chaR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.chaRoll())
        self.chaR.setGeometry(QtCore.QRect(420, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chaR.setFont(font)
        self.chaR.setObjectName("chaR")
        self.wisR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.wisRoll())
        self.wisR.setGeometry(QtCore.QRect(500, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.wisR.setFont(font)
        self.wisR.setObjectName("wisR")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.strSave = QtWidgets.QPushButton(self.centralwidget)
        self.strSave.setGeometry(QtCore.QRect(90, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.strSave.setFont(font)
        self.strSave.setObjectName("strSave")
        self.dexSave = QtWidgets.QPushButton(self.centralwidget)
        self.dexSave.setGeometry(QtCore.QRect(170, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dexSave.setFont(font)
        self.dexSave.setObjectName("dexSave")
        self.conSave = QtWidgets.QPushButton(self.centralwidget)
        self.conSave.setGeometry(QtCore.QRect(90, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.conSave.setFont(font)
        self.conSave.setObjectName("conSave")
        self.intSave = QtWidgets.QPushButton(self.centralwidget)
        self.intSave.setGeometry(QtCore.QRect(170, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.intSave.setFont(font)
        self.intSave.setObjectName("intSave")
        self.chaSave = QtWidgets.QPushButton(self.centralwidget)
        self.chaSave.setGeometry(QtCore.QRect(90, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chaSave.setFont(font)
        self.chaSave.setObjectName("chaSave")
        self.wisSave = QtWidgets.QPushButton(self.centralwidget)
        self.wisSave.setGeometry(QtCore.QRect(170, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wisSave.setFont(font)
        self.wisSave.setObjectName("wisSave")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 310, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180, 310, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(450, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(260, 190, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(260, 220, 101, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(260, 250, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(260, 280, 71, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(260, 310, 81, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(260, 340, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 190, 61, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(430, 220, 91, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(430, 250, 91, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(430, 280, 71, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(430, 310, 61, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(430, 340, 81, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(590, 220, 81, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(590, 250, 61, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(590, 190, 91, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(590, 280, 101, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(590, 310, 81, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(590, 340, 71, 16))
        self.label_32.setObjectName("label_32")
        self.acroPro = QtWidgets.QCheckBox(self.centralwidget)
        self.acroPro.setGeometry(QtCore.QRect(240, 190, 21, 17))
        self.acroPro.setText("")
        self.acroPro.setObjectName("acroPro")
        self.animPro = QtWidgets.QCheckBox(self.centralwidget)
        self.animPro.setGeometry(QtCore.QRect(240, 220, 21, 17))
        self.animPro.setText("")
        self.animPro.setObjectName("animPro")
        self.arcaPro = QtWidgets.QCheckBox(self.centralwidget)
        self.arcaPro.setGeometry(QtCore.QRect(240, 250, 21, 17))
        self.arcaPro.setText("")
        self.arcaPro.setObjectName("arcaPro")
        self.athlPro = QtWidgets.QCheckBox(self.centralwidget)
        self.athlPro.setGeometry(QtCore.QRect(240, 280, 21, 17))
        self.athlPro.setText("")
        self.athlPro.setObjectName("athlPro")
        self.decePro = QtWidgets.QCheckBox(self.centralwidget)
        self.decePro.setGeometry(QtCore.QRect(240, 310, 21, 17))
        self.decePro.setText("")
        self.decePro.setObjectName("decePro")
        self.histPro = QtWidgets.QCheckBox(self.centralwidget)
        self.histPro.setGeometry(QtCore.QRect(240, 340, 21, 17))
        self.histPro.setText("")
        self.histPro.setObjectName("histPro")
        self.insiPro = QtWidgets.QCheckBox(self.centralwidget)
        self.insiPro.setGeometry(QtCore.QRect(410, 190, 21, 17))
        self.insiPro.setText("")
        self.insiPro.setObjectName("insiPro")
        self.intiPro = QtWidgets.QCheckBox(self.centralwidget)
        self.intiPro.setGeometry(QtCore.QRect(410, 220, 21, 17))
        self.intiPro.setText("")
        self.intiPro.setObjectName("intiPro")
        self.invePro = QtWidgets.QCheckBox(self.centralwidget)
        self.invePro.setGeometry(QtCore.QRect(410, 250, 21, 17))
        self.invePro.setText("")
        self.invePro.setObjectName("invePro")
        self.mediPro = QtWidgets.QCheckBox(self.centralwidget)
        self.mediPro.setGeometry(QtCore.QRect(410, 280, 21, 17))
        self.mediPro.setText("")
        self.mediPro.setObjectName("mediPro")
        self.natuPro = QtWidgets.QCheckBox(self.centralwidget)
        self.natuPro.setGeometry(QtCore.QRect(410, 310, 21, 17))
        self.natuPro.setText("")
        self.natuPro.setObjectName("natuPro")
        self.percPro = QtWidgets.QCheckBox(self.centralwidget)
        self.percPro.setGeometry(QtCore.QRect(410, 340, 21, 17))
        self.percPro.setText("")
        self.percPro.setObjectName("percPro")
        self.perfPro = QtWidgets.QCheckBox(self.centralwidget)
        self.perfPro.setGeometry(QtCore.QRect(570, 190, 21, 17))
        self.perfPro.setText("")
        self.perfPro.setObjectName("perfPro")
        self.persPro = QtWidgets.QCheckBox(self.centralwidget)
        self.persPro.setGeometry(QtCore.QRect(570, 220, 21, 17))
        self.persPro.setText("")
        self.persPro.setObjectName("persPro")
        self.reliPro = QtWidgets.QCheckBox(self.centralwidget)
        self.reliPro.setGeometry(QtCore.QRect(570, 250, 21, 17))
        self.reliPro.setText("")
        self.reliPro.setObjectName("reliPro")
        self.sleiPro = QtWidgets.QCheckBox(self.centralwidget)
        self.sleiPro.setGeometry(QtCore.QRect(570, 280, 21, 17))
        self.sleiPro.setText("")
        self.sleiPro.setObjectName("sleiPro")
        self.steaPro = QtWidgets.QCheckBox(self.centralwidget)
        self.steaPro.setGeometry(QtCore.QRect(570, 310, 21, 17))
        self.steaPro.setText("")
        self.steaPro.setObjectName("steaPro")
        self.survPro = QtWidgets.QCheckBox(self.centralwidget)
        self.survPro.setGeometry(QtCore.QRect(570, 340, 21, 17))
        self.survPro.setText("")
        self.survPro.setObjectName("survPro")
        self.acroR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.acroRoll())
        self.acroR.setGeometry(QtCore.QRect(370, 190, 31, 21))
        self.acroR.setObjectName("acroR")
        self.animR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.animRoll())
        self.animR.setGeometry(QtCore.QRect(370, 220, 31, 21))
        self.animR.setObjectName("animR")
        self.arcaR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.arcaRoll())
        self.arcaR.setGeometry(QtCore.QRect(370, 250, 31, 21))
        self.arcaR.setObjectName("arcaR")
        self.athlR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.athlRoll())
        self.athlR.setGeometry(QtCore.QRect(370, 280, 31, 21))
        self.athlR.setObjectName("athlR")
        self.deceR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.deceRoll())
        self.deceR.setGeometry(QtCore.QRect(370, 310, 31, 21))
        self.deceR.setObjectName("deceR")
        self.histR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.histRoll())
        self.histR.setGeometry(QtCore.QRect(370, 340, 31, 21))
        self.histR.setObjectName("histR")
        self.insiR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.insiRoll())
        self.insiR.setGeometry(QtCore.QRect(530, 190, 31, 21))
        self.insiR.setObjectName("insiR")
        self.intiR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.intiRoll())
        self.intiR.setGeometry(QtCore.QRect(530, 220, 31, 21))
        self.intiR.setObjectName("intiR")
        self.inveR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.inveRoll())
        self.inveR.setGeometry(QtCore.QRect(530, 250, 31, 21))
        self.inveR.setObjectName("inveR")
        self.mediR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.mediRoll())
        self.mediR.setGeometry(QtCore.QRect(530, 280, 31, 21))
        self.mediR.setObjectName("mediR")
        self.natuR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.natuRoll())
        self.natuR.setGeometry(QtCore.QRect(530, 310, 31, 21))
        self.natuR.setObjectName("natuR")
        self.percR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.percRoll())
        self.percR.setGeometry(QtCore.QRect(530, 340, 31, 21))
        self.percR.setObjectName("percR")
        self.perfR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.perfRoll())
        self.perfR.setGeometry(QtCore.QRect(700, 190, 31, 21))
        self.perfR.setObjectName("perfR")
        self.persR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.persRoll())
        self.persR.setGeometry(QtCore.QRect(700, 220, 31, 21))
        self.persR.setObjectName("persR")
        self.reliR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.reliRoll())
        self.reliR.setGeometry(QtCore.QRect(700, 250, 31, 21))
        self.reliR.setObjectName("reliR")
        self.sleiR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.sleiRoll())
        self.sleiR.setGeometry(QtCore.QRect(700, 280, 31, 21))
        self.sleiR.setObjectName("sleiR")
        self.steaR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.steaRoll())
        self.steaR.setGeometry(QtCore.QRect(700, 310, 31, 21))
        self.steaR.setObjectName("steaR")
        self.survR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.survRoll())
        self.survR.setGeometry(QtCore.QRect(700, 340, 31, 21))
        self.survR.setObjectName("survR")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(520, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.hpBox = QtWidgets.QLineEdit(self.centralwidget)
        self.hpBox.setGeometry(QtCore.QRect(550, 10, 31, 20))
        self.hpBox.setReadOnly(True)
        self.hpBox.setObjectName("hpBox")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(590, 10, 41, 20))
        self.lineEdit_17.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.submitHp = QtWidgets.QPushButton(self.centralwidget)
        self.submitHp.setGeometry(QtCore.QRect(640, 10, 61, 23))
        self.submitHp.setObjectName("submitHp")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(710, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.tempHpBox = QtWidgets.QLineEdit(self.centralwidget)
        self.tempHpBox.setGeometry(QtCore.QRect(770, 10, 71, 20))
        self.tempHpBox.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tempHpBox.setObjectName("tempHpBox")
        charaSheet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(charaSheet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        charaSheet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(charaSheet)
        self.statusbar.setObjectName("statusbar")
        charaSheet.setStatusBar(self.statusbar)

        self.retranslateUi(charaSheet)
        QtCore.QMetaObject.connectSlotsByName(charaSheet)

    def retranslateUi(self, charaSheet):
        _translate = QtCore.QCoreApplication.translate
        charaSheet.setWindowTitle(_translate("charaSheet", "Character Sheet"))
        self.raceSelect.setItemText(0, _translate("charaSheet", "--SELECT RACE--"))
        self.raceSelect.setItemText(1, _translate("charaSheet", "Dragonborn"))
        self.raceSelect.setItemText(2, _translate("charaSheet", "Dwarf"))
        self.raceSelect.setItemText(3, _translate("charaSheet", "Elf"))
        self.raceSelect.setItemText(4, _translate("charaSheet", "Gnome"))
        self.raceSelect.setItemText(5, _translate("charaSheet", "Halfling"))
        self.raceSelect.setItemText(6, _translate("charaSheet", "Half-Elf"))
        self.raceSelect.setItemText(7, _translate("charaSheet", "Half-Orc"))
        self.raceSelect.setItemText(8, _translate("charaSheet", "Human"))
        self.raceSelect.setItemText(9, _translate("charaSheet", "Tiefling"))
        self.raceSelect.setItemText(10, _translate("charaSheet", "Aarakocra"))
        self.raceSelect.setItemText(11, _translate("charaSheet", "Aasimar"))
        self.raceSelect.setItemText(12, _translate("charaSheet", "Astral Elf"))
        self.raceSelect.setItemText(13, _translate("charaSheet", "Autognome"))
        self.raceSelect.setItemText(14, _translate("charaSheet", "Bugbear"))
        self.raceSelect.setItemText(15, _translate("charaSheet", "Centaur"))
        self.raceSelect.setItemText(16, _translate("charaSheet", "Changeling"))
        self.raceSelect.setItemText(17, _translate("charaSheet", "Deep Gnome"))
        self.raceSelect.setItemText(18, _translate("charaSheet", "Duergar"))
        self.raceSelect.setItemText(19, _translate("charaSheet", "Eldarin"))
        self.raceSelect.setItemText(20, _translate("charaSheet", "Fairy"))
        self.raceSelect.setItemText(21, _translate("charaSheet", "Firblog"))
        self.raceSelect.setItemText(22, _translate("charaSheet", "Genasi"))
        self.raceSelect.setItemText(23, _translate("charaSheet", "Giff"))
        self.raceSelect.setItemText(24, _translate("charaSheet", "Githyanki"))
        self.raceSelect.setItemText(25, _translate("charaSheet", "Githzerai"))
        self.raceSelect.setItemText(26, _translate("charaSheet", "Goblin"))
        self.raceSelect.setItemText(27, _translate("charaSheet", "Goliath"))
        self.raceSelect.setItemText(28, _translate("charaSheet", "Hadozee"))
        self.raceSelect.setItemText(29, _translate("charaSheet", "Harengon"))
        self.raceSelect.setItemText(30, _translate("charaSheet", "Hobgoblin"))
        self.raceSelect.setItemText(31, _translate("charaSheet", "Kalashtar"))
        self.raceSelect.setItemText(32, _translate("charaSheet", "Kender"))
        self.raceSelect.setItemText(33, _translate("charaSheet", "Kenku"))
        self.raceSelect.setItemText(34, _translate("charaSheet", "Kobold"))
        self.raceSelect.setItemText(35, _translate("charaSheet", "Leonin"))
        self.raceSelect.setItemText(36, _translate("charaSheet", "Lizardfolk"))
        self.raceSelect.setItemText(37, _translate("charaSheet", "Minotaur"))
        self.raceSelect.setItemText(38, _translate("charaSheet", "Orc"))
        self.raceSelect.setItemText(39, _translate("charaSheet", "Owlin"))
        self.raceSelect.setItemText(40, _translate("charaSheet", "Plasmoid"))
        self.raceSelect.setItemText(41, _translate("charaSheet", "Satyr"))
        self.raceSelect.setItemText(42, _translate("charaSheet", "Sea Elf"))
        self.raceSelect.setItemText(43, _translate("charaSheet", "Shadar-kai"))
        self.raceSelect.setItemText(44, _translate("charaSheet", "Shifter"))
        self.raceSelect.setItemText(45, _translate("charaSheet", "Tabaxi"))
        self.raceSelect.setItemText(46, _translate("charaSheet", "Thri-kreen"))
        self.raceSelect.setItemText(47, _translate("charaSheet", "Tortle"))
        self.raceSelect.setItemText(48, _translate("charaSheet", "Triton"))
        self.raceSelect.setItemText(49, _translate("charaSheet", "Warforged"))
        self.raceSelect.setItemText(50, _translate("charaSheet", "Yuan-ti"))
        self.classSelect.setItemText(0, _translate("charaSheet", "--SELECT CLASS--"))
        self.classSelect.setItemText(1, _translate("charaSheet", "Barbarian"))
        self.classSelect.setItemText(2, _translate("charaSheet", "Bard"))
        self.classSelect.setItemText(3, _translate("charaSheet", "Cleric"))
        self.classSelect.setItemText(4, _translate("charaSheet", "Druid"))
        self.classSelect.setItemText(5, _translate("charaSheet", "Fighter"))
        self.classSelect.setItemText(6, _translate("charaSheet", "Monk"))
        self.classSelect.setItemText(7, _translate("charaSheet", "Paladin"))
        self.classSelect.setItemText(8, _translate("charaSheet", "Ranger"))
        self.classSelect.setItemText(9, _translate("charaSheet", "Rogue"))
        self.classSelect.setItemText(10, _translate("charaSheet", "Sorcerer"))
        self.classSelect.setItemText(11, _translate("charaSheet", "Warlock"))
        self.classSelect.setItemText(12, _translate("charaSheet", "Wizard"))
        self.classSelect.setItemText(13, _translate("charaSheet", "Artificer"))
        self.classSelect.setItemText(14, _translate("charaSheet", "Blood Hunter"))
        self.characterName.setText(_translate("charaSheet", "Enter Character Name"))
        self.groupBox.setTitle(_translate("charaSheet", "Buttons"))
        self.doNothing.setText(_translate("charaSheet", "👤"))
        self.toInfo.setText(_translate("charaSheet", "ⓘ"))
        self.toNotes.setText(_translate("charaSheet", "📖"))
        self.toSaves.setText(_translate("charaSheet", "💾"))
        self.selectDice.setItemText(0, _translate("charaSheet", "d4"))
        self.selectDice.setItemText(1, _translate("charaSheet", "d6"))
        self.selectDice.setItemText(2, _translate("charaSheet", "d8"))
        self.selectDice.setItemText(3, _translate("charaSheet", "d10"))
        self.selectDice.setItemText(4, _translate("charaSheet", "d12"))
        self.selectDice.setItemText(5, _translate("charaSheet", "d20"))
        self.selectDice.setItemText(6, _translate("charaSheet", "d50"))
        self.selectDice.setItemText(7, _translate("charaSheet", "d100"))
        self.rollButt.setText(_translate("charaSheet", "Roll"))
        self.rollModi.setText(_translate("charaSheet", "Modifier"))
        self.levelOutput.setText(_translate("charaSheet", "1"))
        self.strInp.setText(_translate("charaSheet", "10"))
        self.dexInp.setText(_translate("charaSheet", "10"))
        self.conInp.setText(_translate("charaSheet", "10"))
        self.intInp.setText(_translate("charaSheet", "10"))
        self.chaInp.setText(_translate("charaSheet", "10"))
        self.wisInp.setText(_translate("charaSheet", "10"))
        self.lineEdit_9.setText(_translate("charaSheet", "Base Scores(0-20) :"))
        self.lineEdit_10.setText(_translate("charaSheet", "STR"))
        self.lineEdit_11.setText(_translate("charaSheet", "DEX"))
        self.lineEdit_12.setText(_translate("charaSheet", "CON"))
        self.lineEdit_13.setText(_translate("charaSheet", "INT"))
        self.lineEdit_14.setText(_translate("charaSheet", "CHA"))
        self.lineEdit_15.setText(_translate("charaSheet", "WIS"))
        self.strR.setText(_translate("charaSheet", "+0"))
        self.dexR.setText(_translate("charaSheet", "+0"))
        self.conR.setText(_translate("charaSheet", "+0"))
        self.intR.setText(_translate("charaSheet", "+0"))
        self.chaR.setText(_translate("charaSheet", "+0"))
        self.wisR.setText(_translate("charaSheet", "+0"))
        self.label.setText(_translate("charaSheet", "    STR"))
        self.label_2.setText(_translate("charaSheet", "    DEX"))
        self.label_3.setText(_translate("charaSheet", "    CON"))
        self.label_4.setText(_translate("charaSheet", "    INT"))
        self.label_5.setText(_translate("charaSheet", "    CHA"))
        self.label_6.setText(_translate("charaSheet", "    WIS"))
        self.label_7.setText(_translate("charaSheet", "Saving Throws"))
        self.strSave.setText(_translate("charaSheet", "+0"))
        self.dexSave.setText(_translate("charaSheet", "+0"))
        self.conSave.setText(_translate("charaSheet", "+0"))
        self.intSave.setText(_translate("charaSheet", "+0"))
        self.chaSave.setText(_translate("charaSheet", "+0"))
        self.wisSave.setText(_translate("charaSheet", "+0"))
        self.label_8.setText(_translate("charaSheet", "STR"))
        self.label_9.setText(_translate("charaSheet", "DEX"))
        self.label_10.setText(_translate("charaSheet", "CON"))
        self.label_11.setText(_translate("charaSheet", "INT"))
        self.label_12.setText(_translate("charaSheet", "CHA"))
        self.label_13.setText(_translate("charaSheet", "WIS"))
        self.label_14.setText(_translate("charaSheet", "Skills"))
        self.label_15.setText(_translate("charaSheet", "Acrobatics[DEX]"))
        self.label_16.setText(_translate("charaSheet", "Animal Handling[WIS]"))
        self.label_17.setText(_translate("charaSheet", "Arcana[INT]"))
        self.label_18.setText(_translate("charaSheet", "Athletics[STR]"))
        self.label_19.setText(_translate("charaSheet", "Deception[CHA]"))
        self.label_20.setText(_translate("charaSheet", "History[INT]"))
        self.label_21.setText(_translate("charaSheet", "Insight[WIS]"))
        self.label_22.setText(_translate("charaSheet", "Intimidation[CHA]"))
        self.label_23.setText(_translate("charaSheet", "Investigation[INT]"))
        self.label_24.setText(_translate("charaSheet", "Medicine[WIS]"))
        self.label_25.setText(_translate("charaSheet", "Nature[INT]"))
        self.label_26.setText(_translate("charaSheet", "Perception[WIS]"))
        self.label_27.setText(_translate("charaSheet", "Persuasion[CHA]"))
        self.label_28.setText(_translate("charaSheet", "Religion[INT]"))
        self.label_29.setText(_translate("charaSheet", "Performance[CHA]"))
        self.label_30.setText(_translate("charaSheet", "Sleight of Hand[DEX]"))
        self.label_31.setText(_translate("charaSheet", "Stealth[DEX]"))
        self.label_32.setText(_translate("charaSheet", "Survival[WIS]"))
        self.acroR.setText(_translate("charaSheet", "+0"))
        self.animR.setText(_translate("charaSheet", "+0"))
        self.arcaR.setText(_translate("charaSheet", "+0"))
        self.athlR.setText(_translate("charaSheet", "+0"))
        self.deceR.setText(_translate("charaSheet", "+0"))
        self.histR.setText(_translate("charaSheet", "+0"))
        self.insiR.setText(_translate("charaSheet", "+0"))
        self.intiR.setText(_translate("charaSheet", "+0"))
        self.inveR.setText(_translate("charaSheet", "+0"))
        self.mediR.setText(_translate("charaSheet", "+0"))
        self.natuR.setText(_translate("charaSheet", "+0"))
        self.percR.setText(_translate("charaSheet", "+0"))
        self.perfR.setText(_translate("charaSheet", "+0"))
        self.persR.setText(_translate("charaSheet", "+0"))
        self.reliR.setText(_translate("charaSheet", "+0"))
        self.sleiR.setText(_translate("charaSheet", "+0"))
        self.steaR.setText(_translate("charaSheet", "+0"))
        self.survR.setText(_translate("charaSheet", "+0"))
        self.label_33.setText(_translate("charaSheet", "HP"))
        self.hpBox.setText(_translate("charaSheet", "0/0"))
        self.submitHp.setText(_translate("charaSheet", "Submit HP"))
        self.label_34.setText(_translate("charaSheet", "Temp HP:"))

    def raceSelection(self):
        if {self.raceSelect.currentText()} == '--SELECT RACE--':
            #base stats
            pass
        elif {self.raceSelect.currentText()} == 'Dragonborn':
            #dragonborn stats
            pass
        elif {self.raceSelect.currentText()} == 'Dwarf':
            #dwarf stats
            pass
        elif {self.raceSelect.currentText()} == 'Elf':
            #elf stats
            pass
        elif {self.raceSelect.currentText()} == 'Gnome':
            #gnome stats
            pass
        elif {self.raceSelect.currentText()} == 'Halfling':
            #halfling stats
            pass
        elif {self.raceSelect.currentText()} == 'Half-Elf':
            #half elf stats
            pass
        elif {self.raceSelect.currentText()} == 'Half-Orc':
            #half orc stats
            pass
        elif {self.raceSelect.currentText()} == 'Human':
            #human stats
            pass
        elif {self.raceSelect.currentText()} == 'Tiefling':
            #Tiefling stats
            pass
    def rollFunc(self):
        if self.rollModi.text() == 'Modifier':
            rollModi = 0
        else:
            rollModi = int(self.rollModi.text())
        if self.selectDice.currentText() == 'd4':
            init.roll=random.randint(1,4)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd6':
            init.roll=random.randint(1,6)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd8':
            init.roll=random.randint(1,8)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd10':
            init.roll=random.randint(1,10)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd12':
            init.roll=random.randint(1,12)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd20':
            init.roll=random.randint(1,20)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd50':
            init.roll=random.randint(1,50)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
        elif self.selectDice.currentText() == 'd100':
            init.roll=random.randint(1,100)
            init.roll=init.roll+rollModi
            self.rollLog.append(f'Roll: {init.roll}')
    
    def strRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.strMod
        self.rollLog.append(f'STR: {init.roll}')
    
    def dexRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod
        self.rollLog.append(f'DEX: {init.roll}')
    
    def conRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.conMod
        self.rollLog.append(f'CON: {init.roll}')
    
    def intRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod
        self.rollLog.append(f'INT: {init.roll}')
    
    def chaRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod
        self.rollLog.append(f'CHA: {init.roll}')
    
    def wisRoll(self):
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        self.rollLog.append(f'WIS: {init.roll}')
    
    def acroRoll(self):
        if self.acroPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod+init.profBonus
            self.rollLog.append(f'Acro: {init.roll}')
        elif self.acroPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod
            self.rollLog.append(f'Acro: {init.roll}')

    def animRoll(self):
        if self.animPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod+init.profBonus
            self.rollLog.append(f'Anim: {init.roll}')
        elif self.animPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod
            self.rollLog.append(f'Anim: {init.roll}')

    def arcaRoll(self):
        if self.arcaPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod+init.profBonus
            self.rollLog.append(f'Arca: {init.roll}')
        elif self.arcaPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod
            self.rollLog.append(f'Arca: {init.roll}')

    def athlRoll(self):
        if self.athlPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.strMod+init.profBonus
            self.rollLog.append(f'Athl: {init.roll}')
        elif self.athlPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.strMod
            self.rollLog.append(f'Athl: {init.roll}')

    def deceRoll(self):
        if self.decePro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod+init.profBonus
            self.rollLog.append(f'Dece: {init.roll}')
        elif self.decePro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod
            self.rollLog.append(f'Dece: {init.roll}')
    def histRoll(self):
        if self.histPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod+init.profBonus
            self.rollLog.append(f'Hist: {init.roll}')
        elif self.histPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod
            self.rollLog.append(f'Hist: {init.roll}')

    def insiRoll(self):
        if self.insiPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod+init.profBonus
            self.rollLog.append(f'Insi: {init.roll}')
        elif self.insiPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod
            self.rollLog.append(f'Insi: {init.roll}')

    def intiRoll(self):
        if self.intiPro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod+init.profBonus
            self.rollLog.append(f'Inti: {init.roll}')
        elif self.intiPro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod
            self.rollLog.append(f'Inti: {init.roll}')

    def inveRoll(self):
        if self.invePro.isChecked() == True:
        #if init.acroProf == 'true':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod+init.profBonus
            self.rollLog.append(f'Inve: {init.roll}')
        elif self.invePro.isChecked() == False:
        #elif init.acroProf == 'false':
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod
            self.rollLog.append(f'Inve: {init.roll}')

    def mediRoll(self):
        if self.mediPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod+init.profBonus
            self.rollLog.append(f'Medi: {init.roll}')
        elif self.mediPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod
            self.rollLog.append(f'Medi: {init.roll}')

    def natuRoll(self):
        if self.natuPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod+init.profBonus
            self.rollLog.append(f'Natu: {init.roll}')
        elif self.natuPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod
            self.rollLog.append(f'Natu: {init.roll}')

    def percRoll(self):
        if self.percPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod+init.profBonus
            self.rollLog.append(f'Perc: {init.roll}')
        elif self.percPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.wisMod
            self.rollLog.append(f'Perc: {init.roll}')

    def perfRoll(self):
        if self.perfPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod+init.profBonus
            self.rollLog.append(f'Perf: {init.roll}')
        elif self.perfPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod
            self.rollLog.append(f'Perf: {init.roll}')

    def persRoll(self):
        if self.persPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod+init.profBonus
            self.rollLog.append(f'Pers: {init.roll}')
        elif self.persPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.chaMod
            self.rollLog.append(f'Pers: {init.roll}')

    def reliRoll(self):
        if self.reliPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod+init.profBonus
            self.rollLog.append(f'Reli: {init.roll}')
        elif self.reliPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.intMod
            self.rollLog.append(f'Reli: {init.roll}')

    def sleiRoll(self):
        if self.sleiPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod+init.profBonus
            self.rollLog.append(f'Slei: {init.roll}')
        elif self.sleiPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod
            self.rollLog.append(f'Slei: {init.roll}')

    def steaRoll(self):
        if self.steaPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod+init.profBonus
            self.rollLog.append(f'Stea: {init.roll}')
        elif self.steaPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod
            self.rollLog.append(f'Stea: {init.roll}')

    def survRoll(self):
        if self.survPro.isChecked() == True:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod+init.profBonus
            self.rollLog.append(f'Surv: {init.roll}')
        elif self.survPro.isChecked() == False:
            init.roll=random.randint(1,20)
            init.roll=init.roll+init.dexMod
            self.rollLog.append(f'Surv: {init.roll}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    charaSheet = QtWidgets.QMainWindow()
    ui = Ui_charaSheet()
    ui.setupUi(charaSheet)
    charaSheet.show()
    sys.exit(app.exec_())