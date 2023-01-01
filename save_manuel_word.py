from PyQt5 import QtWidgets, uic
import sys
from databaseProcess import databaseProcess
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QMessageBox

class save_manuel_word(QtWidgets.QMainWindow):
    def __init__(self):
        super(save_manuel_word, self).__init__()
        uic.loadUi('save_manuel_word.ui', self)
        self.show()
        self.init()
    
    def init(self):
        self.widgets = dict()
        self.ex_counter = 1
        self.init_widgets()
        self.button_config()
        self.db = databaseProcess("words.db")

    def init_widgets (self):
        self.widgets['button_save'] = self.button_save

    def button_config(self):
        self.widgets['button_save'].clicked.connect(self.button_save_click)

        if(self.ex_counter == 0):
            self.lineEdit_ex_1.hide()
            self.label_ex_1.hide()
            self.lineEdit_ex_2.hide()
            self.label_ex_2.hide()
            self.lineEdit_ex_3.hide()
            self.label_ex_3.hide()
            self.lineEdit_ex_4.hide()
            self.label_ex_4.hide()
        if(self.ex_counter == 1):
            self.lineEdit_ex_2.hide()
            self.label_ex_2.hide()
            self.lineEdit_ex_3.hide()
            self.label_ex_3.hide()
            self.lineEdit_ex_4.hide()
            self.label_ex_4.hide()
        elif(self.ex_counter == 2):
            self.lineEdit_ex_3.hide()
            self.label_ex_3.hide()
            self.lineEdit_ex_4.hide()
            self.label_ex_4.hide()
        elif(self.ex_counter == 3):
            self.lineEdit_ex_4.hide()
            self.label_ex_4.hide()
    
    def button_save_click(self):
        eng = self.lineEdit_english.text()
        tr = self.lineEdit_turkish.text()
        ex_1 = self.lineEdit_ex_1.text()
        ex_2 = self.lineEdit_ex_2.text()
        ex_3 = self.lineEdit_ex_3.text()
        ex_4 = self.lineEdit_ex_4.text()
        data = data = (eng, tr, ex_1, ex_2, ex_3, ex_4)
        self.db.setWordDataToTable("test", data)
        
        self.lineEdit_english.setText("")
        self.lineEdit_turkish.setText("")
        self.lineEdit_ex_1.setText("")
        self.lineEdit_ex_2.setText("")
        self.lineEdit_ex_3.setText("")
        self.lineEdit_ex_4.setText("")

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Kayit Basarili")
        dlg.setText("Kelimeniz veritabanina basariyla kaydedildi.!")
        button = dlg.exec()
