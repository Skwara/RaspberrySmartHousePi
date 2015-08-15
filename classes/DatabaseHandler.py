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

    def get_time_interval_temperature(self, from_timestamp, to_timestamp):
        connection = sqlite3.connect(self.db_name)
        c = connection.cursor()
        c.execute('''SELECT * FROM temperatures
                     WHERE timestamp >= {} AND timestamp <= {}'''.format(from_timestamp, to_timestamp))
        temp_tab = c.fetchall()
        connection.close()
        return temp_tab
