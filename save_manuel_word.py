from PyQt5 import QtWidgets, uic
import sys
from databaseProcess import databaseProcess
from PyQt5.QtWidgets import QMessageBox
import special_functions as sf

class save_manuel_word(QtWidgets.QMainWindow):
    def __init__(self):
        super(save_manuel_word, self).__init__()
        uic.loadUi('./ui/save_manuel_word.ui', self)
        self.init()
        self.init_widgets()
        self.show()

    def init(self):
        self.widgets = dict()
        self.program_db = databaseProcess("./db/programDatabase.db")
        self.ex_counter = int(self.program_db.getDataFromTableWithId("program_table", 1)[0][2])
        self.table_name = self.program_db.getDataFromTableWithId("program_table", 2)[0][2]
        self.db = databaseProcess("./db/words.db")

    def init_widgets (self):
        self.button_save.clicked.connect(self.button_save_click)
        if(self.ex_counter == 0):
            self.label_ex_1_en.hide()
            self.lineEdit_ex_1_en.hide()
            self.label_ex_1_tr.hide()
            self.lineEdit_ex_1_tr.hide()

            self.label_ex_2_en.hide()
            self.lineEdit_ex_2_en.hide()
            self.label_ex_2_tr.hide()
            self.lineEdit_ex_2_tr.hide()

        elif(self.ex_counter == 1):
            self.label_ex_2_en.hide()
            self.lineEdit_ex_2_en.hide()
            self.label_ex_2_tr.hide()
            self.lineEdit_ex_2_tr.hide()

    def button_save_click(self):
        eng = self.lineEdit_english.text()
        tr = self.lineEdit_turkish.text()
        ex_1_en = self.lineEdit_ex_1_en.text()
        ex_1_tr = self.lineEdit_ex_1_tr.text()
        ex_2_en = self.lineEdit_ex_2_en.text()
        ex_2_tr = self.lineEdit_ex_1_tr.text()

        if(self.ex_counter == 0):
            data = (eng, tr, "", "", "", "")
        elif(self.ex_counter == 1):
            data = (eng, tr, ex_1_en, ex_1_tr, "", "")
        else:
            data = (eng, tr, ex_1_en, ex_1_tr, ex_2_en, ex_2_tr)

        self.db.setWordDataToTable(self.table_name, data)
        
        self.lineEdit_english.setText("")
        self.lineEdit_turkish.setText("")
        self.lineEdit_ex_1_en.setText("")
        self.lineEdit_ex_1_tr.setText("")
        self.lineEdit_ex_2_en.setText("")
        self.lineEdit_ex_2_tr.setText("")

        sf.msg_box("Kayit Basarili", "Kelimeniz veritabanina basariyla kaydedildi.!")
