import sqlite3

def connect():
    return sqlite3.connect("voters.db")

def create_table():
    con = connect()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS voters(
        id INTEGER PRIMARY KEY,
        name TEXT,
        fingerprint TEXT,
        voted INTEGER DEFAULT 0
    )
    """)
    con.commit()
    con.close()

def add_voter(name, fingerprint):
    con = connect()
    cur = con.cursor()
    cur.execute("INSERT INTO voters(name, fingerprint) VALUES(?,?)",
                (name, fingerprint))
    con.commit()
    con.close()

def get_voters():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM voters")
    data = cur.fetchall()
    con.close()
    return data

def mark_voted(voter_id):
    con = connect()
    cur = con.cursor()
    cur.execute("UPDATE voters SET voted=1 WHERE id=?", (voter_id,))
    con.commit()
    con.close()
