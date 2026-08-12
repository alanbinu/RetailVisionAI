import sqlite3


DATABASE_FILE = "data/database/retailvision.db"


def get_session_count():
    """Return the total number of customer sessions."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM sessions")

    session_count = cursor.fetchone()[0]

    connection.close()

    return session_count


def get_average_attention_rate():
    """Return the average attention rate across all sessions."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT AVG(attention_rate) FROM sessions")

    average_rate = cursor.fetchone()[0]

    connection.close()

    if average_rate is None:
        return 0

    return average_rate

if __name__ == "__main__":

    total_sessions = get_session_count()
    average_rate = get_average_attention_rate()

    print("RetailVisionAI Analytics")
    print("------------------------")
    print(f"Total Sessions: {total_sessions}")
    print(f"Average Attention Rate: {average_rate:.1f}%")