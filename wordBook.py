import pyperclip
from libs import *


class shorcutClass():
    
    programDbName = "programDatabase.db"

    def setNewShorcutData(self, data):
        db = databaseProcess(self.programDbName)
        db.setShorcutDataToTable("shorcut", data)
    
    def setDefaultShorcut(self):
        db = databaseProcess(self.programDbName)
        db.updateDataFromTable("shorcut", 1, "save", self.getDefaultShorcut()[0])
        db.updateDataFromTable("shorcut", 1, "enTr", self.getDefaultShorcut()[1])
        db.updateDataFromTable("shorcut", 1, "trEn", self.getDefaultShorcut()[2])
        db.updateDataFromTable("shorcut", 1, "closeProgram", self.getDefaultShorcut()[3])
        db.updateDataFromTable("shorcut", 1, "translationType", self.getDefaultShorcut()[4])
    
    def updateShorcutData(self, columnName, newShorcut):
        db = databaseProcess(self.programDbName)
        db.updateDataFromTable("shorcut", 1, columnName, newShorcut)

    @staticmethod
    def getDefaultShorcut():
        save = 1
        enTr = 2
        trEn = 3
        closeProgram = 0
        translationType = enTr
        return [save, enTr, trEn, closeProgram, translationType]

    def getCustomShorcut(self):
        db = databaseProcess(self.programDbName)
        data = db.getDataFromTableWithId("shorcut", 1)
        list = [item for item in data[0]] 
        list.pop(0) ## en bastan cekilen id bilgisini  siliyor
        return list

    @staticmethod
    def getShorcutWithId(id): 
        """[BETA] Bu fonksiyonun yazimina birden fazla kullanicinin  calismasi  hedeflendiginde baslanacaktir."""
        db = databaseProcess("programDatabase.db")
        # if(key != )
        data = db.getDataFromTableWithId("shorcut", id)
        return data    
    
