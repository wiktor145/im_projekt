import glob
import logging
import os
import time

last_file_mtime = None

directory_path = ".\\data\\"

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO)

logging.info(1)


list_of_files = filter(os.path.isfile,
                       glob.glob(directory_path + '*'))

logging.info(2)

files_with_dates = [(x, os.path.getmtime(x)) for x in list_of_files]

logging.info(3)

files_with_dates.sort(key=lambda x: x[1], reverse=True)

logging.info(4)

last_processed = 0

for file_path, system_modification_time in files_with_dates:
    file_name = os.path.basename(file_path)
    # system_modification_time = os.path.getmtime(file_path)


    last_processed += 1


logging.info(last_processed)
logging.info(5)

time.sleep(10)
