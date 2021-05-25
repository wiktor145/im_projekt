import threading
import time

from repository_checker import check_repository_for_new_files
from database_connection import *
from metadata_extractor import *

checker_thread = None


if __name__ == '__main__':
    # db_connection = MockDatabaseConnection()
    db_connection = MySqlDatabaseConnection()
    check_time = 60 * 1

    configuration = Configuration()
    extractor = MetadataExtractor(configuration)

    dir_path = "./data/"

    checker_thread = threading.Thread(target=check_repository_for_new_files,
                                      args=(db_connection, dir_path, extractor, check_time))
    checker_thread.start()

    try:
        while True:
            time.sleep(30)
        # todo later maybe sth more?
    except:
        exit(0)