class WordBook():

    translator = Translator()
    shorcut = shorcutClass()
    info = info()
    sf = specialFunction()

    wordDbName = "words.db"
    programDbName = "programDatabase.db"

    sourceLanguage = ""
    destinationLanguage = ""

    Save = None
    enTr = None 
    trEn = None
    closeProgram = None
    translationType = None

    def __init__(self, tableName):
        self.tableName = tableName
        self.getShorcut()
        self.welcomeMenu()

    def getShorcut(self):
        shorcutData = self.shorcut.getCustomShorcut()
        self.Save = shorcutData[0] 
        self.enTr = shorcutData[1]
        self.trEn = shorcutData[2]
        self.closeProgram = shorcutData[3]
        self.translationType =  shorcutData[4]
    
        return [self.Save, self.enTr, self.trEn, self.closeProgram, self.translationType]

    def welcomeMenu(self):
        change = input("""
        Kelime Kaydetme Modulune Hosgeldiniz.!
        Kayit islemi {} adli listeye yapilacaktir.

        Lütfen Aşağıdaki işlemlerden birisini  seçiniz: 
        ****************************************************
            0. Cikis
            1. Kelime Kaydetme Islemine Devam Et
            2. Klavye Kisayollarini Goster
            3. Klavye Kisayollarini Degistir
        ****************************************************
        --> """.format(self.tableName))
        
        if (change == "0"):
            exit()
        elif (change == "1"):
            self.wordFunction()
        elif (change == "2"):
            self.sf.clear()
            print("[0]Save: {}\n[1]En->Tr: {}\n[2]Tr->En: {}\n[3]Close Program: {}\n[4]Translation Type: {}"
            .format(self.getShorcut()[0], self.getShorcut()[1], self.getShorcut()[2], self.getShorcut()[3], self.getShorcut()[4]) )
            self.welcomeMenu()
        elif (change == "3"):
            self.changeShorcut()
        else:
            self.info.elseChanges()  
            self.welcomeMenu() 

    def changeShorcut(self):
        print("""Klavye Kısayolu Değiştirme Ekranına Hoşgeldiniz. Mevcut Kısayollarınız: """)
        print("[0]Save: {}\n[1]En->Tr: {}\n[2]Tr->En: {}\n[3]Close Program: {}\n[4]Translation Type: {}"
        .format(self.getShorcut()[0], self.getShorcut()[1], self.getShorcut()[2], self.getShorcut()[3], self.getShorcut()[4]) )
        change = input("\n\nLutfen degistirmek istediginiz kisayolun en basindaki  numarayi giriniz.  \nOrnek: [0] Save Icın '0'('q' bir ust menu): ")
        

        if(change == "q"):
            self.sf.clear()
            self.welcomeMenu()
            pass

        temp = int(change)
        change = temp
        selectedShorcut = None
        if (change == 0):
            selectedShorcut = "Save"
        elif (change == 1):
            selectedShorcut = "enTr"
        elif (change == 2):
            selectedShorcut = "trEn"
        elif (change == 3):
            selectedShorcut = "closeProgram"
        elif (change == 4):
            selectedShorcut = "translationType"
            
            newShorcut = int (input("{} icin yeni kisayol seciniz! \nEn->Tr Icın: {}\nTr->En Icın: {} -->".format(selectedShorcut, self.shorcut.getCustomShorcut()[1], self.shorcut.getCustomShorcut()[2])) )
            if (newShorcut == self.shorcut.getCustomShorcut()[1] or newShorcut == self.shorcut.getCustomShorcut()[2]):
                self.shorcut.updateShorcutData(selectedShorcut, newShorcut)
                self.sf.clear()
                print("{} icin yeni  kisayol  tusu {} olarak ayarlanmistir. ".format(selectedShorcut, newShorcut))
                self.changeShorcut()
                pass
            else:
                self.info.elseChanges()
                self.changeShorcut()
                pass
        else:
            self.info.elseChanges()   
            self.changeShorcut()
            pass
        newShorcut = int (input("{} icin yeni kisayol tusunu giriniz. Yeni kisayol sayi olmak zorundadir! -->".format(selectedShorcut)) )
        self.shorcut.updateShorcutData(selectedShorcut, newShorcut)
        self.sf.clear()
        print("[BILGI]: {} icin yeni  kisayol  tusu {} olarak ayarlanmistir. ".format(selectedShorcut, newShorcut))
        self.changeShorcut()

    def wordFunction(self):
        word = ""
        while 1:

            if (self.translationType == self.enTr):
                sourceLanguage = "en"
                destinationLanguage = "tr"
                word = input("[En] -> [Tr] Kelime: ")

            elif (self.translationType == self.trEn):
                sourceLanguage = "tr"
                destinationLanguage = "en"
                word = input("[Tr] -> [En] Kelime: ")

            pyperclip.copy(word)
            
            if (word == str(self.enTr)):
                self.translationType = self.enTr
            elif (word ==  str(self.trEn)):
                self.translationType = self.trEn
            elif (word == str(self.closeProgram)):
                self.sf.clear()
                self.welcomeMenu()
            else:
                word = word.lower()
                translationText = self.translator.translate(word,  src=sourceLanguage, dest=destinationLanguage).text
                print(translationText)

                write = input("Kaydet ? ({}): ".format(str(self.Save)))
                if(write == str(self.Save)):
                    db = databaseProcess(self.wordDbName)

                    if (self.translationType == self.enTr ):
                        if (not db.searchDataFromDatabase(self.tableName, "en", word)):
                            db.setWordDataToTable(self.tableName, (word, translationText))
                        else: 
                            print("[UYARI]: Bu kelime daha once kaydedilmistir! ")
                    else: 
                        if (not db.searchDataFromDatabase(self.tableName, "tr", word)):
                          db.setWordDataToTable(self.tableName, (translationText, word))
                        else: 
                            print("[UYARI]: Bu kelime daha once kaydedilmistir! ")
                       

