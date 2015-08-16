from datetime import datetime, timedelta
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

    def get_last_period_temperature(self, period_string, without_filling=False):
        connection = sqlite3.connect(self.db_name)
        c = connection.cursor()
        from_datetime = datetime.utcnow().replace(second=0, microsecond=0)
        if period_string == "HOUR":
            from_datetime -= timedelta(hours=1)
        elif period_string == "DAY":
            from_datetime -= timedelta(days=1)
        elif period_string == "WEEK":
            from_datetime -= timedelta(days=7)
        elif period_string == "MONTH":
            from_datetime -= timedelta(days=30)
        now = datetime.utcnow().replace(second=0, microsecond=0)
        c.execute('''SELECT * FROM temperatures
                     WHERE timestamp > {} AND timestamp <= {}'''.format(self.__get_timestamp(from_datetime),
                                                                        self.__get_timestamp(now)))
        temp_tab = c.fetchall()
        if not without_filling:
            self.__fill_missing_data(temp_tab, from_datetime, now)
        connection.close()
        return temp_tab

    @staticmethod
    def __get_timestamp(dt):
        return int((dt - datetime(1970, 1, 1)) / timedelta(seconds=1))

    @staticmethod
    def __fill_missing_data(temp_tab, from_datetime, to_datetime):
        index = 0
        while from_datetime != to_datetime:
            from_datetime += timedelta(minutes=1)
            current_timestamp = DatabaseHandler.__get_timestamp(from_datetime)
            if index == len(temp_tab) or current_timestamp < temp_tab[index][1]:
                temp_tab.insert(index, ["?", current_timestamp])
            index += 1
