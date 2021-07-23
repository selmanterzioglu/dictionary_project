from libs import *

class shorcutClass():
    
    programDbName = "programDatabase.db"

    def __init__(self):
        db = sqlite3.connect(self.programDbName)
        im = db.cursor()
        
        pass


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
    
class wordBook():
        
    translator = Translator()
    shorcut = shorcutClass()
    info = info()
    sf = specialFunction()

    wordDbName = "words.db"
    programDbName = "programDatabase.db"

    sourceLanguage = ""
    destinationLanguage = ""
    
    def __init__(self, tableName):
        self.tableName = tableName
        
    def getShorcut(self):
        shorcutData = self.shorcut.getCustomShorcut()
        save = shorcutData[0] 
        enTr = shorcutData[1]
        trEn = shorcutData[2]
        closeProgram = shorcutData[3]
        lastWord =  shorcutData[4]

        return [save, enTr, trEn, closeProgram, lastWord]

    def welcomeMenu(self):
        print("Kelime Kaydetme Modulune Hosgeldiniz.!")
        
        pass

    def changeShorcut(self):
        print("""Klavye Kısayolu Değiştirme Ekranına Hoşgeldiniz. Mevcut Kısayollarınız: """)
        print("[0]Save: {}\n[1]En->Tr: {}\n[2]Tr->En: {}\n[3]Close Program: {}\n[4]Last Word: {}"
        .format(self.getShorcut()[0], self.getShorcut()[1], self.getShorcut()[2], self.getShorcut()[3], self.getShorcut()[4]) )
        change = input("\n\n Lutfen degistirmek istediginiz kisayolun en basindaki  numarayi giriniz.  \nOrnek: [0] Save Icın '0'('q' bir ust menu): ")
        

        if (change != "q" or change == "0" or  change != "1" or change != "2" or change != "3" or change != "4"):
            info.elseChanges()   
            self.changeShorcut()
            pass
        elif(change == "q"):
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
            selectedShorcut = "lastWord"

        newShorcut = int (input("{} icin yeni kisayol tusunu giriniz. Yeni kisayol sayi olmak zorundadir! -->".format(selectedShorcut)) )
        self.shorcut.updateShorcutData(selectedShorcut, newShorcut)
        self.sf.clear()
        print("{} icin yeni  kisayol  tusu {} olarak ayarlanmistir. ".format(selectedShorcut, newShorcut))
        self.changeShorcut()


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


a = wordBook("kelime")
