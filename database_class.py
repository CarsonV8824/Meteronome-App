import sqlite3

class Database():

    def __init__(self, db_name='meteronome_data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS metronome_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                piece TEXT NOT NULL,
                section TEXT NOT NULL,
                tempo INTEGER NOT NULL
            )
        ''')
        self.connection.commit()
    
    def add_entry(self, piece: str, section: str, tempo: int):
        self.cursor.execute('''
            INSERT INTO metronome_data (piece, section, tempo)
            VALUES (?, ?, ?)
        ''', (piece, section, tempo))
        self.connection.commit()

    def get_all_entries(self) -> list[tuple[str, str, str]]:
        self.cursor.execute('SELECT piece, section, tempo FROM metronome_data ORDER BY id')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def delete_all_entries(self):
        self.cursor.execute('DELETE FROM metronome_data')
        self.connection.commit()
