import sqlite3
import os


# Location of our database file
DATABASE_FOLDER = "data/database"
DATABASE_FILE = os.path.join(DATABASE_FOLDER, "retailvision.db")


def create_database():
    """Create the database and sessions table if they don't exist."""

    # Create the database folder if needed
    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    # Connect to SQLite
    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    # Create the sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time TEXT,
            end_time TEXT,
            attentive_time REAL,
            away_time REAL,
            attention_rate REAL
        )
    """)

    connection.commit()
    connection.close()


def save_session(
    start_time,
    end_time,
    attentive_time,
    away_time,
    attention_rate
):
    """Save one customer session to the database."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions (
            start_time,
            end_time,
            attentive_time,
            away_time,
            attention_rate
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        start_time,
        end_time,
        attentive_time,
        away_time,
        attention_rate
    ))

    connection.commit()
    connection.close()

