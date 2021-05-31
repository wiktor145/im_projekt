import os

import pydicom as pydicom


class MetadataExtractor:

    def __init__(self, configuration):
        self.configuration = configuration

    def extract_data_from_file(self, file_name):
        try:
            ds = pydicom.dcmread(file_name)
            # print(ds)

            ret = {}

            for field in self.configuration.fields_to_extract:
                if field in ds.dir():
                    # print(field, ds.dir())
                    # print(ds[field])
                    ret[field] = ds[field]
            # print(file_name)
            # print(ds.dir())
            # print(ds['RadiationMode'])
            print(ret)
            return ret
        except Exception as e:
            print("ERROR!")
            print(e)
            # print(ds)
            return None
