import sqlite3

# =========================================
# CONNECT DATABASE
# =========================================

conn = sqlite3.connect(
    "jobshield.db",
    check_same_thread=False
)

c = conn.cursor()

# =========================================
# INITIALIZE DATABASE
# =========================================

def init_db():

    c.execute("""

    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        job_text TEXT,

        result TEXT
    )

    """)

    conn.commit()

# =========================================
# INSERT PREDICTION
# =========================================

def insert_prediction(job_text, result):

    c.execute(
        """
        INSERT INTO predictions (
            job_text,
            result
        )

        VALUES (?, ?)
        """,

        (
            job_text,
            result
        )
    )

    conn.commit()

# =========================================
# FETCH ALL RECORDS
# =========================================

def fetch_all():

    c.execute(
        "SELECT * FROM predictions"
    )

    data = c.fetchall()

    return data