import os
import glob

class sf():
    
    @staticmethod
    def getOsType():
        if (os.name == 'posix'):
            return "linux"
        elif (os.name == "nt"): 
            return "windows"
        else:
            return "[WARNING!]: isletim sistemi tespitinde hata! Lutfen root/lib/specialFunctions.py/sf/getOsType metodunu Kontrol edin! "

    @staticmethod
    def clear():
        if(sf.getOsType()  == "linux"):
            os.system("clear")
        elif (sf.getOsType == "windows"):
            os.system("cls")
        
    @staticmethod
    def getFileList(path):
        return glob.glob(path)

    @staticmethod 
    def getFileListWithType(path, type):        
        data = glob.glob(path + type)
        return data