import sqlite3

DB_PATH = "data/results.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def store_result(chunk, score):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO results (chunk, score) VALUES (?, ?)", (chunk, score))
    conn.commit()
    conn.close()
import sqlite3

DB_PATH = "data/results.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def store_result(chunk, score):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO results (chunk, score) VALUES (?, ?)", (chunk, score))
    conn.commit()
    conn.close()
