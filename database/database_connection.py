import mysql.connector
from datetime import datetime
import time
import traceback

from database.db_classes import Patient, Study, Series, Image, File, ImageFile, FileField

time.strftime('%Y-%m-%d %H:%M:%S')


class FieldNotFoundException(Exception):
    pass


class MySqlDatabaseConnection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="imuser",
            password="imuserpassword",
            database="imdb"
        )
        self.processed_files = set()
        self.processed_files_cache_time = None
        self.processed_files_cache_lifetime_seconds = 60
        self.get_processed_files_from_db()

    def was_file_processed(self, filename):
        cache_life = datetime.now() - self.processed_files_cache_time
        if cache_life.total_seconds() > self.processed_files_cache_lifetime_seconds:
            self.get_processed_files_from_db()

        return filename in self.processed_files

    def add_data_to_db(self, data, filename):
        self.add_to_file_table(filename, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1, data)
        self.processed_files.add(filename)

    def add_failed_file_to_db(self, filename):
        self.add_to_file_table(filename, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0)

    def get_processed_files_from_db(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT file_name FROM files")
        myresult = mycursor.fetchall()
        for x in myresult:
            self.processed_files.add(str(x[0]))

        mycursor.close()
        self.processed_files_cache_time = datetime.now()

    def add_to_file_table_class(self, parsed_file, filename):
        processed_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        was_successful = 1
        mycursor = self.db.cursor()
        try:

            # adding to files table
            file_id = self.add_to_table_files(mycursor, filename, processed_date, was_successful, parsed_file)

            # adding to files_fileds table
            self.add_to_table_files_fileds(mycursor, file_id, parsed_file)

            # adding to patients table
            patient_id = self.add_to_table_patients(mycursor, parsed_file)

            # adding to srtudies table
            studies_id = self.add_to_table_studies(mycursor, patient_id, parsed_file)

            # adding to series table
            series_id = self.add_to_table_series(mycursor, studies_id, parsed_file)

            # adding to images table
            image_id = self.add_to_table_images(mycursor, series_id, file_id, parsed_file)

            self.db.commit()

        except Exception as e:
            print(e)
            traceback.print_exc()
            self.db.rollback()
        finally:
            mycursor.close()

    def add_to_file_table(self, filename, processed_date, was_successful, content=None):
        mycursor = self.db.cursor()
        sql = "INSERT INTO files (file_name, processed_date, was_successful, content) VALUES (%s, %s, %s, %s)"
        val = (filename, processed_date, was_successful, str(content))
        mycursor.execute(sql, val)
        id = mycursor.lastrowid
        if content:
            for key in content:
                sql = "INSERT INTO files_fields (file_id, keyword, value) VALUES (%s, %s, %s)"
                val = (str(id), str(key), str(content[key]))
                mycursor.execute(sql, val)

        self.db.commit()
        mycursor.close()

    def get_processed_files_list(self):
        self.get_processed_files_from_db()
        return list(self.processed_files)

    def get_processed_files_with_dates(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT file_name, processed_date, content, comment FROM files order by processed_date desc")
        myresult = mycursor.fetchall()
        result = []
        for x in myresult:
            result.append((str(x[0]), str(x[1]), str(x[2]), str(x[3])))

        mycursor.close()
        return result

    def save_comment_for_file(self, filename, comment):
        mycursor = self.db.cursor()
        sql = "update files set comment = %s where file_name = %s"
        val = (comment, filename)
        mycursor.execute(sql, val)
        self.db.commit()
        mycursor.close()

    def save_comment_for_file_id(self, file_id, comment):
        mycursor = self.db.cursor()
        sql = "update files set comment = %s where file_id = %s"
        val = (comment, file_id)
        mycursor.execute(sql, val)
        self.db.commit()
        mycursor.close()

    def get_values_list_for_file(self, filename):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT keyword, value FROM files_fields where file_Id = " + \
            "(select file_Id from files where file_name = %s) order by keyword",
            (filename,))
        myresult = mycursor.fetchall()
        result = []
        for x in myresult:
            result.append((str(x[0]), str(x[1])))
        mycursor.close()
        return result

    def add_to_table_files(self, mycursor, filename, processed_date, was_successful, parsed_file):
        sql = "INSERT INTO files (file_name, processed_date, was_successful, content) VALUES (%s, %s, %s, %s)"
        val = (filename, processed_date, was_successful, str(parsed_file.extracted_fields_dict))
        mycursor.execute(sql, val)
        return mycursor.lastrowid

    def add_to_table_files_fileds(self, mycursor, file_id, parsed_file):
        dc = parsed_file.extracted_fields_dict
        for key in dc:
            sql = "INSERT INTO files_fields (file_id, keyword, value) VALUES (%s, %s, %s)"
            val = (str(file_id), str(key), str(dc[key]))
            mycursor.execute(sql, val)

    def add_to_table_patients(self, mycursor, parsed_file):
        dc = parsed_file.person_fields_dict
        if "PatientID" not in dc:
            raise FieldNotFoundException("PatientID is not present")

        sql = "SELECT patient_id from patients WHERE PatientID = %s"
        val = (str(dc["PatientID"]),)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if result:
            return result[0][0]
        else:
            sql = "INSERT INTO patients (PatientID, PatientAge, PatientBirthDate, PatientName, PatientSex) " + \
                  "VALUES (%s, %s, %s, %s, %s)"
            val = (str(dc.get("PatientID")), str(dc.get("PatientAge", "")), str(dc.get('PatientBirthDate', '')),
                   str(dc.get("PatientName", '')), str(dc.get("PatientSex", '')))
            mycursor.execute(sql, val)
            return mycursor.lastrowid

    def add_to_table_studies(self, mycursor, patient_id, parsed_file):
        dc = parsed_file.study_fields_dict
        if "StudyInstanceUID" not in dc:
            raise FieldNotFoundException("StudyInstanceUID is not present")

        sql = "SELECT study_id from studies WHERE StudyInstanceUID = %s"
        val = (str(dc["StudyInstanceUID"]),)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if result:
            return result[0][0]
        else:
            sql = "INSERT INTO studies (StudyInstanceUID, patient_id, StudyDate, StudyDescription, " + \
                  "StudyID, StudyIDIssuer, StudyTime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (str(dc.get("StudyInstanceUID")), str(patient_id), str(dc.get('StudyDate', '')),
                   str(dc.get("StudyDescription", '')), str(dc.get("StudyID", '')), str(dc.get("StudyIDIssuer", '')),
                   str(dc.get("StudyTime", '')))
            mycursor.execute(sql, val)
            return mycursor.lastrowid

    def add_to_table_series(self, mycursor, studies_id, parsed_file):
        dc = parsed_file.series_fields_dict
        if "SeriesInstanceUID" not in dc:
            raise FieldNotFoundException("SeriesInstanceUID is not present")

        sql = "SELECT series_id from series WHERE SeriesInstanceUID = %s"
        val = (str(dc["SeriesInstanceUID"]),)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if result:
            return result[0][0]
        else:
            sql = "INSERT INTO series (SeriesInstanceUID, study_id, SeriesDate, SeriesDescription, " + \
                  "SeriesNumber, SeriesTime) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (str(dc.get("SeriesInstanceUID")), str(studies_id), str(dc.get('SeriesDate', '')),
                   str(dc.get("SeriesDescription", '')), str(dc.get("SeriesNumber", '')), str(dc.get("SeriesTime", '')))
            mycursor.execute(sql, val)
            return mycursor.lastrowid

    def add_to_table_images(self, mycursor, series_id, file_id, parsed_file):
        dc = parsed_file.image_fields_dict

        sql = "INSERT INTO images (series_id, file_id, ImageType, PixelData) VALUES (%s, %s, %s, %s)"
        val = (str(series_id), str(file_id), str(dc.get('ImageType', '')), str(dc.get("PixelData", '')))
        mycursor.execute(sql, val)
        return mycursor.lastrowid

    def get_patients(self):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT patient_id, PatientID, PatientAge, PatientBirthDate, PatientName, " + \
            "PatientSex FROM patients order by patient_id desc")
        myresult = mycursor.fetchall()
        patients_list = []
        for x in myresult:
            patients_list.append(Patient(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5])))

        mycursor.close()
        return patients_list

    def get_studies_for_patient(self, patient):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT study_id, StudyInstanceUID, patient_id, StudyDate, StudyDescription, " + \
            "StudyID, StudyIDIssuer, StudyTime FROM studies where patient_id = %s order by study_id desc",
            (patient.patient_id,))
        myresult = mycursor.fetchall()
        studies_list = []
        for x in myresult:
            studies_list.append(
                Study(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6]), str(x[7])))

        mycursor.close()
        return studies_list

    def get_series_for_study(self, study):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT series_id, SeriesInstanceUID, study_id, SeriesDate, SeriesDescription, " + \
            "SeriesNumber, SeriesTime FROM series where study_id = %s order by series_id desc",
            (study.study_id,))
        myresult = mycursor.fetchall()
        series_list = []
        for x in myresult:
            series_list.append(
                Series(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6])))

        mycursor.close()
        return series_list

    def get_images_for_series(self, series):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT image_id, series_id, file_id, ImageType, PixelData " + \
            "FROM images where series_id = %s order by image_id desc",
            (series.series_id,))
        myresult = mycursor.fetchall()
        images_list = []
        for x in myresult:
            images_list.append(
                Image(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4])))

        mycursor.close()
        return images_list

    def get_file_by_file_id(self, file_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT file_id, file_name, processed_date, was_successful, content, comment " + \
            "FROM files where file_id = %s",
            (file_id,))
        myresult = mycursor.fetchall()
        file = None
        for x in myresult:
            file = File(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]))

        mycursor.close()
        return file

    def get_filefields_for_file(self, file_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            "SELECT file_id, keyword, value " + \
            "FROM files_fields where file_id = %s order by keyword",
            (file_id,))
        myresult = mycursor.fetchall()
        fields_list = []
        for x in myresult:
            fields_list.append(
                FileField(str(x[0]), str(x[1]), str(x[2])))

        mycursor.close()
        return fields_list

    def get_imagefiles_for_series(self, series):
        images = self.get_images_for_series(series)
        imagefiles = []
        for image in images:
            file = self.get_file_by_file_id(image.file_id)
            file_fields = self.get_filefields_for_file(image.file_id)
            imagefiles.append(ImageFile(image, file, file_fields))

        return imagefiles


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

    def get_processed_files_list(self):
        return list(self.processed_files)

    def get_processed_files_with_dates(self):
        result = []
        for i in range(30):
            result.append(("File_{}".format(i), str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                           self.db[0] if len(self.db) > 0 else "tes test", "comment comment comment"))

        return result

    def save_comment_for_file(self, filename, comment):
        print(filename, comment)

    def get_values_list_for_file(self, filename):
        return [('key1', 'value1'), ('key2', 'value2')]