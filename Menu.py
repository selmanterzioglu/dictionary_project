from libs import *
from wordBook import *
from runWords import *

class menu():

    sf = specialFunction()    
    info = info()
    wordDbName = "words.db"
    shorcut = shorcutClass()


    def welcomeMenu(self):

        print("Kelime Uygulamasına Hoşgeldiniz !")
        change = input("""
        Lütfen Aşağıdaki işlemlerden birisini  seçiniz: 
        0. Çıkış
        1. Kelime Kaydetmeye Başla
        2. Kelime Çalış
        3. Kelime Listelerini Göster
        4. Kelime Listesi Olustur
        5. Kelime Listesi Sil 
        --> """)

        self.sf.clear()

        if (change == "0"):
            exit()
        elif (change == "1"):
            self.wordBook()
        elif (change == "2"):
            pass
        elif (change == "3"):
            self.showWordList()
            wordListName = input("\n\n('q' bir ust menu): -->")
            if (wordListName != "q"):
                self.info.elseChanges()
                self.showWordList()
                pass
            
            self.sf.clear()
            self.welcomeMenu()

        elif (change == "4"):
            self.createWordList()
        elif (change == "5"):
            self.deleteWordList()
        else:
            self.info.elseChanges()  
            self.welcomeMenu() 
               
    def saveWordList(self):
        db = databaseProcess(self.wordDbName)
        wordList = db.listTableName()
        if (len(wordList == 1)):
            self.sf.clear()
            print("[UYARI]: Veritabanınızda kelime ekleyebileceginiz  liste yok! Lütfen liste ekleyiniz.")
            self.welcomeMenu()
        
        self.showWordList()
        change = input("""
        Lütfen yeni kelimelerinizi eklemek istediginiz listenizi seciniz: 
        0. Bir Ust Menu
        --> """)
        if change == "0":
            self.sf.clear()
            self.welcomeMenu()
        temp = int(change)
        change = temp 

        if (change >= len(wordList) or  change <= 0 ):
            self.sf.clear()
            print("[HATA]: Girdiginiz deger herhangi  bir listeye ait degil")
            self.showWordList()
    def runWordBook(self):
        wordList = self.showWordList()
        wordListName = input("\n\nLutfen uzerine yazmak istediginiz liste numarasini girin ('q' bir ust menu): ")
    
        if(wordListName == "q"):
            self.sf.clear()
            self.welcomeMenu()
            pass

        temp = int(wordListName)
        wordListNumber = temp 

        if (wordListNumber >= len(wordList) or  wordListNumber <= 0 ):
            self.sf.clear()
            print("[HATA]: Girdiginiz deger herhangi  bir listeye ait degil")
            self.runWordBook()
            pass

        wb = WordBook(wordList[wordListNumber])
    def runWords(self):
        wordList = self.showWordList()
        wordListName = input("\n\nLutfen kelimelerini calismak istediginiz listenin numarasini  girin ('q' bir ust menu): ")
    
        if(wordListName == "q"):
            self.sf.clear()
            self.welcomeMenu()
            pass

        temp = int(wordListName)
        wordListNumber = temp 

        if (wordListNumber >= len(wordList) or  wordListNumber <= 0 ):
            self.sf.clear()
            print("[HATA]: Girdiginiz deger herhangi  bir listeye ait degil")
            self.runWordBook()
            pass
        else:
            rw = runWords(wordList[wordListNumber])

    def showWordList(self):
        db = databaseProcess(self.wordDbName)
        wordList = db.listTableName()
        numberWordlist = len(wordList) -1

        
        if (numberWordlist == 0):
            print("[UYARI]: Veritabanınızda kelime ekleyebileceginiz  liste yok! Lütfen liste ekleyiniz.")
            pass
        else:
            maxWordTableNameLength = 2
            maxWordTableLength = 21
            
            for i in range(1, (numberWordlist + 1)):
                
                if (len (wordList[i]) >= maxWordTableNameLength):
                    maxWordTableNameLength = len (wordList[i])
                if (db.getLineCountFromTable(wordList[i]) >= maxWordTableLength):
                    maxWordTableLength = db.getLineCountFromTable(wordList[i])
            
            print("Veritabanında {} adet liste mevcut. Mevcut Kelime Listeleriniz: ".format(numberWordlist))
            print("\n*************************************")
            print(f"{'No': <{len(str(numberWordlist)) + 2}} {'Ad': <{maxWordTableNameLength}}  {'Kayitli Kelime Sayisi': <{maxWordTableLength}}")
            for i in range(1,(numberWordlist+1)):
                tableNumber = "[{}]".format(i)
                tableName = wordList[i]
                tableWordCount = str (db.getLineCountFromTable(wordList[i]))
                print(f"{tableNumber: <{i}} {tableName: <{maxWordTableNameLength}} {tableWordCount: ^{maxWordTableLength}}")

                # print(tableName.ljust(maxWordTableNameLength) + tableWordCount.center(maxWordTableLength))
                # print(tableName.ljust(maxWordTableNameLength) + tableWordCount.rjust(10))
            print("*************************************\n")

        return wordList

    def createWordList(self):
        self.showWordList()
        wordListName = input("\n\nLutfen yeni  olusturmak istediginiz liste ismini girin ('q' bir ust menu): ")
        
        if(wordListName == "q"):
            self.sf.clear()
            self.welcomeMenu()
            pass

        db = databaseProcess(self.wordDbName)
        wordList = db.listTableName()

        control = False
        for i in range(len(wordList)):
            if(wordListName ==  wordList[i]):
                control = True

        if control == False:
            db.createTableToDatabase(wordListName)
            self.sf.clear()
            print("[BILGI]: {} adli kelime listesi basariyla olusturulmustur.\n".format(wordListName))
            self.createWordList()
            pass
        else:
            self.sf.clear()
            print("[HATA]: Bu liste ismi veritabanında  mevcuttur. Lutfen baska bir isim girin. ")
            self.createWordList()
    
    def deleteWordList(self):
        wordList = self.showWordList()
        change = input("Lufen silmek istediginiz listenin numarasini giriniz: ('q' bir ust menu):")
        
        if(change == "q"):
            self.sf.clear()
            self.welcomeMenu()
            pass
        elif (change.isalpha()):
            self.info.elseChanges()
            self.deleteWordList()
            pass
        
        temp = int(change)
        change = temp
        

        if (change >= len(wordList) or  change <= 0 ):
            self.sf.clear()
            print("[HATA]: Girdiginiz deger herhangi  bir listeye ait degil")
            self.deleteWordList()
            pass
        
        db = databaseProcess(self.wordDbName)
        wordCounter = db.getLineCountFromTable(wordList[change])

        deleteChange = input("{} adli kelime listenizde {} adet kelime kaydi mevcut.\nSilmek istediginize emin misiniz?\n(E/H)-->".format(wordList[change], wordCounter))
        if(deleteChange == "e" or deleteChange == "E"):
            db = databaseProcess(self.wordDbName)
            db.deleteTable(wordList[change])        
            self.sf.clear()
            print("[BILGI]: {} adli liste basariyla silindi.! ".format(wordList[change]))
            self.deleteWordList()
        else:
            self.sf.clear()
            print("[BILGI]: {} adli listenin silme islemi iptal edildi.! ".format(wordList[change]))
            self.deleteWordList()

if (__name__ == '__main__'):
    menu = menu()
    menu.welcomeMenu()