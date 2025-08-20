import sqlite3

def connect():
    return sqlite3.connect("data.db")

def create_tables():
    conn = connect()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            meaning TEXT,
            difficulty INTEGER DEFAULT 1
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student TEXT,
            word_id INTEGER,
            correct INTEGER
        )
    """)
    conn.commit()
    conn.close()
