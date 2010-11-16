
import sqlite3

dbConn = sqlite3.connect('./db')
cursor = dbConn.cursor()
cursor.execute('''create table blocks(x integer, y integer, z integer, type integer)''')



for x in range(0, 50):
    for y in range(0, 50):
        for z in range(0, 2):
            
            print "requesting data"
            data = cursor.execute("""insert into blocks(x,y,z,type) values (?,?,?,?)""", (x,y,z,1))

dbConn.commit()