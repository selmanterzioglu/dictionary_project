from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys
from save_manuel_word import save_manuel_word
from databaseProcess import databaseProcess
from read_database import read_database

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.db = databaseProcess("programDatabase.db")
        self.show()
        self.widgets = dict()
        self.init_widgets()
        self.button_config()

    def init_widgets (self):
        self.widgets['button_translate'] = self.button_translate
        self.widgets['button_save_manuel_word'] = self.button_save_manuel_word
        self.widgets['button_open_words'] = self.button_open_words

    def button_config(self):
        self.widgets['button_save_manuel_word'].clicked.connect(self.button_save_manuel_word_click)
        self.widgets['button_open_words'].clicked.connect(self.button_open_words_click)

    def button_open_words_click(self):
        self.read_db = read_database()
        self.read_db.show()
        self.hide()

    def button_create_csv_click(self):
        print("test")
        self.saveFileDialog()

    def button_save_manuel_word_click(self):
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