from PyQt5 import QtWidgets, uic
import sys
from databaseProcess import databaseProcess
import special_functions as sf
from googletrans import Translator
import googletrans

class word_translate(QtWidgets.QMainWindow):
    def __init__(self):
        super(word_translate, self).__init__()
        uic.loadUi('./ui/word_translate.ui', self)
        self.init()
        self.show()

    def init(self):
        self.widgets = dict()
        self.db = databaseProcess("./db/words.db")
        self.program_db = databaseProcess("./db/programDatabase.db")
        self.table_name = self.program_db.getDataFromTableWithId("program_table", 2)[0][2]
        print("table: ", self.table_name)

        self.button_translate.clicked.connect(self.translate_func)
        self.button_swap.clicked.connect(self.swap_text)
        self.button_save_word.clicked.connect(self.save_word)
        # self.lineEdit_source.textChanged.connect(self.translate_func)
       
        self.source = "tr"
        self.destination = "en"
        self.translate = Translator() 
        self.source_text = ""
        self.destination_text = ""
        self.translated_text = ""

    def translate_func(self):
        self.lineEdit_destination.setText("")
        self.source_text = self.lineEdit_source.text(),
        try:
            self.statusBar().showMessage('Translating...')
            self.translated_txt = self.translate.translate(text = self.source_text, src=self.source, dest=self.destination).text
        except TypeError:
            self.statusBar().showMessage('Translate error. Try again...')

        self.lineEdit_destination.setText(self.translated_text)
        self.statusBar().showMessage('')
    
    def save_word(self):
        en = None
        tr = None

        if(self.source == "tr"):
            tr = self.lineEdit_source.text()
            eng = self.lineEdit_destination.text()
        elif(self.source == "en"):
            eng = self.lineEdit_source.text()
            tr = self.lineEdit_destination.text()
        
        if(en == "" or tr == ""):
            sf.msg_box("Hata", "Kaynak dil sözcük veya çeviri boş olamaz.!")
        else:
            data = (eng, tr, "", "", "", "")
            self.db.setWordDataToTable(self.table_name, data)
            sf.msg_box("Kayit Basarili", "Kelimeniz veritabanina basariyla kaydedildi.!")

    def swap_text(self):
        source = self.source
        destination = self.destination
        self.source = destination
        self.destination = source
        
        origin_source = self.lineEdit_source.text()
        origin_destination = self.lineEdit_destination.text()

        if(self.source == "tr"):
            self.label_source.setText("Türkçe")
            self.label_destination.setText("İngilizce")
        elif(self.source == "en"):
            self.label_source.setText("İngilizce")
            self.label_destination.setText("Türkçe")

        self.lineEdit_destination.setText(origin_source)
        self.lineEdit_source.setText(origin_destination)
        
        self.source_text = self.lineEdit_source.text()
        try:
            self.statusBar().showMessage('Translating...')
            self.translated_txt = self.translate.translate(text = self.source_text, src=self.source, dest=self.destination).text
        except TypeError:
            self.statusBar().showMessage('Translate error. Try again...')

        self.lineEdit_destination.setText(self.translated_text)
        self.statusBar().showMessage('')

