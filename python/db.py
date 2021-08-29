import time

class Database:
    def __init__(self, con):
        self.con = con
        self.cur = con.cursor()
    
    def addUser(self, name: str, beacon: str):
        self.cur.execute("INSERT INTO User(name, beacon) VALUES (?, ?)", (name, beacon))
        self.con.commit()

    def findUserById(self, id: int):
        self.cur.execute("SELECT * FROM User WHERE id=?", (id, ))
        return self.cur.fetchone()

    def findUserByBeacon(self, beacon: str):
        self.cur.execute("SELECT * FROM User WHERE beacon=?", (beacon, ))
        return self.cur.fetchone()


    def addStore(self, name: str):
        self.cur.execute("INSERT INTO Store(name) VALUES (?)", (name, ))
        self.con.commit()

    def findStoreById(self, id: int):
        self.cur.execute("SELECT * FROM Store WHERE id=?", (id, ))
        return self.cur.fetchone()
    

    def addVisit(self, user_id: int, store_id: int):
        timestamp = time.time()

        self.cur.execute("INSERT INTO Visit(user, store, timestamp) VALUES (?, ?, ?)", (user_id, store_id, str(timestamp)))
        self.con.commit()

    def findAllVisit(self):
        self.cur.execute("SELECT * FROM Visit")
        return self.cur.fetchall()