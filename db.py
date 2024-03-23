import sqlite3

import streamlit
import pandas as pd

from UserDetail import UserDetail


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('./db.sqlite')
        self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_detail (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob DATE,
                city TEXT
            )
        ''')
        self.conn.commit()
        c.close()

    def insert_user_detail(self, userDetail):
        c = self.conn.cursor()
        c.execute('''
                    INSERT INTO user_detail (name, dob, city) VALUES (?, ?, ?)
                ''', (userDetail.name, userDetail.dob, userDetail.city))
        self.conn.commit()
        user_id = c.lastrowid
        c.close()
        return user_id

    def get_user_detail(self, user_id):
        c = self.conn.cursor()
        c.execute('''
                        SELECT * FROM user_detail WHERE id = ?
                ''', user_id)
        user_detail = self.fetch_data_and_map_to_objects(c)
        c.close()
        return user_detail

    def fetch_data_and_map_to_objects(self, cursor):
        row = cursor.fetchone()

        name = row[1]
        dob = row[2]
        city = row[3]

        obj = UserDetail(name, dob, city)

        return obj
