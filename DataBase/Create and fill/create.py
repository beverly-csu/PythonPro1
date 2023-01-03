import sqlite3

DB_NAME = 'quiz.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    