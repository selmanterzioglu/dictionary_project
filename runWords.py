from libs import *
import random

class runWords():

    sf = specialFunction()
    info = info()

    wordDbName = "words.db"
    programDbName = "programDatabase.db"

    def __init__(self, tableName):
        self.tableName = tableName
        self.welcomeMenu()


    def welcomeMenu(self):

        change = input("""
        Kelime Calisma Modulune Hoşgeldiniz !
    
        Lütfen Aşağıdaki işlemlerden birisini  seçiniz: 
        ****************************************************
            0. Çıkış
            1. Rastgele Kelime Calis
            2. [BETA!] En fazla Hata yapilan kelimeleri calis
            3. Kelimelerin Hata Durumunu Sifirla
        ****************************************************
        --> """)

        self.sf.clear()

        if (change == "0"):
            exit()
        elif (change == "1"):
            self.workWords(False)
        elif (change == "2"):
            self.sf.clear()
            print("[BILGI]: Bu ozellik gelistirilme asamasindadir...!")
            self.welcomeMenu()

        elif (change == "3"):
            self.deleteMistakeFromWordList()
        else:
            self.info.elseChanges()  
            self.welcomeMenu() 
        
    def deleteMistakeFromWordList(self):

        change = input("{} adli listenin hata durumunu sifrlamak istiyor musunuz ?(E/H)".format(self.tableName))
        self.sf.clear()
        if(change == "e" or change == "E"):
            db = databaseProcess(self.wordDbName)
            db.setDataAllColumnsFromTable(self.tableName, "mistake")
            db.setDataAllColumnsFromTable(self.tableName, "correct")
            print("[BILGI]: {} adli listenizin hata durumlari basariyla sifirlandi !".format(self.tableName))
            self.welcomeMenu()
        else:
            print("[BILGI]: Islem iptal edildi !".format(self.tableName))
            self.welcomeMenu()

    def workWords(self, state):
        translateTypeChange = input("[1] En-->Tr\n[2] Tr-->En\n[3] Bir ust Menu\n-->")
        self.sf.clear()

        if (translateTypeChange != "1" and translateTypeChange != "2" and translateTypeChange != "3"):
            self.info.elseChanges()
            self.workWords(state)
            pass

        db = databaseProcess(self.wordDbName)
        lineCounter = db.getLineCountFromTable(self.tableName)

        if (state):
            mistake = [0] * lineCounter
            correct = [0] * lineCounter
            idList =  [0] * lineCounter
            mistakeStatement =  [0] * lineCounter
            mistakeStatementList =  [0] * lineCounter

            for i in range(lineCounter):
                idList[i]  = db.getDataFromTable(self.tableName)[i][0] 
                mistake[i] = db.getDataFromTable(self.tableName)[i][3]
                correct[i] = db.getDataFromTable(self.tableName)[i][4]
                mistakeStatement[i] = mistake[i] - correct[i]

            maxMistake = mistakeStatement[0]

            for i in range(lineCounter):
                if (maxMistake >= mistakeStatement[i]):
                    if (translateTypeChange == "1"):
                        questionWord = db.getDataFromTableWithId(self.tableName, idList[i])[0][1]
                        answerWord = db.getDataFromTableWithId(self.tableName, idList[i])[0][2]

                    else:
                        questionWord = db.getDataFromTableWithId(self.tableName, idList[i])[0][2]
                        answerWord = db.getDataFromTableWithId(self.tableName, idList[i])[0][1]
                    
                    inputWord = input("{} ('q' Cevabi Goster)-->".format(questionWord))
                    if(inputWord == "q"):
                        print("{}-->{}".format(questionWord, answerWord))
                    else: 

                        while(inputWord != answerWord):
                            inputWord = input("{}-->".format(questionWord))

        else:
            enWords = [None] * lineCounter
            trWords = [None] * lineCounter
            correct = [0] * lineCounter

            data = db.getDataFromTable(self.tableName)
            
            for i in range (lineCounter):
                enWords[i] = data[i][1]
                trWords[i] = data[i][2]
            
            while 1:
                counter = 0
                for i in correct:
                    if i == 1:
                        counter += 1
                
                if(counter == lineCounter):
                    self.sf.clear()
                    print("[BILGI]:{} adli listede bulunan {} adet kelimenin tamamini calistiniz ".format(self.tableName, lineCounter))
                    self.welcomeMenu()
                    break

                while(1):
                    rand = random.randrange(0,lineCounter)
                    if (correct[rand] == 0):
                        break

                if (translateTypeChange == "1"):
                    questionWord = enWords[rand]
                    answerWord = trWords[rand]

                elif (translateTypeChange == "2"):
                    questionWord = trWords[rand]
                    answerWord = enWords[rand]
                    
                while(1):
                    inputWord = input("{}-->".format(questionWord))
                    inputWord = inputWord.lower()
                    if(inputWord == "q"):
                        print("{}-->{}".format(questionWord, answerWord))
                        break

                    elif (inputWord == answerWord):
                        correct[rand] = 1
                        self.sf.clear()
                        break

