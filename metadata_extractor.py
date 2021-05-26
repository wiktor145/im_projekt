import os

import pydicom as pydicom


class Configuration:
    fields_to_extract = [
        "PatientName",
        "Modality",
        "StudyID",
        "StudyTime",
        "PatientID",
        "RadiationSetting",
        "RadiationMode",
        "SeriesNumber"
    ]


class MetadataExtractor:

    def __init__(self, configuration):
        self.configuration = configuration

    def extract_data_from_file(self, file_name):
        try:
            ds = pydicom.dcmread(file_name)
            # print(ds)

            ret = {}

            for field in self.configuration.fields_to_extract:
                ret[field] = ds[field]

            print(ret)
            return str(ds)
        except Exception as e:
            print(e)
            return None
