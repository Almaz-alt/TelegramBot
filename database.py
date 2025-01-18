import sqlite3


class database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect("db.sqlite") as conn:
                cursor = conn.cursor()
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS           
                    complaints(
                    id INTEGER PRIMARY KEY 
                    AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    complaint TEXT, 
                    )            
                """)