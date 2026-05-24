import sqlite3

# CONNECT DATABASE

conn = sqlite3.connect("users.db", check_same_thread=False)

cursor = conn.cursor()

# CREATE TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

conn.commit()

# ADD USER

def add_user(username, password):

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()

# LOGIN USER

def login_user(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    data = cursor.fetchone()

    return data