import sqlite3

class databaseProcess():
    
    def __init__(self, database_name):
        self.database_name = database_name

    def setWordDataToTable(self, table_name, data):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        data_str = ""
        for i in data: 
            data_str +=", \"" +i + "\""

        if(len(data) == 2):
            im.execute("""INSERT INTO {} VALUES (null {}, null, null, null, null)""".format(table_name, data_str))
        elif(len(data) == 3):
            im.execute("""INSERT INTO {} VALUES (null {}, null, null, null)""".format(table_name, data_str))
        elif(len(data) == 4):
            im.execute("""INSERT INTO {} VALUES (null {}, null, null)""".format(table_name, data_str))
        elif(len(data) == 5):
            im.execute("""INSERT INTO {} VALUES (null {}, null)""".format(table_name, data_str))
        elif(len(data) == 6):
            im.execute("""INSERT INTO {} VALUES (null {})""".format(table_name, data_str))

        db.commit()
        db.close()

    def searchDataFromDatabase(self,table_name, column_name, data):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        im.execute("""SELECT * FROM {} WHERE {} = '{}'""".format(table_name, column_name, data))
        returnData = im.fetchall()
        db.close()
        return returnData

    def delete_row(self, table_name, id):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        im.execute("""DELETE FROM {} WHERE ID = {}""".format(table_name, id))
        db.commit()
        db.close()

    def createTableToDatabase(self, newtable_name):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()

        im.execute("""
        CREATE TABLE IF NOT EXISTS {} 
        ("id" INTEGER NOT NULL, "en" TEXT NOT NULL, "tr" TEXT NOT NULL,
        "ex_1" TEXT, 
        "ex_2" TEXT,
        "ex_3" TEXT,
        "ex_4" TEXT,
        PRIMARY KEY("id" AUTOINCREMENT))""".format(newtable_name) )
        
        db.close()

    def updateDataFromTable(self, table_name, id, column_name, data):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql  = """UPDATE {} SET {} = '{}' WHERE id = {}""".format(table_name, column_name, data, id)
        im.execute(sql)
        db.commit()
        db.close()
    
    def getDataFromTable(self, table_name):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = """SELECT * FROM {} """.format(table_name)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data

    def getDataFromTableWithId(self, table_name, id):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = """SELECT * FROM {} WHERE id = {}""".format(table_name, id)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data

    def getDataFromTableColumn(self, table_name, id, column_name):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = """SELECT {} FROM {} WHERE id = {}""".format(column_name, table_name, id)
        im.execute(sql)
        data = im.fetchall()
        db.close()
        return data
    
    def deleteTable(self, table_name):
        tableList = self.listtable_name()

        control = False
        for i in tableList:
            if (i == table_name):
                db = sqlite3.connect(self.database_name)
                im = db.cursor()
                sql = """DROP TABLE {}""".format(table_name)    
                im.execute(sql)
                db.close()
                control = True

        return control

    def list_table_name(self):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = """SELECT name FROM sqlite_master"""
        im.execute(sql)
        data = im.fetchall()
        db.close()
        list = [item[0] for item in data]
        list.pop(0)
        return list
    
    def getLineCountFromTable(self, table_name):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = """SELECT COUNT(*) FROM {}""".format(table_name)
        im.execute(sql)
        data = im.fetchone()[0]
        db.close()
        return data

    def getLineCountFromtableWithColumn(self, table_name, column_name):
            db = sqlite3.connect(self.database_name)
            im = db.cursor()
            sql = """SELECT COUNT({}) FROM {}""".format(column_name, table_name)
            im.execute(sql)
            data = im.fetchone()[0]
            db.close()
            return data

    def setDataAllColumnsFromTable(self, table_name, column_name):
        db = sqlite3.connect(self.database_name)
        im = db.cursor()
        sql = "UPDATE {} SET {}= 0".format(table_name, column_name)
        im.execute(sql)
        db.commit()
        db.close()
        
