import glob
import json
import os
import time
import signal

from database.database_connection import MockDatabaseConnection, MySqlDatabaseConnection
from metadata_extractor import MetadataExtractor
from other_classes.constants import LAST_FILE_MTIME_FILE, DELETED_MARK, CONFIGURATION_FILE, DATA_DIRECTORY

finish = False


def signal_handler(sig, frame):
    global finish
    finish = True


def load_last_file_mtime():
    ret = None
    if os.path.isfile(LAST_FILE_MTIME_FILE):
        with open(LAST_FILE_MTIME_FILE) as f:
            s = f.read()
            if s != DELETED_MARK:
                try:
                    ret = float(f.read())
                except:
                    pass
    return ret


def save_last_file_mtime(last_file_mtime):
    with open(LAST_FILE_MTIME_FILE, "w") as f:
        s = f.read() if os.stat(LAST_FILE_MTIME_FILE).st_size != 0 else ""
        if s != DELETED_MARK:
            f.write(str(last_file_mtime))


def check_repository_for_new_files(db_connection, directory_path, data_extractor, check_time, is_one_time=False,
                                   with_last_file_limit=False):
    while True:
        last_file_mtime = load_last_file_mtime()

        list_of_files = filter(os.path.isfile,
                               glob.glob(directory_path + '*'))

        files_with_dates = [(x, os.path.getmtime(x)) for x in list_of_files]

        files_with_dates.sort(key=lambda x: x[1], reverse=True)

        last_processed = -1

        for file_path, system_modification_time in files_with_dates:
            file_name = os.path.basename(file_path)
            print(file_name)
            # system_modification_time = os.path.getmtime(file_path)

            if with_last_file_limit and last_file_mtime and system_modification_time < last_file_mtime:
                break

            last_processed += 1

            if not db_connection.was_file_processed(file_name):
                data = data_extractor.extract_data_from_file_class(file_path)
                if data:
                    db_connection.add_to_file_table_class(data, file_name, system_modification_time)
                else:
                    db_connection.add_failed_file_to_db(file_name, system_modification_time)

        if last_processed >= 0:
            last_file_mtime = files_with_dates[0][1]
            save_last_file_mtime(last_file_mtime)

        if is_one_time or finish:
            return
        else:
            time.sleep(check_time)


if __name__ == '__main__':
    # db_connection = MockDatabaseConnection()
    db_connection = MySqlDatabaseConnection()
    check_time = 60 * 1

    f = open(CONFIGURATION_FILE, "r")
    configuration = json.load(f)
    f.close()

    extractor = MetadataExtractor(configuration)

    dir_path = DATA_DIRECTORY

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    check_repository_for_new_files(db_connection, dir_path, extractor, check_time)
