import sqlite3

DATABASE = "honeypot.db"

def create_database():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        username TEXT,
        password TEXT,
        timestamp TEXT,
        user_agent TEXT,
        risk_level TEXT,
        attack_type TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(ip, username, password, timestamp, user_agent, risk, attack_type):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attempts(ip_address, username, password, timestamp, user_agent)
    VALUES (?, ?, ?, ?, ?)
    """, (ip, username, password, timestamp, user_agent))

    conn.commit()
    conn.close()


def get_logs():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attempts")

    rows = cursor.fetchall()

    conn.close()

    return rows