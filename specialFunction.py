import os
import glob

class specialFunction():
    
    @staticmethod
    def getOsType():
        if (os.name == 'posix'):
            return "linux"
        elif (os.name == "nt"): 
            return "windows"
        else:
            return "[WARNING!]: isletim sistemi tespitinde hata! Lutfen root/library/specialFunctions.py/sf/getOsType metodunu Kontrol edin! "

    @staticmethod
    def clear():
        if(specialFunction.getOsType()  == "linux"):
            os.system("clear")
        elif (specialFunction.getOsType == "windows"):
            os.system("cls")
        
    @staticmethod
    def getFileList(path):
        return glob.glob(path)

    @staticmethod 
    def getFileListWithType(path, type):        
        data = glob.glob(path + type)
        return data


class info(specialFunction):

    def elseChanges(self):
        self.clear()
        print("[UYARI]: Lutfen belirtilen secenekler arasinda islem yapiniz! ") 
