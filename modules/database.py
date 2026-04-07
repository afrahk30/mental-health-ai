import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("data/mood_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mood
                 (text TEXT, sentiment TEXT, score REAL, emotion TEXT, insight TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def insert_entry(text, sentiment, score, emotion, insight):
    conn = sqlite3.connect("data/mood_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO mood (text, sentiment, score, emotion, insight) VALUES (?, ?, ?, ?, ?)",
              (text, sentiment, score, emotion, insight))
    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect("data/mood_data.db")
    df = pd.read_sql_query("SELECT * FROM mood", conn)
    conn.close()
    return df