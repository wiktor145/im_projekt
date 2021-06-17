class ParsedFile:

    def __init__(self, person_fields_dict, study_fields_dict, series_fields_dict, image_fields_dict,
                 extracted_fields_dict, dicom_dict):
        self.person_fields_dict = person_fields_dict
        self.study_fields_dict = study_fields_dict
        self.series_fields_dict = series_fields_dict
        self.image_fields_dict = image_fields_dict
        self.extracted_fields_dict = extracted_fields_dict
        self.dicom_dict = dicom_dict
