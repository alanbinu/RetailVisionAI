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


def get_average_attentive_time():
    """Return the average attentive time across all sessions."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT AVG(attentive_time) FROM sessions")

    average_time = cursor.fetchone()[0]

    connection.close()

    if average_time is None:
        return 0

    return average_time


def get_average_away_time():
    """Return the average looking away time across all sessions."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT AVG(away_time) FROM sessions")

    average_time = cursor.fetchone()[0]

    connection.close()

    if average_time is None:
        return 0

    return average_time

def get_highest_attention_rate():
    """Return the highest attention rate recorded."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT MAX(attention_rate) FROM sessions")

    highest_rate = cursor.fetchone()[0]

    connection.close()

    if highest_rate is None:
        return 0

    return highest_rate


def get_lowest_attention_rate():
    """Return the lowest attention rate recorded."""

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("SELECT MIN(attention_rate) FROM sessions")

    lowest_rate = cursor.fetchone()[0]

    connection.close()

    if lowest_rate is None:
        return 0

    return lowest_rate

if __name__ == "__main__":

    total_sessions = get_session_count()
    average_rate = get_average_attention_rate()
    average_attentive = get_average_attentive_time()
    average_away = get_average_away_time()
    highest_rate = get_highest_attention_rate()
    lowest_rate = get_lowest_attention_rate()

    print()
    print("===================================")
    print("       RetailVisionAI Analytics")
    print("===================================")

    print(f"Total Sessions: {total_sessions}")
    print(f"Average Attention Rate: {average_rate:.1f}%")
    print(f"Average Attentive Time: {average_attentive:.1f} seconds")
    print(f"Average Looking Away Time: {average_away:.1f} seconds")
    print(f"Highest Attention Rate: {highest_rate:.1f}%")
    print(f"Lowest Attention Rate: {lowest_rate:.1f}%")

    print("===================================")