from datetime import datetime, timedelta, timezone
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

    def get_last_period_temperature(self, period_string):
        connection = sqlite3.connect(self.db_name)
        c = connection.cursor()
        from_datetime = datetime.utcnow()
        if period_string == "HOUR":
            from_datetime -= timedelta(hours=1)
        elif period_string == "DAY":
            from_datetime -= timedelta(days=1)
        elif period_string == "WEEK":
            from_datetime -= timedelta(days=7)
        elif period_string == "MONTH":
            from_datetime -= timedelta(days=30)
        c.execute('''SELECT * FROM temperatures
                     WHERE timestamp >= {} AND timestamp <= {}'''.format(self.__get_timestamp(from_datetime),
                                                                         self.__get_timestamp(datetime.now())))
        temp_tab = c.fetchall()
        connection.close()
        return temp_tab

    @staticmethod
    def __get_timestamp(dt):
        return int((dt - datetime(1970, 1, 1)) / timedelta(seconds=1))
