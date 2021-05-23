class MySqlDatabaseConnection:
    pass


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
