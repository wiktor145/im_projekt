import threading

from client_gui.client_gui import show_client_gui
from repository_checker.repository_checker import *

checker_thread = None

if __name__ == '__main__':
    db_connection = MockDatabaseConnection()
    # db_connection = MySqlDatabaseConnection()
    check_time = 60 * 1

    f = open("configuration.json", "r")
    configuration = json.load(f)
    f.close()

    extractor = MetadataExtractor(configuration)

    dir_path = "./data/"

    checker_thread = threading.Thread(target=check_repository_for_new_files,
                                      args=(db_connection, dir_path, extractor, check_time))
    checker_thread.start()

    client_db = MockDatabaseConnection()
    show_client_gui(db_connection)
    exit(0)

    try:
        while True:
            time.sleep(30)
        # todo later maybe sth more?
    except:
        exit(0)
