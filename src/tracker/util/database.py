import sqlite3
import os
from generated.enums.killers import Killer
from generated.enums.survivors import Survivor
from generated.enums.maps import Map
from tracker.data.victory import Victory
from tracker.data.pips import Pips
from datetime import datetime
DATABASE_PATH = "games.db"



class Database(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            needs_setup = not os.path.isfile(DATABASE_PATH)
            cls.conn = sqlite3.connect(DATABASE_PATH)
            if needs_setup:
                cls.db_init(cls)
        return cls._instance

    def db_init(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY, 
            survivor INTEGER, 
            killer INTEGER, 
            mapvariation INTEGER,
            victory INTEGER,
            pip INTEGER,
            time TEXT
        );""")
        self.conn.commit()

    def write(self, entry):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO games (
            survivor, 
            killer, 
            mapvariation,
            victory,
            pip,
            time
        ) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        );""", (entry.survivor.value, entry.killer.value, entry.mapvariation.value, entry.victory.value, entry.pip.value, str(datetime.utcnow())[:16]))
        self.conn.commit()

    def apply_survivor_filter(self, survivor):
        self.survivor_filter = survivor
        
    def get_all_filter(self):
        filter = ""
        params = []
        if self.survivor_filter:
            filter += " survivor=?"
            params += [self.survivor_filter.value]
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM games WHERE" + filter, tuple(params))
        self.conn.commit()
        return map(lambda x: (Survivor(x[1]), Killer(x[2]), Map(x[3]), Victory(x[4])), cursor.fetchall())

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM games")
        self.conn.commit()
        return map(lambda x: (Survivor(x[1]), Killer(x[2]), Map(x[3]), Victory(x[4]), Pips(x[5]), x[6]), cursor.fetchall())