import glob
import os
import time


def check_repository_for_new_files(db_connection, directory_path, data_extractor, check_time, is_one_time=False,
                                   with_last_file_limit=True):
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
                data = data_extractor.extract_data_from_file(file_path)
                if data:
                    db_connection.add_data_to_db(data, file_name)

        if is_one_time:
            return
        else:
            time.sleep(check_time)
