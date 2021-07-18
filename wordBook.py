from libs import *

class wordBook():
        
    translator = Translator()
    shorcut = shorcut()

    wordDbName = "words.db"
    programDbName = "programDatabase.db"

    sourceLanguage = ""
    destinationLanguage = ""
    
    def __init__(self, tableName):
        self.tableName = tableName
        shorcutData = shorcut.getShorcut() 
     
        save = shorcutData[1] 
        enTr = shorcutData[2]
        trEn = shorcutData[3]
        closeProgram = shorcutData[4]
        lastWord =  shorcutData[5]
        translationType = enTr

    def getShorcut(self):
        self.shorcut.

    def changeShorcut(self):
        print("""Klavye Kısayolu Değiştirme Ekranına Hoşgeldiniz. Mevcut Kısayollarınız: """)
        print(self.getShorcut())

    # def wordFunction(self):
        
    #     if (self.translationType == self.enTr):
    #         sourceLanguage = "en"
    #         destinationLanguage = "tr"
    #         word = input("[En] -> [Tr] Kelime: ")

    #     elif (self.translationType == self.trEn):
    #         sourceLanguage = "tr"
    #         destinationLanguage = "en"
    #         word = input("[Tr] -> [En] Kelime: ")

    #     clipboard.copy(word)

    #     if (word == str(self.enTr)):
    #         translationType = self.enTr
    #     elif (word ==  str(self.trEn)):
    #         translationType = self.trEn
    #     elif (word == str(self.closeProgram)):
    #         exit()
    #     else:
    #         word = word.lower()

    #         translationText = self.translator.translate(word,  src=sourceLanguage, dest=destinationLanguage).text
    #         print(translationText)

    #         write = input("Yaz ? ({}): ".format())
    #         if(write == "1"):
    #             # buraya kayıt kodları yazılacak 
    #             pass


class shorcut():
    
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
        db.updateDataFromTable("shorcut", 1, "lastWord", self.getDefaultShorcut()[4])
    
    def updateShorcutData(self, columnName, newShorcut):
        db = databaseProcess(self.programDbName)
        db.updateDataFromTable(self.tableName, 1, columnName, newShorcut)

    @staticmethod
    def getDefaultShorcut():
        save = 1
        enTr = 2
        trEn = 3
        closeProgram = 0
        lastWord = 4
        return [save, enTr, trEn, closeProgram, lastWord]

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
    

a = wordBook("kelime")
