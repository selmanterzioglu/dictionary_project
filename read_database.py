from PyQt5 import QtWidgets, uic
import sys
from databaseProcess import databaseProcess
from PyQt5.QtWidgets import *
import codecs
import os
import special_functions as sf

class read_database(QtWidgets.QMainWindow):
    def __init__(self):
        super(read_database, self).__init__()
        uic.loadUi('./ui/read_database.ui', self)
        self.db = databaseProcess("./db/words.db")

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
        self.button_configure()
        self.comboBox_database_list.currentTextChanged.connect(self.database_changed)

    def button_configure(self):
        self.button_delete_word.clicked.connect(self.button_delete_word_clicked)
        self.button_create_csv.clicked.connect(self.saveFileDialog)
        self.button_delete_word_list.clicked.connect(self.delete_word_list)
        self.button_create_word_list.clicked.connect(self.create_word_list)

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

        sf.msg_box("Silme islemi basarili", "Kelimeniz veritabanindan basariyla silindi.!")
    
    def load_database_list(self):
        self.comboBox_database_list.clear()
        for i in self.table_list:
            self.comboBox_database_list.addItem(i)

    def database_changed(self, value):
        self.table_name = value
        self.load_word_list_from_db()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self,"CSV Dosyasini Kaydet","","csv Files (*.csv)", options=options)
        if file_name:
            self.create_csv_file(file_name)

    def delete_word_list(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Kelime Listesi Silme Onayi")
        msgBox.setText("{} adli kelime listesi silinsin mi ?".format(self.table_name))
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret_val = msgBox.exec()

        if ret_val == QMessageBox.Ok:
            table = self.table_name
            self.db.delete_table(table)
            index = self.comboBox_database_list.findText(table)
            self.comboBox_database_list.removeItem(index)
            sf.msg_box("Silme Basarili", "{} adli kelime listeniz veritabanindan basariyla silinmistir".format(table))
            
    def create_word_list(self):
        word_list = self.db.list_table_name()
        is_found = False

        text, okPressed = QInputDialog.getText(self, "Yeni Kelime Listesi Kaydi","Yeni Kelime Listenizin Ismini Girin", QLineEdit.Normal, "")
        
        if okPressed and text != '':
            for i in word_list:
                if (i == text):
                    is_found = True

            if(is_found):
                sf.msg_box("Hata", """{} adli kelime listesi veritabaninda mevcuttur. Lutfen farkli bir isim girin.""".format(text))
                self.create_word_list()
            else:
                self.db.createTableToDatabase(text)
                sf.msg_box("Kayit Basarili", "{} adli kelime listesi veritabanina basariyla kaydedilmistir.".format(text))
                self.comboBox_database_list.addItem(text)

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

        sf.msg_box("Kayit Basarili", """Kelime Listeniz "{}" adiyla \n"{}"\nKonumuna kaydedilmistir.""".format(tail, head))
