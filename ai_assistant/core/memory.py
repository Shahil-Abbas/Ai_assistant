import sqlite3

conn = sqlite3.connect("database/assistant.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT
    )
    """
)

conn.commit()

def save_note(note):
    cursor.execute(
        "INSERT INTO notes(note) VALUES(?)",
        (note,)
    )

    conn.commit()


def get_notes():
    cursor.execute("SELECT note FROM notes")

    return cursor.fetchall()