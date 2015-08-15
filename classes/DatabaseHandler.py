import sqlite3
import sys


class DatabaseHandler:
    def __init__(self):
        self.db_name = sys.path[0] + "/temp_db.db"
        self.create_database()

    def create_database(self):
        connection = sqlite3.connect(self.db_name)
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS temperatures(
                                       temperature REAL,
                                       timestamp INTEGER);''')
        connection.commit()
        connection.close()

    def save_temperature(self, temperature, timestamp):
        connection = sqlite3.connect(self.db_name)
        c = connection.cursor()
        c.execute('''INSERT INTO temperatures VALUES ({}, {})'''.format(temperature, timestamp))
        connection.commit()
        connection.close()
