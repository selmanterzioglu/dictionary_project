from libs import *


class runWords():

    sf = specialFunction()
    info = info()

    def __init__(self, tableName):
        self.tableName = tableName

    def welcomeMenu(self):

        print("Kelime Calisma Modulune Hoşgeldiniz !")
        change = input("""
        Lütfen Aşağıdaki işlemlerden birisini  seçiniz: 
        0. Çıkış
        1. Rastgele Kelime Sor
        2. En fazla Hata yapilan kelimeleri calis
        3. Kelimelerin Hata Durumunu Sifirla
        --> """)

        self.sf.clear()

        if (change == "0"):
            exit()
        elif (change == "1"):
            self.enterWordlistNumber()
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

        else:
            self.info.elseChanges()  
            self.welcomeMenu() 
           