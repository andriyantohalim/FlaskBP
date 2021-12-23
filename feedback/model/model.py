import sqlite3
import os


def create_db():
    if not os.path.isfile("feedback.db"):
        conn = sqlite3.connect("feedback.db")
        conn.execute("CREATE TABLE feedback (email TEXT, comment TEXT)")
        conn.close()

