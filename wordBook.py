from libs import *

class wordBook():
        
    translator = Translator()

    sourceLanguage = ""
    destinationLanguage = ""
    save = 1
    enTr = 2
    trEn = 3
    closeProgram = 0
    lastWord = 4
    translationType = enTr ## 2 oldugunda [En] -> [Tr] ----  3 oldugunda [Tr] -> [En]
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName


    @staticmethod
    def getShorcut():
        db = databaseProcess("programDatabase.db")
        data = db.getAllDataFromTable("shorcut")
        return data

    @staticmethod
    def getShorcut(id):
        db = databaseProcess("programDatabase.db")
        # if(key != )
        data = db.getDataFromTableWithId("shorcut", id)
            
    

    @staticmethod
    def changeShorcut():
        print("""Klavye Kısayolu Değiştirme Ekranına Hoşgeldiniz.  Mevcut Kısayollarınız: """)
        print(wordBook.getShorcut(1))

    def wordFunction(self):
        
        if (self.translationType == self.enTr):
            sourceLanguage = "en"
            destinationLanguage = "tr"
            word = input("[En] -> [Tr] Kelime: ")

        elif (self.translationType == self.trEn):
            sourceLanguage = "tr"
            destinationLanguage = "en"
            word = input("[Tr] -> [En] Kelime: ")

        clipboard.copy(word)

        if (word == str(self.enTr)):
            translationType = self.enTr
        elif (word ==  str(self.trEn)):
            translationType = self.trEn
        elif (word == str(self.closeProgram)):
            exit()
        else:
            word = word.lower()

            translationText = self.translator.translate(word,  src=sourceLanguage, dest=destinationLanguage).text
            print(translationText)

            write = input("Yaz ? ({}): ".format())
            if(write == "1"):
                # buraya kayıt kodları yazılacak 
                pass


a  = wordBook("de", "sdf")
x = a.getShorcut(1)

print(x)

