import sqlite3
import hashlib

# =========================================
# CONNECT DATABASE
# =========================================

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

c = conn.cursor()

# =========================================
# CREATE USERS TABLE
# =========================================

c.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password TEXT
)
""")

conn.commit()

# =========================================
# HASH PASSWORD
# =========================================

def make_hash(password):

    return hashlib.sha256(
        str.encode(password)
    ).hexdigest()

# =========================================
# ADD USER
# =========================================

def add_user(username, password):

    # Check if username already exists
    c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    existing_user = c.fetchone()

    if existing_user:

        return False

    # Insert new user
    c.execute(
        "INSERT INTO users(username, password) VALUES (?, ?)",
        (
            username,
            make_hash(password)
        )
    )

    conn.commit()

    return True

# =========================================
# LOGIN USER
# =========================================

def login_user(username, password):

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (
            username,
            make_hash(password)
        )
    )

    data = c.fetchone()

    if data:

        return True

    return False