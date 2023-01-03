from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
from save_manuel_word import save_manuel_word
from databaseProcess import databaseProcess
from read_database import read_database
import special_functions as sf
from word_translate import word_translate

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./ui/main.ui', self)
        self.show()
        self.db = databaseProcess("./db/programDatabase.db")
        self.word_db = databaseProcess("./db/words.db")
        
        self.widgets = dict()
        self.init()

    def init(self):
        self.init_widgets()
        self.button_config()
        self.init_ex_combo_val()
        self.init_database_combo_val()

    def init_database_combo_val(self):
        word_table_list = self.word_db.list_table_name()
        for i in word_table_list:
            self.comboBox_database.addItem(str(i))

        default_item = self.db.getDataFromTableWithId("program_table", 2)[0][2]
        self.comboBox_database.setCurrentText(str(default_item))


    def init_ex_combo_val(self):
        self.comboBox_ex_counter.addItem(str(0))
        self.comboBox_ex_counter.addItem(str(1))
        self.comboBox_ex_counter.addItem(str(2))

        default_item = self.db.getDataFromTableWithId("program_table", 1)[0][2]

        self.comboBox_ex_counter.setCurrentText(str(default_item))


    def init_widgets (self):
        self.widgets['button_translate'] = self.button_translate
        self.widgets['button_save_manuel_word'] = self.button_save_manuel_word
        self.widgets['button_open_words'] = self.button_open_words

    def button_config(self):
        self.widgets['button_save_manuel_word'].clicked.connect(self.button_save_manuel_word_click)
        self.widgets['button_open_words'].clicked.connect(self.button_open_words_click)
        self.widgets['button_translate'].clicked.connect(self.button_translate_click)

    def button_translate_click(self):
        self.db.updateDataFromTable("program_table", 2, "feature_value", self.comboBox_database.currentText())
        self.word_translate = word_translate()
        self.word_translate.show()
        self.hide()

    def button_open_words_click(self):
        self.read_db = read_database()
        self.read_db.show()
        self.hide()

    def button_create_csv_click(self):
        self.saveFileDialog()

    def button_save_manuel_word_click(self):
        self.db.updateDataFromTable("program_table", 1, "feature_value", self.comboBox_ex_counter.currentText())
        self.db.updateDataFromTable("program_table", 2, "feature_value", self.comboBox_database.currentText())
        self.save_manuel_word = save_manuel_word()
        self.save_manuel_word.show()
        self.hide()

    def button_save_word_click(self):
        self.read_db = read_database()
        self.read_db.show()
        self.hide()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()