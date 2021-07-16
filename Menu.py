from databaseProcess import databaseProcess
import libs

class Menu():
    

    def welcomeMenu(self):
        
        print("Kelime Uygulamasına Hoşgeldiniz !")
        change = input("""
        Lütfen Aşağıdaki işlemlerden birisini  seçiniz: 
        0. Çıkış
        1. Kelime Kaydetmeye Başla
        2. Kelime Çalış
        3. Kelime Databaselerini göster """)

        if (change == 0):
            exit()
        elif (change == 1):
            pass
        elif (change == 2):
            pass
        elif (change == 3):
            pass
    
    