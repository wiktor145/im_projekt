import mysql.connector
from datetime import date, datetime, timedelta


class MySqlDatabaseConnection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="imuser",
            password="imuserpassword",
            database="imdb"
        )
        self.processed_files = set()
        self.get_processed_files_from_db()

    def was_file_processed(self, filename):
        return filename in self.processed_files

    def add_data_to_db(self, data, filename):
        self.add_to_file_table(filename, datetime.now().date(), 1, str(data))
        self.processed_files.add(filename)

    def add_failed_file_to_db(self, filename):
        self.add_to_file_table(filename, datetime.now().date(), 0)

    def get_processed_files_from_db(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT file_name FROM files")
        myresult = mycursor.fetchall()
        for x in myresult:
            self.processed_files.add(str(x[0]))

        mycursor.close()

    def add_to_file_table(self, filename, processed_date, was_successful, content=None):
        mycursor = self.db.cursor()
        sql = "INSERT INTO files (file_name, processed_date, was_successful, content) VALUES (%s, %s, %s, %s)"
        val = (filename, processed_date, was_successful, content)
        mycursor.execute(sql, val)
        self.db.commit()
        mycursor.close()


class MockDatabaseConnection:

    def __init__(self):
        self.name = "Mock Database V2"
        self.processed_files = set()
        self.db = []

    def was_file_processed(self, filename):
        return filename in self.processed_files

    def add_data_to_db(self, data, filename):
        self.processed_files.add(filename)
        self.db.append(data)

    def add_failed_file_to_db(self, filename):
        self.processed_files.add(filename)
