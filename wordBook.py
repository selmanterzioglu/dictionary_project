from googletrans import Translator
import  clipboard
from databaseProcess import databaseProcess


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

    @staticmethod
    def getShorcut():
        db = databaseProcess("programDatabase.db")
        data = db.getAllDataFromTable("shorcut")
        return data

    @staticmethod
    def getShorcut(key):
        db = databaseProcess("programDatabase.db")
        # if(key != )
        data = db.getDataFromTableWithColumn("shorcut", key)
            


    @staticmethod
    def changeShorcut():
        print("""Klavye Kısayolu Değiştirme Ekranına Hoşgeldiniz.  Mevcut Kısayollarınız: """)
        print(wordBook.getShorcut())

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

            write = input("Yaz ? (1): ")
            if(write == "1"):
                # buraya kayıt kodları yazılacak 
                pass
