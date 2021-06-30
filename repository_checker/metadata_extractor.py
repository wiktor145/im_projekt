import pydicom as pydicom

from other_classes.parsed_file import ParsedFile


class MetadataExtractor:

    def __init__(self, configuration):
        # print(configuration)
        self.configuration = configuration

    def extract_fields(self, ds, fields_to_extract, file_name):
        ret = {}

        for field in fields_to_extract:
            if field in ds.dir():
                # print(field, ds.dir())
                # print(ds[field])
                try:
                    ret[field] = ds[field]
                except:
                    print("Error during getting field", field, "in file", file_name)
        # print(file_name)
        # print(ds.dir())
        # print(ds['RadiationMode'])
        # print(ds)
        return ret

    def extract_data_from_file(self, file_name):
        try:
            ds = pydicom.dcmread(file_name)
            # print(ds)
            return self.extract_fields(ds, self.configuration['fields_to_extract'], file_name)
        except Exception as e:
            print("ERROR!")
            print(e)
            # print(ds)
            return None

    def extract_data_from_file_class(self, file_name):
        try:
            ds = pydicom.dcmread(file_name)
            # print(ds)
            extracted_fields_dict = self.extract_fields(ds, self.configuration['fields_to_extract'], file_name)
            person_fields_dict = self.extract_fields(ds, self.configuration['person_fields'], file_name)
            study_fields_dict = self.extract_fields(ds, self.configuration['study_fields'], file_name)
            series_fields_dict = self.extract_fields(ds, self.configuration['series_fields'], file_name)
            image_fields_dict = self.extract_fields(ds, self.configuration['image_fields'], file_name)

            return ParsedFile(person_fields_dict, study_fields_dict, series_fields_dict, image_fields_dict,
                              extracted_fields_dict, ds)

        except Exception as e:
            print("ERROR!")
            print(e)
            # print(ds)
            return None
