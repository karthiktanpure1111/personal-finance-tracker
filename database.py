import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL
)
""")

conn.commit()


def add_transaction_db(transaction_type, amount, category):

    cursor.execute(
        """
        INSERT INTO transactions
        (type, amount, category)
        VALUES (?, ?, ?)
        """,
        (
            transaction_type,
            amount,
            category
        )
    )

    conn.commit()


def get_transactions():

    cursor.execute(
        """
        SELECT * FROM transactions
        """
    )

    return cursor.fetchall()


def update_transaction(
    transaction_id,
    transaction_type,
    amount,
    category
):

    cursor.execute(
        """
        UPDATE transactions
        SET type=?, amount=?, category=?
        WHERE id=?
        """,
        (
            transaction_type,
            amount,
            category,
            transaction_id
        )
    )

    conn.commit()


def delete_transaction(
    transaction_id
):

    cursor.execute(
        """
        DELETE FROM transactions
        WHERE id=?
        """,
        (transaction_id,)
    )

    conn.commit()


def close_db():
    conn.close()