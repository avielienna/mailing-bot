import sqlite3
import logging

DB_FILE = "users.db"

def init_db():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY
                )
            ''')
        logging.info("База данных готова к работе.")
    except sqlite3.Error as e:
        logging.error(f"Ошибка при инициализации БД: {e}")

def add_user(user_id: int):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    except sqlite3.Error as e:
        logging.error(f"Ошибка добавления пользователя {user_id}: {e}")

def get_all_users() -> list[int]:
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM users')
            return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        logging.error(f"Ошибка получения списка пользователей: {e}")
        return []

def count_users() -> int:
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(user_id) FROM users')
            count = cursor.fetchone()[0]
            return count if count else 0
    except sqlite3.Error as e:
        logging.error(f"Ошибка при подсчете пользователей: {e}")
        return 0