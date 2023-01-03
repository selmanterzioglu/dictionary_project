from PyQt5 import QtWidgets, uic
import sys
from databaseProcess import databaseProcess
from PyQt5.QtWidgets import *
import codecs
import os

class read_database(QtWidgets.QMainWindow):
    def __init__(self):
        super(read_database, self).__init__()
        uic.loadUi('read_database.ui', self)
        self.db = databaseProcess("words.db")

        self.table_list = self.db.list_table_name()
        self.load_database_list()
        self.table_name = self.comboBox_database_list.currentText()
        self.all_word_data = self.db.getDataFromTable(self.table_name)

        self.show()
        self.init()
    
    def init(self):
        self.widgets = dict()
        self.ex_counter = 1
        self.load_word_list_from_db()
        self.button_delete_word.clicked.connect(self.button_delete_word_clicked)
        self.button_create_csv.clicked.connect(self.saveFileDialog)
        self.comboBox_database_list.currentTextChanged.connect(self.database_changed)


    def load_word_list_from_db(self):
        self.word_list.clear()
        row = self.db.getLineCountFromTable(self.table_name)
        self.word_list.setRowCount(row) 
        self.word_list.setColumnCount(7) 
        
        self.all_word_data = self.db.getDataFromTable(self.table_name)

        self.word_list.setHorizontalHeaderLabels(["id", "English", "Turkish", "Sentence 1", "Sentence 2", "Sentence 3","Sentence 4"])

        for i in range(row):
            self.word_list.setItem(i,0, QTableWidgetItem(str(self.all_word_data[i][0])))
            self.word_list.setItem(i,1, QTableWidgetItem(self.all_word_data[i][1]))
            self.word_list.setItem(i,2, QTableWidgetItem(self.all_word_data[i][2]))
            self.word_list.setItem(i,3, QTableWidgetItem(self.all_word_data[i][3]))
            self.word_list.setItem(i,4, QTableWidgetItem(self.all_word_data[i][4]))
            self.word_list.setItem(i,5, QTableWidgetItem(self.all_word_data[i][5]))
            self.word_list.setItem(i,6, QTableWidgetItem(self.all_word_data[i][6]))

    def button_delete_word_clicked(self):
        self.word_list.setSelectionMode(QAbstractItemView.SingleSelection)
        selected_index = self.word_list.currentRow()
        self.word_list.removeRow(selected_index)
        self.db.delete_row(self.table_name, self.all_word_data[selected_index][0])

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Silme islemi basarili")
        dlg.setText("Kelimeniz veritabanindan basariyla silindi.!")
        button = dlg.exec()
    
    def load_database_list(self):
        self.comboBox_database_list.clear()
        for i in self.table_list: 
            self.comboBox_database_list.addItem(i)

    def database_changed(self, value):
        self.table_name = value
        self.load_word_list_from_db()

    def saveFileDialog(self):

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","csv Files (*.csv)", options=options)
        if file_name:
            self.create_csv_file(file_name)

    def create_csv_file(self, file_name):
        data_for_write = ""
        counter = 0
        for i in range(len(self.all_word_data)):
            for k in range(1, len(self.all_word_data[i])):
                if(self.all_word_data[i][k] != ""):
                    data_for_write += self.all_word_data[i][k] + ";"
                if(k == 6):
                    data_for_write = data_for_write[:-1]
                    data_for_write += "\n"

        file = codecs.open(file_name, "w", "utf-8")
        file.write(data_for_write)
        file.close()

        head, tail = os.path.split(file_name)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Kayit Basarili")
        dlg.setText("""Kelime Listeniz "{}" adiyla \n"{}"\nKonumuna kaydedilmistir.""".format(tail, head))
        button = dlg.exec()


app = QtWidgets.QApplication(sys.argv)
window = read_database()
app.exec_()