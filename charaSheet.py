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
        self.raceSelect.setGeometry(QtCore.QRect(260, 10, 140, 21))
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
        self.classSelect.setGeometry(QtCore.QRect(410, 10, 140, 21))
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
        self.rollLog.setGeometry(QtCore.QRect(800, 140, 130, 241))
        self.rollLog.setReadOnly(True)
        self.rollLog.setObjectName("rollLog")
        self.selectDice = QtWidgets.QComboBox(self.centralwidget)
        self.selectDice.setGeometry(QtCore.QRect(860, 101, 70, 20))
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
        self.rollButt.setGeometry(QtCore.QRect(800, 70, 51, 51))
        self.rollButt.setObjectName("rollButt")
        self.rollModi = QtWidgets.QLineEdit(self.centralwidget)
        self.rollModi.setGeometry(QtCore.QRect(860, 70, 70, 21))
        self.rollModi.setObjectName("rollModi")
        self.levelOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.levelOutput.setGeometry(QtCore.QRect(230, 10, 25, 21))
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
        self.setInp = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.setInput()) 
        self.setInp.setGeometry(QtCore.QRect(690, 40, 80, 21))
        self.setInp.setObjectName("setInp")
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
        font.setPointSize(18)
        self.strR.setFont(font)
        self.strR.setObjectName("strR")
        self.dexR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dexRoll())
        self.dexR.setGeometry(QtCore.QRect(180, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dexR.setFont(font)
        self.dexR.setObjectName("dexR")
        self.conR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.conRoll())
        self.conR.setGeometry(QtCore.QRect(260, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.conR.setFont(font)
        self.conR.setObjectName("conR")
        self.intR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.intRoll())
        self.intR.setGeometry(QtCore.QRect(340, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.intR.setFont(font)
        self.intR.setObjectName("intR")
        self.chaR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.chaRoll())
        self.chaR.setGeometry(QtCore.QRect(420, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chaR.setFont(font)
        self.chaR.setObjectName("chaR")
        self.wisR = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.wisRoll())
        self.wisR.setGeometry(QtCore.QRect(500, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
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
        self.label_7.setGeometry(QtCore.QRect(95, 150, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.strSave = QtWidgets.QPushButton(self.centralwidget)
        self.strSave.setGeometry(QtCore.QRect(90, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.strSave.setFont(font)
        self.strSave.setObjectName("strSave")
        self.dexSave = QtWidgets.QPushButton(self.centralwidget)
        self.dexSave.setGeometry(QtCore.QRect(170, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dexSave.setFont(font)
        self.dexSave.setObjectName("dexSave")
        self.conSave = QtWidgets.QPushButton(self.centralwidget)
        self.conSave.setGeometry(QtCore.QRect(90, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conSave.setFont(font)
        self.conSave.setObjectName("conSave")
        self.intSave = QtWidgets.QPushButton(self.centralwidget)
        self.intSave.setGeometry(QtCore.QRect(170, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.intSave.setFont(font)
        self.intSave.setObjectName("intSave")
        self.chaSave = QtWidgets.QPushButton(self.centralwidget)
        self.chaSave.setGeometry(QtCore.QRect(90, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chaSave.setFont(font)
        self.chaSave.setObjectName("chaSave")
        self.wisSave = QtWidgets.QPushButton(self.centralwidget)
        self.wisSave.setGeometry(QtCore.QRect(170, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wisSave.setFont(font)
        self.wisSave.setObjectName("wisSave")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(95, 170, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(175, 170, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(95, 240, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(175, 240, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(95, 310, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(175, 310, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(450, 150, 50, 31))
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
        self.acroPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.acroPro.setGeometry(QtCore.QRect(240, 190, 21, 17))
        self.acroPro.setText("")
        self.acroPro.setObjectName("acroPro")
        self.animPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.animPro.setGeometry(QtCore.QRect(240, 220, 21, 17))
        self.animPro.setText("")
        self.animPro.setObjectName("animPro")
        self.arcaPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.arcaPro.setGeometry(QtCore.QRect(240, 250, 21, 17))
        self.arcaPro.setText("")
        self.arcaPro.setObjectName("arcaPro")
        self.athlPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.athlPro.setGeometry(QtCore.QRect(240, 280, 21, 17))
        self.athlPro.setText("")
        self.athlPro.setObjectName("athlPro")
        self.decePro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.decePro.setGeometry(QtCore.QRect(240, 310, 21, 17))
        self.decePro.setText("")
        self.decePro.setObjectName("decePro")
        self.histPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.histPro.setGeometry(QtCore.QRect(240, 340, 21, 17))
        self.histPro.setText("")
        self.histPro.setObjectName("histPro")
        self.insiPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.insiPro.setGeometry(QtCore.QRect(410, 190, 21, 17))
        self.insiPro.setText("")
        self.insiPro.setObjectName("insiPro")
        self.intiPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.intiPro.setGeometry(QtCore.QRect(410, 220, 21, 17))
        self.intiPro.setText("")
        self.intiPro.setObjectName("intiPro")
        self.invePro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.invePro.setGeometry(QtCore.QRect(410, 250, 21, 17))
        self.invePro.setText("")
        self.invePro.setObjectName("invePro")
        self.mediPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.mediPro.setGeometry(QtCore.QRect(410, 280, 21, 17))
        self.mediPro.setText("")
        self.mediPro.setObjectName("mediPro")
        self.natuPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.natuPro.setGeometry(QtCore.QRect(410, 310, 21, 17))
        self.natuPro.setText("")
        self.natuPro.setObjectName("natuPro")
        self.percPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.percPro.setGeometry(QtCore.QRect(410, 340, 21, 17))
        self.percPro.setText("")
        self.percPro.setObjectName("percPro")
        self.perfPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.perfPro.setGeometry(QtCore.QRect(570, 190, 21, 17))
        self.perfPro.setText("")
        self.perfPro.setObjectName("perfPro")
        self.persPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.persPro.setGeometry(QtCore.QRect(570, 220, 21, 17))
        self.persPro.setText("")
        self.persPro.setObjectName("persPro")
        self.reliPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.reliPro.setGeometry(QtCore.QRect(570, 250, 21, 17))
        self.reliPro.setText("")
        self.reliPro.setObjectName("reliPro")
        self.sleiPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.sleiPro.setGeometry(QtCore.QRect(570, 280, 21, 17))
        self.sleiPro.setText("")
        self.sleiPro.setObjectName("sleiPro")
        self.steaPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
        self.steaPro.setGeometry(QtCore.QRect(570, 310, 21, 17))
        self.steaPro.setText("")
        self.steaPro.setObjectName("steaPro")
        self.survPro = QtWidgets.QCheckBox(self.centralwidget, clicked= lambda: self.setInput())
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
        self.label_33.setGeometry(QtCore.QRect(560, 10, 50, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.hpBox = QtWidgets.QLineEdit(self.centralwidget)
        self.hpBox.setGeometry(QtCore.QRect(590, 10, 50, 20))
        self.hpBox.setReadOnly(True)
        self.hpBox.setObjectName("hpBox")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(650, 10, 50, 20))
        self.lineEdit_17.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.submitHp = QtWidgets.QPushButton(self.centralwidget)
        self.submitHp.setGeometry(QtCore.QRect(710, 10, 85, 23))
        self.submitHp.setObjectName("submitHp")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(800, 10, 90, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.tempHpBox = QtWidgets.QLineEdit(self.centralwidget)
        self.tempHpBox.setGeometry(QtCore.QRect(890, 10, 80, 20))
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
        self.raceSelect.setItemText(0, _translate("charaSheet", "SELECT RACE"))
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
        self.classSelect.setItemText(0, _translate("charaSheet", "SELECT CLASS"))
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
        self.groupBox.setTitle(_translate("charaSheet", " "))
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
        self.setInp.setText(_translate("charaSheet", "Set Input"))
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
        self.label.setText(_translate("charaSheet", " STR"))
        self.label_2.setText(_translate("charaSheet", "DEX"))
        self.label_3.setText(_translate("charaSheet", "CON"))
        self.label_4.setText(_translate("charaSheet", "INT"))
        self.label_5.setText(_translate("charaSheet", "CHA"))
        self.label_6.setText(_translate("charaSheet", "WIS"))
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
        
    def setInput(self):
        init.inputStr = int(self.strInp.text())
        if init.inputStr > 20:
            init.inputStr = 20
            self.strInp.setText('20')
        if init.inputStr < 1:
            init.inputStr = 1
            self.strInp.setText('1')
        init.stre = init.inputStr+init.raceStrMod
        if init.stre > 20:
            init.stre=20
        if init.stre < 1:
            init.stre=1
        init.inputDex=int(self.dexInp.text())
        if init.inputDex > 20:
            init.inputDex = 20
            self.dexInp.setText('20')
        if init.inputDex < 1:
            init.inputDex = 1
            self.dexInp.setText('1')
        init.dex=init.inputDex+init.raceDexMod
        if init.dex > 20:
            init.dex=20
        if init.dex < 1:
            init.dex=1
        init.inputCon=int(self.conInp.text())
        if init.inputCon > 20:
            init.inputCon = 20
            self.conInp.setText('20')
        if init.inputCon < 1:
            init.inputCon = 1
            self.conInp.setText('1')
        init.con=init.inputCon+init.raceConMod
        if init.con > 20:
            init.con=20
        if init.con < 1:
            init.con=1
        init.inputInt=int(self.intInp.text())
        if init.inputInt > 20:
            init.inputInt = 20
            self.intInp.setText('20')
        if init.inputInt < 1:
            init.inputInt = 1
            self.intInp.setText('1')
        init.intel=init.inputInt+init.raceIntMod
        if init.intel > 20:
            init.intel=20
        if init.intel < 1:
            init.intel=1
        init.inputWis=int(self.wisInp.text())
        if init.inputWis > 20:
            init.inputWis = 20
            self.wisInp.setText('20')
        if init.inputWis < 1:
            init.inputWis = 1
            self.wisInp.setText('1')
        init.wis=init.inputWis+init.raceWisMod
        if init.wis > 20:
            init.wis=20
        if init.wis < 1:
            init.wis=1
        init.inputCha=int(self.chaInp.text())
        if init.inputCha > 20:
            init.inputCha = 20
            self.chaInp.setText('20')
        if init.inputCha < 1:
            init.inputCha = 1
            self.chaInp.setText('1')
        init.cha=init.inputCha+init.raceChaMod
        if init.cha > 20:
            init.cha=20
        if init.cha < 1:
            init.cha=1
        if init.stre == 1:
            self.strR.setText('-5')
            if self.athlPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.athlR.setText(f'+{text}')
                else:
                    self.athlR.setText(f'{text}')
            if self.athlPro.isChecked() == False:
                self.athlR.setText('-5')
            init.strMod = -5
        elif init.stre >1 and init.stre < 4:
            self.strR.setText('-4')
            if self.athlPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.athlR.setText(f'+{text}')
                else:
                    self.athlR.setText(f'{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('-4')
            init.strMod = -4
        elif init.stre > 3 and init.stre < 6:
            self.strR.setText('-3')
            if self.athlPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.athlR.setText(f'+{text}')
                else:
                    self.athlR.setText(f'{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('-3')
            init.strMod = -3
        elif init.stre > 5 and init.stre < 8:
            self.strR.setText('-2')
            if self.athlPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.athlR.setText(f'+{text}')
                else:
                    self.athlR.setText(f'{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('-2')
            init.strMod = -2
        elif init.stre > 7 and init.stre < 10:
            self.strR.setText('-1')
            if self.athlPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.athlR.setText(f'+{text}')
                else:
                    self.athlR.setText(f'{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('-1')
            init.strMod = -1
        elif init.stre > 9 and init.stre < 12:
            self.strR.setText('+0')
            if self.athlPro.isChecked() == True:
                text=0+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+0')
            init.strMod = 0
        elif init.stre > 11 and init.stre < 14:
            self.strR.setText('+1')
            if self.athlPro.isChecked() == True:
                text=1+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+1')
            init.strMod = 1
        elif init.stre > 13 and init.stre < 16:
            self.strR.setText('+2')
            if self.athlPro.isChecked() == True:
                text=2+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+2')
            init.strMod = 2
        elif init.stre > 15 and init.stre < 18:
            self.strR.setText('+3')
            if self.athlPro.isChecked() == True:
                text=3+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+3')
            init.strMod = 3
        elif init.stre > 17 and init.stre < 20:
            self.strR.setText('+4')
            if self.athlPro.isChecked() == True:
                text=4+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+4')
            init.strMod = 4
        elif init.stre == 20:
            self.strR.setText('+5')
            if self.athlPro.isChecked() == True:
                text=5+init.profBonus
                self.athlR.setText(f'+{text}')
            elif self.athlPro.isChecked() == False:
                self.athlR.setText('+5')
            init.strMod = 5
        if init.dex == 1:
            self.dexR.setText('-5')
            if self.acroPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.acroR.setText(f'+{text}')
                else:
                    self.acroR.setText(f'{text}')
            if self.acroPro.isChecked() == False:
                self.acroR.setText('-5')
            if self.sleiPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.sleiR.setText(f'+{text}')
                else:
                    self.sleiR.setText(f'{text}')
            if self.sleiPro.isChecked() == False:
                self.sleiR.setText('-5')
            if self.steaPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.steaR.setText(f'+{text}')
                else:
                    self.steaR.setText(f'{text}')
            if self.steaPro.isChecked() == False:
                self.steaR.setText('-5')
            init.dexMod = -5
        elif init.dex >1 and init.dex < 4:
            self.dexR.setText('-4')
            if self.acroPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.acroR.setText(f'+{text}')
                else:
                    self.acroR.setText(f'{text}')
            if self.acroPro.isChecked() == False:
                self.acroR.setText('-4')
            if self.sleiPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.sleiR.setText(f'+{text}')
                else:
                    self.sleiR.setText(f'{text}')
            if self.sleiPro.isChecked() == False:
                self.sleiR.setText('-4')
            if self.steaPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.steaR.setText(f'+{text}')
                else:
                    self.steaR.setText(f'{text}')
            if self.steaPro.isChecked() == False:
                self.steaR.setText('-4')
            init.dexMod = -4
        elif init.dex > 3 and init.dex < 6:
            self.dexR.setText('-3')
            if self.acroPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.acroR.setText(f'+{text}')
                else:
                    self.acroR.setText(f'{text}')
            if self.acroPro.isChecked() == False:
                self.acroR.setText('-3')
            if self.sleiPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.sleiR.setText(f'+{text}')
                else:
                    self.sleiR.setText(f'{text}')
            if self.sleiPro.isChecked() == False:
                self.sleiR.setText('-3')
            if self.steaPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.steaR.setText(f'+{text}')
                else:
                    self.steaR.setText(f'{text}')
            if self.steaPro.isChecked() == False:
                self.steaR.setText('-3')
            init.dexMod = -3
        elif init.dex > 5 and init.dex < 8:
            self.dexR.setText('-2')
            if self.acroPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.acroR.setText(f'+{text}')
                else:
                    self.acroR.setText(f'{text}')
            if self.acroPro.isChecked() == False:
                self.acroR.setText('-2')
            if self.sleiPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.sleiR.setText(f'+{text}')
                else:
                    self.sleiR.setText(f'{text}')
            if self.sleiPro.isChecked() == False:
                self.sleiR.setText('-2')
            if self.steaPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.steaR.setText(f'+{text}')
                else:
                    self.steaR.setText(f'{text}')
            if self.steaPro.isChecked() == False:
                self.steaR.setText('-2')
            elif self.athlPro.isChecked == False:
                self.athlR.setText('-2')
            init.dexMod = -2
        elif init.dex > 7 and init.dex < 10:
            self.dexR.setText('-1')
            if self.acroPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.acroR.setText(f'+{text}')
                else:
                    self.acroR.setText(f'{text}')
            if self.acroPro.isChecked() == False:
                self.acroR.setText('-1')
            if self.sleiPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.sleiR.setText(f'+{text}')
                else:
                    self.sleiR.setText(f'{text}')
            if self.sleiPro.isChecked() == False:
                self.sleiR.setText('-1')
            if self.steaPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.steaR.setText(f'+{text}')
                else:
                    self.steaR.setText(f'{text}')
            if self.steaPro.isChecked() == False:
                self.steaR.setText('-1')
            init.dexMod = -1
        elif init.dex > 9 and init.dex < 12:
            self.dexR.setText('+0')
            if self.acroPro.isChecked() == True:
                text=0+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+0')
            if self.sleiPro.isChecked() == True:
                text=0+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked() == False:
                self.sleiR.setText('+0')
            if self.steaPro.isChecked() == True:
                text=0+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+0')
            init.dexMod = 0
        elif init.dex > 11 and init.dex < 14:
            self.dexR.setText('+1')
            if self.acroPro.isChecked() == True:
                text=1+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+1')
            if self.sleiPro.isChecked() == True:
                text=1+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked() == False:
                self.sleiR.setText('+1')
            if self.steaPro.isChecked() == True:
                text=1+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+1')
            init.dexMod = 1
        elif init.dex > 13 and init.dex < 16:
            self.dexR.setText('+2')
            if self.acroPro.isChecked() == True:
                text=2+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+2')
            if self.sleiPro.isChecked() == True:
                text=2+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked == False:
                self.sleiR.setText('+2')
            if self.steaPro.isChecked() == True:
                text=2+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+2')
            init.dexMod = 2
        elif init.dex > 15 and init.dex < 18:
            self.dexR.setText('+3')
            if self.acroPro.isChecked() == True:
                text=3+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+3')
            if self.sleiPro.isChecked() == True:
                text=3+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked() == False:
                self.sleiR.setText('+3')
            if self.steaPro.isChecked() == True:
                text=3+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+3')
            init.dexMod = 3
        elif init.dex > 17 and init.dex < 20:
            self.dexR.setText('+4')
            if self.acroPro.isChecked() == True:
                text=4+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+4')
            if self.sleiPro.isChecked() == True:
                text=4+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked() == False:
                self.sleiR.setText('+4')
            if self.steaPro.isChecked() == True:
                text=4+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+4')
            init.dexMod = 4
        elif init.dex == 20:
            self.dexR.setText('+5')
            if self.acroPro.isChecked() == True:
                text=5+init.profBonus
                self.acroR.setText(f'+{text}')
            elif self.acroPro.isChecked() == False:
                self.acroR.setText('+5')
            if self.sleiPro.isChecked() == True:
                text=5+init.profBonus
                self.sleiR.setText(f'+{text}')
            elif self.sleiPro.isChecked() == False:
                self.sleiR.setText('+5')
            if self.steaPro.isChecked() == True:
                text=5+init.profBonus
                self.steaR.setText(f'+{text}')
            elif self.steaPro.isChecked() == False:
                self.steaR.setText('+5')
            init.dexMod = 5
        if init.con == 1:
            self.conR.setText('-5')
            init.conMod = -5
        elif init.con >1 and init.con < 4:
            self.conR.setText('-4')
            init.conMod = -4
        elif init.con > 3 and init.dex < 6:
            self.conR.setText('-3')
            init.conMod = -3
        elif init.con > 5 and init.con < 8:
            self.conR.setText('-2')
            init.conMod = -2
        elif init.con > 7 and init.con < 10:
            self.conR.setText('-1')
            init.conMod = -1
        elif init.con > 9 and init.con < 12:
            self.conR.setText('+0')
            init.conMod = 0
        elif init.con > 11 and init.con < 14:
            self.conR.setText('+1')
            init.conMod = 1
        elif init.con > 13 and init.con < 16:
            self.conR.setText('+2')
            init.conMod = 2
        elif init.con > 15 and init.con < 18:
            self.conR.setText('+3')
            init.conMod = 3
        elif init.con > 17 and init.con < 20:
            self.conR.setText('+4')
            init.conMod = 4
        elif init.con == 20:
            self.conR.setText('+5')
            init.conMod = 5
        if init.intel == 1:
            self.intR.setText('-5')
            if self.arcaPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.arcaR.setText(f'+{text}')
                else:
                    self.arcaR.setText(f'{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('-5')
            if self.histPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.histR.setText(f'+{text}')
                else:
                    self.histR.setText(f'{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('-5')
            if self.invePro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.inveR.setText(f'+{text}')
                else:
                    self.inveR.setText(f'{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('-5')
            if self.natuPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.natuR.setText(f'+{text}')
                else:
                    self.natuR.setText(f'{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('-5')
            if self.reliPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.reliR.setText(f'+{text}')
                else:
                    self.reliR.setText(f'{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('-5')
            init.intMod = -5
        elif init.intel >1 and init.intel < 4:
            self.intR.setText('-4')
            if self.arcaPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.arcaR.setText(f'+{text}')
                else:
                    self.arcaR.setText(f'{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('-4')
            if self.histPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.histR.setText(f'+{text}')
                else:
                    self.histR.setText(f'{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('-4')
            if self.invePro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.inveR.setText(f'+{text}')
                else:
                    self.inveR.setText(f'{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('-4')
            if self.natuPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.natuR.setText(f'+{text}')
                else:
                    self.natuR.setText(f'{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('-4')
            if self.reliPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.reliR.setText(f'+{text}')
                else:
                    self.reliR.setText(f'{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('-4')
            init.intMod = -4
        elif init.intel > 3 and init.intel < 6:
            self.intR.setText('-3')
            if self.arcaPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.arcaR.setText(f'+{text}')
                else:
                    self.arcaR.setText(f'{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('-3')
            if self.histPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.histR.setText(f'+{text}')
                else:
                    self.histR.setText(f'{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('-3')
            if self.invePro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.inveR.setText(f'+{text}')
                else:
                    self.inveR.setText(f'{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('-3')
            if self.natuPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.natuR.setText(f'+{text}')
                else:
                    self.natuR.setText(f'{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('-3')
            if self.reliPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.reliR.setText(f'+{text}')
                else:
                    self.reliR.setText(f'{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('-3')
            init.intMod = -3
        elif init.intel > 5 and init.intel < 8:
            self.intR.setText('-2')
            if self.arcaPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.arcaR.setText(f'+{text}')
                else:
                    self.arcaR.setText(f'{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('-2')
            if self.histPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.histR.setText(f'+{text}')
                else:
                    self.histR.setText(f'{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('-2')
            if self.invePro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.inveR.setText(f'+{text}')
                else:
                    self.inveR.setText(f'{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('-2')
            if self.natuPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.natuR.setText(f'+{text}')
                else:
                    self.natuR.setText(f'{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('-2')
            if self.reliPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.reliR.setText(f'+{text}')
                else:
                    self.reliR.setText(f'{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('-2')
            init.intMod = -2
        elif init.intel > 7 and init.intel < 10:
            self.intR.setText('-1')
            if self.arcaPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.arcaR.setText(f'+{text}')
                else:
                    self.arcaR.setText(f'{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('-1')
            if self.histPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.histR.setText(f'+{text}')
                else:
                    self.histR.setText(f'{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('-1')
            if self.invePro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.inveR.setText(f'+{text}')
                else:
                    self.inveR.setText(f'{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('-1')
            if self.natuPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.natuR.setText(f'+{text}')
                else:
                    self.natuR.setText(f'{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('-1')
            if self.reliPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.reliR.setText(f'+{text}')
                else:
                    self.reliR.setText(f'{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('-1')
            init.intMod = -1
        elif init.intel > 9 and init.intel < 12:
            self.intR.setText('+0')
            if self.arcaPro.isChecked() == True:
                text=0+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+0')
            if self.histPro.isChecked() == True:
                text=0+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+0')
            if self.invePro.isChecked() == True:
                text=0+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+0')
            if self.natuPro.isChecked() == True:
                text=0+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+0')
            if self.reliPro.isChecked() == True:
                text=0+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+0')
            init.intMod = 0
        elif init.intel > 11 and init.intel < 13:
            self.intR.setText('+1')
            if self.arcaPro.isChecked() == True:
                text=1+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+1')
            if self.histPro.isChecked() == True:
                text=1+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+1')
            if self.invePro.isChecked() == True:
                text=1+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+1')
            if self.natuPro.isChecked() == True:
                text=1+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+1')
            if self.reliPro.isChecked() == True:
                text=1+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+1')
            init.intMod = 1
        elif init.intel > 13 and init.intel < 16:
            self.intR.setText('+2')
            if self.arcaPro.isChecked() == True:
                text=2+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+2')
            if self.histPro.isChecked() == True:
                text=2+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+2')
            if self.invePro.isChecked() == True:
                text=2+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+2')
            if self.natuPro.isChecked() == True:
                text=2+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+2')
            if self.reliPro.isChecked() == True:
                text=2+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+2')
            init.intMod = 2
        elif init.intel > 15 and init.intel < 18:
            self.intR.setText('+3')
            if self.arcaPro.isChecked() == True:
                text=3+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+3')
            if self.histPro.isChecked() == True:
                text=3+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+3')
            if self.invePro.isChecked() == True:
                text=3+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+3')
            if self.natuPro.isChecked() == True:
                text=3+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+3')
            if self.reliPro.isChecked() == True:
                text=3+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+3')
            init.intMod = 3
        elif init.intel > 17 and init.intel < 20:
            self.intR.setText('+4')
            if self.arcaPro.isChecked() == True:
                text=4+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+4')
            if self.histPro.isChecked() == True:
                text=4+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+4')
            if self.invePro.isChecked() == True:
                text=4+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+4')
            if self.natuPro.isChecked() == True:
                text=4+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+4')
            if self.reliPro.isChecked() == True:
                text=4+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+4')
            init.intMod = 4
        elif init.intel == 20:
            self.intR.setText('+5')
            if self.arcaPro.isChecked() == True:
                text=5+init.profBonus
                self.arcaR.setText(f'+{text}')
            if self.arcaPro.isChecked() == False:
                self.arcaR.setText('+5')
            if self.histPro.isChecked() == True:
                text=5+init.profBonus
                self.histR.setText(f'+{text}')
            if self.histPro.isChecked() == False:
                self.histR.setText('+5')
            if self.invePro.isChecked() == True:
                text=5+init.profBonus
                self.inveR.setText(f'+{text}')
            if self.invePro.isChecked() == False:
                self.inveR.setText('+5')
            if self.natuPro.isChecked() == True:
                text=5+init.profBonus
                self.natuR.setText(f'+{text}')
            if self.natuPro.isChecked() == False:
                self.natuR.setText('+5')
            if self.reliPro.isChecked() == True:
                text=5+init.profBonus
                self.reliR.setText(f'+{text}')
            if self.reliPro.isChecked() == False:
                self.reliR.setText('+5')
            init.intMod = 5
        if init.wis == 1:
            self.wisR.setText('-5')
            if self.animPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.animR.setText(f'+{text}')
                else:
                    self.animR.setText(f'{text}')
            if self.animPro.isChecked() == False:
                self.animR.setText('-5')
            if self.insiPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.insiR.setText(f'+{text}')
                else:
                    self.insiR.setText(f'{text}')
            if self.insiPro.isChecked() == False:
                self.insiR.setText('-5')
            if self.percPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.percR.setText(f'+{text}')
                else:
                    self.percR.setText(f'{text}')
            if self.percPro.isChecked() == False:
                self.percR.setText('-5')
            if self.mediPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.mediR.setText(f'+{text}')
                else:
                    self.mediR.setText(f'{text}')
            if self.mediPro.isChecked() == False:
                self.mediR.setText('-5')
            if self.survPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.survR.setText(f'+{text}')
                else:
                    self.survR.setText(f'{text}')
            if self.survPro.isChecked() == False:
                self.survR.setText('-5')
            init.wisMod = -5
        elif init.wis >1 and init.wis < 4:
            self.wisR.setText('-4')
            if self.animPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.animR.setText(f'+{text}')
                else:
                    self.animR.setText(f'{text}')
            if self.animPro.isChecked() == False:
                self.animR.setText('-4')
            if self.insiPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.insiR.setText(f'+{text}')
                else:
                    self.insiR.setText(f'{text}')
            if self.insiPro.isChecked() == False:
                self.insiR.setText('-4')
            if self.percPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.percR.setText(f'+{text}')
                else:
                    self.percR.setText(f'{text}')
            if self.percPro.isChecked() == False:
                self.percR.setText('-4')
            if self.mediPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.mediR.setText(f'+{text}')
                else:
                    self.mediR.setText(f'{text}')
            if self.mediPro.isChecked() == False:
                self.mediR.setText('-4')
            if self.survPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.survR.setText(f'+{text}')
                else:
                    self.survR.setText(f'{text}')
            if self.survPro.isChecked() == False:
                self.survR.setText('-4')
            init.wisMod = -4
        elif init.wis > 3 and init.dex < 6:
            self.wisR.setText('-3')
            if self.animPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.animR.setText(f'+{text}')
                else:
                    self.animR.setText(f'{text}')
            if self.animPro.isChecked() == False:
                self.animR.setText('-3')
            if self.insiPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.insiR.setText(f'+{text}')
                else:
                    self.insiR.setText(f'{text}')
            if self.insiPro.isChecked() == False:
                self.insiR.setText('-3')
            if self.percPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.percR.setText(f'+{text}')
                else:
                    self.percR.setText(f'{text}')
            if self.percPro.isChecked() == False:
                self.percR.setText('-3')
            if self.mediPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.mediR.setText(f'+{text}')
                else:
                    self.mediR.setText(f'{text}')
            if self.mediPro.isChecked() == False:
                self.mediR.setText('-3')
            if self.survPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.survR.setText(f'+{text}')
                else:
                    self.survR.setText(f'{text}')
            if self.survPro.isChecked() == False:
                self.survR.setText('-3')
            init.wisMod = -3
        elif init.wis > 5 and init.wis < 8:
            self.wisR.setText('-2')
            if self.animPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.animR.setText(f'+{text}')
                else:
                    self.animR.setText(f'{text}')
            if self.animPro.isChecked() == False:
                self.animR.setText('-2')
            if self.insiPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.insiR.setText(f'+{text}')
                else:
                    self.insiR.setText(f'{text}')
            if self.insiPro.isChecked() == False:
                self.insiR.setText('-2')
            if self.percPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.percR.setText(f'+{text}')
                else:
                    self.percR.setText(f'{text}')
            if self.percPro.isChecked() == False:
                self.percR.setText('-2')
            if self.mediPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.mediR.setText(f'+{text}')
                else:
                    self.mediR.setText(f'{text}')
            if self.mediPro.isChecked() == False:
                self.mediR.setText('-2')
            if self.survPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.survR.setText(f'+{text}')
                else:
                    self.survR.setText(f'{text}')
            if self.survPro.isChecked() == False:
                self.survR.setText('-2')
            init.wisMod = -2
        elif init.wis > 7 and init.wis < 10:
            self.wisR.setText('-1')
            if self.animPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.animR.setText(f'+{text}')
                else:
                    self.animR.setText(f'{text}')
            if self.animPro.isChecked() == False:
                self.animR.setText('-1')
            if self.insiPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.insiR.setText(f'+{text}')
                else:
                    self.insiR.setText(f'{text}')
            if self.insiPro.isChecked() == False:
                self.insiR.setText('-1')
            if self.percPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.percR.setText(f'+{text}')
                else:
                    self.percR.setText(f'{text}')
            if self.percPro.isChecked() == False:
                self.percR.setText('-1')
            if self.mediPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.mediR.setText(f'+{text}')
                else:
                    self.mediR.setText(f'{text}')
            if self.mediPro.isChecked() == False:
                self.mediR.setText('-1')
            if self.survPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.survR.setText(f'+{text}')
                else:
                    self.survR.setText(f'{text}')
            if self.survPro.isChecked() == False:
                self.survR.setText('-1')
            init.wisMod = -1
        elif init.wis > 9 and init.wis < 12:
            self.wisR.setText('+0')
            if self.animPro.isChecked() == True:
                text=0+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+0')
            if self.insiPro.isChecked() == True:
                text=0+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+0')
            if self.mediPro.isChecked() == True:
                text=0+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+0')
            if self.percPro.isChecked() == True:
                text=0+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+0')
            if self.survPro.isChecked() == True:
                text=0+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+0')
            init.wisMod = 0
        elif init.wis > 11 and init.wis < 14:
            self.wisR.setText('+1')
            if self.animPro.isChecked() == True:
                text=1+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+1')
            if self.insiPro.isChecked() == True:
                text=1+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+1')
            if self.mediPro.isChecked() == True:
                text=1+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+1')
            if self.percPro.isChecked() == True:
                text=1+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+1')
            if self.survPro.isChecked() == True:
                text=1+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+1')
            init.wisMod = 1
        elif init.wis > 13 and init.wis < 16:
            self.wisR.setText('+2')
            if self.animPro.isChecked() == True:
                text=2+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+2')
            if self.insiPro.isChecked() == True:
                text=2+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+2')
            if self.mediPro.isChecked() == True:
                text=2+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+2')
            if self.percPro.isChecked() == True:
                text=2+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+2')
            if self.survPro.isChecked() == True:
                text=2+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+2')
            init.wisMod = 2
        elif init.wis > 15 and init.wis < 18:
            self.wisR.setText('+3')
            if self.animPro.isChecked() == True:
                text=3+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+3')
            if self.insiPro.isChecked() == True:
                text=3+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+3')
            if self.mediPro.isChecked() == True:
                text=3+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+3')
            if self.percPro.isChecked() == True:
                text=3+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+3')
            if self.survPro.isChecked() == True:
                text=3+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+3')
            init.wisMod = 3
        elif init.wis > 17 and init.wis < 20:
            self.wisR.setText('+4')
            if self.animPro.isChecked() == True:
                text=4+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+4')
            if self.insiPro.isChecked() == True:
                text=4+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+4')
            if self.mediPro.isChecked() == True:
                text=4+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+4')
            if self.percPro.isChecked() == True:
                text=4+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+4')
            if self.survPro.isChecked() == True:
                text=4+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+4')
            init.wisMod = 4
        elif init.wis == 20:
            self.wisR.setText('+5')
            if self.animPro.isChecked() == True:
                text=5+init.profBonus
                self.animR.setText(f'+{text}')
            elif self.animPro.isChecked() == False:
                self.animR.setText('+5')
            if self.insiPro.isChecked() == True:
                text=5+init.profBonus
                self.insiR.setText(f'+{text}')
            elif self.insiPro.isChecked() == False:
                self.insiR.setText('+5')
            if self.mediPro.isChecked() == True:
                text=5+init.profBonus
                self.mediR.setText(f'+{text}')
            elif self.mediPro.isChecked() == False:
                self.mediR.setText('+5')
            if self.percPro.isChecked() == True:
                text=5+init.profBonus
                self.percR.setText(f'+{text}')
            elif self.percPro.isChecked() == False:
                self.percR.setText('+5')
            if self.survPro.isChecked() == True:
                text=5+init.profBonus
                self.survR.setText(f'+{text}')
            elif self.survPro.isChecked() == False:
                self.survR.setText('+5')
            init.wisMod = 5
        if init.cha == 1:
            self.chaR.setText('-5')
            if self.decePro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.deceR.setText(f'+{text}')
                else:
                    self.deceR.setText(f'{text}')
            if self.decePro.isChecked() == False:
                self.deceR.setText('-5')
            if self.intiPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.intiR.setText(f'+{text}')
                else:
                    self.intiR.setText(f'{text}')
            if self.intiPro.isChecked() == False:
                self.intiR.setText('-5')
            if self.perfPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.perfR.setText(f'+{text}')
                else:
                    self.perfR.setText(f'{text}')
            if self.perfPro.isChecked() == False:
                self.perfR.setText('-5')
            if self.persPro.isChecked() == True:
                text=-5+init.profBonus
                if text > -1:
                    self.persR.setText(f'+{text}')
                else:
                    self.persR.setText(f'{text}')
            if self.persPro.isChecked() == False:
                self.persR.setText('-5')
            init.chaMod = -5
        elif init.cha >1 and init.cha < 4:
            self.chaR.setText('-4')
            if self.decePro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.deceR.setText(f'+{text}')
                else:
                    self.deceR.setText(f'{text}')
            if self.decePro.isChecked() == False:
                self.deceR.setText('-4')
            if self.intiPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.intiR.setText(f'+{text}')
                else:
                    self.intiR.setText(f'{text}')
            if self.intiPro.isChecked() == False:
                self.intiR.setText('-4')
            if self.perfPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.perfR.setText(f'+{text}')
                else:
                    self.perfR.setText(f'{text}')
            if self.perfPro.isChecked() == False:
                self.perfR.setText('-4')
            if self.persPro.isChecked() == True:
                text=-4+init.profBonus
                if text > -1:
                    self.persR.setText(f'+{text}')
                else:
                    self.persR.setText(f'{text}')
            if self.persPro.isChecked() == False:
                self.persR.setText('-4')
            init.chaMod = -4
        elif init.cha > 3 and init.cha < 6:
            self.chaR.setText('-3')
            if self.decePro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.deceR.setText(f'+{text}')
                else:
                    self.deceR.setText(f'{text}')
            if self.decePro.isChecked() == False:
                self.deceR.setText('-3')
            if self.intiPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.intiR.setText(f'+{text}')
                else:
                    self.intiR.setText(f'{text}')
            if self.intiPro.isChecked() == False:
                self.intiR.setText('-3')
            if self.perfPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.perfR.setText(f'+{text}')
                else:
                    self.perfR.setText(f'{text}')
            if self.perfPro.isChecked() == False:
                self.perfR.setText('-3')
            if self.persPro.isChecked() == True:
                text=-3+init.profBonus
                if text > -1:
                    self.persR.setText(f'+{text}')
                else:
                    self.persR.setText(f'{text}')
            if self.persPro.isChecked() == False:
                self.persR.setText('-3')
            init.chaMod = -3
        elif init.cha > 5 and init.cha < 8:
            self.chaR.setText('-2')
            if self.decePro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.deceR.setText(f'+{text}')
                else:
                    self.deceR.setText(f'{text}')
            if self.decePro.isChecked() == False:
                self.deceR.setText('-2')
            if self.intiPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.intiR.setText(f'+{text}')
                else:
                    self.intiR.setText(f'{text}')
            if self.intiPro.isChecked() == False:
                self.intiR.setText('-2')
            if self.perfPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.perfR.setText(f'+{text}')
                else:
                    self.perfR.setText(f'{text}')
            if self.perfPro.isChecked() == False:
                self.perfR.setText('-2')
            if self.persPro.isChecked() == True:
                text=-2+init.profBonus
                if text > -1:
                    self.persR.setText(f'+{text}')
                else:
                    self.persR.setText(f'{text}')
            if self.persPro.isChecked() == False:
                self.persR.setText('-2')
            init.chaMod = -2
        elif init.cha > 7 and init.cha < 10:
            self.chaR.setText('-1')
            if self.decePro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.deceR.setText(f'+{text}')
                else:
                    self.deceR.setText(f'{text}')
            if self.decePro.isChecked() == False:
                self.deceR.setText('-1')
            if self.intiPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.intiR.setText(f'+{text}')
                else:
                    self.intiR.setText(f'{text}')
            if self.intiPro.isChecked() == False:
                self.intiR.setText('-1')
            if self.perfPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.perfR.setText(f'+{text}')
                else:
                    self.perfR.setText(f'{text}')
            if self.perfPro.isChecked() == False:
                self.perfR.setText('-1')
            if self.persPro.isChecked() == True:
                text=-1+init.profBonus
                if text > -1:
                    self.persR.setText(f'+{text}')
                else:
                    self.persR.setText(f'{text}')
            if self.persPro.isChecked() == False:
                self.persR.setText('-1')
            init.chaMod = -1
        elif init.cha > 9 and init.cha < 12:
            self.chaR.setText('+0')
            if self.decePro.isChecked() == True:
                text=0+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+0')
            if self.intiPro.isChecked() == True:
                text=0+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+0')
            if self.perfPro.isChecked() == True:
                text=0+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+0')
            if self.persPro.isChecked() == True:
                text=0+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+0')
            init.chaMod = 0
        elif init.cha > 11 and init.cha < 14:
            self.chaR.setText('+1')
            if self.decePro.isChecked() == True:
                text=1+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+1')
            if self.intiPro.isChecked() == True:
                text=1+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+1')
            if self.perfPro.isChecked() == True:
                text=1+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+1')
            if self.persPro.isChecked() == True:
                text=1+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+1')
            init.chaMod = 1
        elif init.cha > 13 and init.cha < 16:
            self.chaR.setText('+2')
            if self.decePro.isChecked() == True:
                text=2+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+2')
            if self.intiPro.isChecked() == True:
                text=2+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+2')
            if self.perfPro.isChecked() == True:
                text=2+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+2')
            if self.persPro.isChecked() == True:
                text=2+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+2')
            init.chaMod = 2
        elif init.cha > 15 and init.cha < 18:
            self.chaR.setText('+3')
            if self.decePro.isChecked() == True:
                text=3+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+3')
            if self.intiPro.isChecked() == True:
                text=3+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+3')
            if self.perfPro.isChecked() == True:
                text=3+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+3')
            if self.persPro.isChecked() == True:
                text=3+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+3')
            init.chaMod = 3
        elif init.cha > 17 and init.cha < 20:
            self.chaR.setText('+4')
            if self.decePro.isChecked() == True:
                text=4+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+4')
            if self.intiPro.isChecked() == True:
                text=4+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+4')
            if self.perfPro.isChecked() == True:
                text=4+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+4')
            if self.persPro.isChecked() == True:
                text=4+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+4')
            init.chaMod = 4
        elif init.cha == 20:
            self.chaR.setText('+5')
            if self.decePro.isChecked() == True:
                text=5+init.profBonus
                self.deceR.setText(f'+{text}')
            elif self.decePro.isChecked() == False:
                self.deceR.setText('+5')
            if self.intiPro.isChecked() == True:
                text=5+init.profBonus
                self.intiR.setText(f'+{text}')
            elif self.intiPro.isChecked() == False:
                self.intiR.setText('+5')
            if self.perfPro.isChecked() == True:
                text=5+init.profBonus
                self.perfR.setText(f'+{text}')
            elif self.perfPro.isChecked() == False:
                self.perfR.setText('+5')
            if self.persPro.isChecked() == True:
                text=5+init.profBonus
                self.persR.setText(f'+{text}')
            elif self.persPro.isChecked() == False:
                self.persR.setText('+5')
            init.chaMod = 5

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