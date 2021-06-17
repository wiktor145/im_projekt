import glob
import json
import os
import time
import signal

from database.database_connection import MockDatabaseConnection, MySqlDatabaseConnection
from metadata_extractor import MetadataExtractor

finish = False


def signal_handler(sig, frame):
    global finish
    finish = True


def check_repository_for_new_files(db_connection, directory_path, data_extractor, check_time, is_one_time=False,
                                   with_last_file_limit=False):
    last_file = None
    last_file_saved = False

    while True:
        list_of_files = filter(os.path.isfile,
                               glob.glob(directory_path + '*'))
        list_of_files = sorted(list_of_files,
                               key=os.path.getmtime)
        last_file_saved = False
        for file_path in list_of_files:
            file_name = os.path.basename(file_path)
            print(file_name)

            if with_last_file_limit and file_name == last_file:
                break

            if not last_file_saved:
                last_file_saved = True
                last_file = file_name

            if not db_connection.was_file_processed(file_name):
                data = data_extractor.extract_data_from_file_class(file_path)
                if data:
                    db_connection.add_to_file_table_class(data, file_name)
                else:
                    db_connection.add_failed_file_to_db(file_name)

        if is_one_time or finish:
            return
        else:
            time.sleep(check_time)


if __name__ == '__main__':
    # db_connection = MockDatabaseConnection()
    db_connection = MySqlDatabaseConnection()
    check_time = 60 * 1

    f = open("../configuration.json", "r")
    configuration = json.load(f)
    f.close()

    extractor = MetadataExtractor(configuration)

    dir_path = "../data/"

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    check_repository_for_new_files(db_connection, dir_path, extractor, check_time)
