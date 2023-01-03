from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
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
        self.init()

    def init(self):
        self.init_widgets()
        self.button_config()
        self.init_ex_combo_val()
    
    def init_ex_combo_val(self):
        self.comboBox_ex_counter.addItem(str(0))
        self.comboBox_ex_counter.addItem(str(1))
        self.comboBox_ex_counter.addItem(str(2))

        default_item = self.db.getDataFromTableWithId("program_table", 1)[0][1]
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
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Bilgilendirme")
        dlg.setText("Programimizin bu kismi gelistirilme asamasindadir.")
        button = dlg.exec()

    def button_open_words_click(self):
        self.read_db = read_database()
        self.read_db.show()
        self.hide()

    def button_create_csv_click(self):
        self.saveFileDialog()

    def button_save_manuel_word_click(self):
        self.db.updateDataFromTable("program_table", 1, "default_ex_counter", self.comboBox_ex_counter.currentText())
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