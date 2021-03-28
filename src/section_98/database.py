import os
import sqlite3


class Database:
    def __init__(self, db_path=None):
        """Initialize Database class variables"""
        if db_path:
            self.connection = sqlite3.connect(db_path)
        elif self.is_windows:
            self.connection = sqlite3.connect("readings.db")
        else:
            self.connection = sqlite3.connect("/home/pi/readings.db")
        self.cursor = self.connection.cursor()
        self._check_db_schema()

    def __del__(self):
        self.connection.close()

    def _check_db_schema(self):
        sql_query = "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND tbl_name IN ('sensor_reading');"
        self.cursor.execute(sql_query)
        res = self.cursor.fetchall()
        if res[0][0] != 1:
            # sensor_reading table not found, create it
            self._create_tables()

    def _create_tables(self):
        sql_query = """CREATE TABLE sensor_reading (
            datetime_epoch INTEGER NOT NULL,
            datetime_utc TEXT NOT NULL,
            datetime_local TEXT NOT NULL,
            sensor_desc TEXT NOT NULL,
            reading_desc TEXT NOT NULL,
            reading_1 REAL NULL,
            reading_2 REAL NULL,
            reading_3 REAL NULL
        );"""
        self.cursor.execute(sql_query)
        self.connection.commit

    def write_sensor_readings_to_db(
        self, sensor_desc, reading_desc, reading_1, reading_2, reading_3
    ):
        sql_query = """INSERT INTO sensor_reading VALUES(
            strftime('%s','now') || substr(strftime('%f','now'),4),
            datetime('now'),
            datetime('now','localtime'),
            ?,
            ?,
            ?,
            ?,
            ?
        );"""
        self.cursor.execute(
            sql_query, (sensor_desc, reading_desc, reading_1, reading_2, reading_3)
        )
        self.connection.commit()

    @property
    def is_windows(self):
        return os.name == "nt"


if __name__ == "__main__":
    db = Database()
    db.write_sensor_readings_to_db(
        sensor_desc="BME280_Kitchen",
        reading_desc="Temperature;Pressure;Humidity",
        reading_1=1.1,
        reading_2=2.2,
        reading_3=None,
    )
