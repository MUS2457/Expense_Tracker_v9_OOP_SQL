import sqlite3

def create_connection(db_file="expenses.db"):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        category TEXT,
        amount REAL NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()


def insert_into_table(conn, expenses):
    cursor = conn.cursor()

    for expense in expenses:
        cursor.execute("""
        INSERT INTO expenses (product, category, amount)
        VALUES (?, ?, ?)
        """, (expense.product, expense.category, expense.amount))

    conn.commit()