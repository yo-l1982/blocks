## Mysql class

import MySQLdb

class mysql:
    cursor=0
    conn=0
    debug=0
    
    def __init__(self, host, user, password, db ):
        self.conn = MySQLdb.connect (host ,
        user,
        password,
        db)
        self.cursor = self.conn.cursor ()

    def __exit__(self):
        self.cursor.close()
        self.conn.close()

    def getVersion(self):
        self.cursor.execute ("SELECT VERSION()")
        row = self.cursor.fetchone ()
        return row[0]

    def query(self, q):
        if self.debug: print "Query: %s" % (q)
        self.cursor.execute(q)
        row = self.cursor.fetchone ()
        return row

    def queryAll(self, q):
        if self.debug: print "Query: %s" % (q)
        self.cursor.execute(q)
        row = self.cursor.fetchall()
        return row