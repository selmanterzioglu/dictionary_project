import sqlite3

class databaseProcess():
    
    def __init__(self, databaseName):
        self.dbName = databaseName

    def setWordDataToTable(self, tableName, data):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        im.execute("""INSERT INTO {} VALUES (null, ?, ?, 0, 0)""".format(tableName), data)
        db.commit()
        db.close()

    def searchDataFromDatabase(self,tableName, columnName, data):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        im.execute("""SELECT * FROM {} WHERE {} = '{}'""".format(tableName, columnName, data))
        returnData = im.fetchall()
        db.close()
        return returnData

    def setShorcutDataToTable(self, tableName, data):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        im.execute("""INSERT INTO {} VALUES (null, ?, ?, ?, ?, ? )""".format(tableName), data)
        db.commit()
        db.close()

    def createTableToDatabase(self, newTableName):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS {} ("id" INTEGER NOT NULL, "en" TEXT NOT NULL, "tr" INTEGER NOT NULL, "mistake" INTEGER, "correct" INTEGER, PRIMARY KEY("id" AUTOINCREMENT))""".format(newTableName) )
        db.close()

    def updateDataFromTable(self, tableName, id, columnName, data):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql  = """UPDATE {} SET {} = '{}' WHERE id = {}""".format(tableName, columnName, data, id)
        im.execute(sql)
        db.commit()
        db.close()
    
    def getDataFromTable(self, tableName):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = """SELECT * FROM {} """.format(tableName)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data

    def getDataFromTableWithId(self, tableName, id):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = """SELECT * FROM {} WHERE id = {}""".format(tableName, id)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data

    def getDataFromTableColumn(self, tableName, id, columnName):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = """SELECT {} FROM {} WHERE id = {}""".format(columnName, tableName, id)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data
    
    def deleteTable(self, tableName):
        tableList = self.listTableName()

        control = False
        for i in tableList:
            if (i == tableName):
                db = sqlite3.connect(self.dbName)
                im = db.cursor()
                sql = """DROP TABLE {}""".format(tableName)    
                im.execute(sql)
                db.close()
                control = True

        return control

    def listTableName(self):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = """SELECT name FROM sqlite_master"""
        im.execute(sql)
        data = im.fetchall()
        db.close()
        list = [item[0] for item in data]
        return list
    
    def getLineCountFromTable(self, tableName):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = """SELECT COUNT(*) FROM {}""".format(tableName)
        im.execute(sql)
        data = im.fetchone()[0]
        db.close()
        return data

    def getLineCountFromtableWithColumn(self, tableName, columnName):
            db = sqlite3.connect(self.dbName)
            im = db.cursor()
            sql = """SELECT COUNT({}) FROM {}""".format(columnName, tableName)
            im.execute(sql)
            data = im.fetchone()[0]
            db.close()
            return data

    def setDataAllColumnsFromTable(self, tableName, columnName):
        db = sqlite3.connect(self.dbName)
        im = db.cursor()
        sql = "UPDATE {} SET {}= 0".format(tableName, columnName)
        im.execute(sql)
        db.commit()
        db.close()
        

if __name__ == "__main__":

    a = databaseProcess("words.db")
    x = a.getDataFromTable("kelime")[0][1]
    print(x)
