import sqlite3

class PhotoDatabase:
    
    def __init__(self, file='photo_database.sqlite3'):
        self.connection = sqlite3.Connection(file)
        self.cursor = self.connection.cursor()
        self.__make_table()

    def __make_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SHEET_MUSIC(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Photos BLOB
            );
        """)
        self.connection.commit()

    def add_data(self, Photos):
        self.cursor.execute("""
            INSERT INTO SHEET_MUSIC (Photos) 
            VALUES (?)""", (Photos,))  # Note the comma
        self.connection.commit()
        
    def get_data(self):
        self.cursor.execute("""
        SELECT * FROM SHEET_MUSIC
        """)
        return self.cursor.fetchall()  # Add parentheses
    
    def clear_data(self):
        self.cursor.execute("""
            DELETE FROM SHEET_MUSIC
        """)
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()