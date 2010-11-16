## This class is responsible for loading the world from remote sql server
import sqlite3
class clientConnection:
    dbConn = 0

    def __init__(self):
        self.dbConn = sqlite3.connect('../data/db')

    def requestData(self):
        cursor = self.dbConn.cursor()
        print "requesting data"
        cursor.execute("SELECT x,y,z,type FROM blocks;")
        self.dbConn.commit()
        return cursor.fetchall()
