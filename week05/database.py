import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    # Create table with a "class" column (will only apply on first run)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            "class" TEXT NOT NULL
        )
    """)
    # If the table already existed without the "class" column, add it:
    try:
        cursor.execute('ALTER TABLE users ADD COLUMN "class" TEXT NOT NULL DEFAULT "A"')
    except sqlite3.OperationalError:
        # column already exists, ignore
        pass
    conn.commit()
    conn.close()
