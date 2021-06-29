class File:
    def __init__(self, file_id, file_name, processed_date, was_successful,
                 content, comment, system_modification_time):
        self.file_id = file_id
        self.file_name = file_name
        self.processed_date = processed_date
        self.was_successful = was_successful
        self.content = content
        self.comment = comment
        self.system_modification_time = system_modification_time


class FileField:
    def __init__(self, file_id, keyword, value):
        self.file_id = file_id
        self.keyword = keyword
        self.value = value


class Patient:
    def __init__(self, patient_id, PatientID, PatientAge, PatientBirthDate,
                 PatientName, PatientSex):
        self.patient_id = patient_id
        self.PatientID = PatientID
        self.PatientAge = PatientAge
        self.PatientBirthDate = PatientBirthDate
        self.PatientName = PatientName
        self.PatientSex = PatientSex


class Study:
    def __init__(self, study_id, StudyInstanceUID, patient_id, StudyDate,
                 StudyDescription, StudyID, StudyIDIssuer, StudyTime ):
        self.study_id = study_id
        self.StudyInstanceUID = StudyInstanceUID
        self.patient_id = patient_id
        self.StudyDate = StudyDate
        self.StudyDescription = StudyDescription
        self.StudyID = StudyID
        self.StudyIDIssuer = StudyIDIssuer
        self.StudyTime = StudyTime


class Series:
    def __init__(self, series_id, SeriesInstanceUID, study_id, SeriesDate,
                 SeriesDescription, SeriesNumber, SeriesTime):
        self.series_id = series_id
        self.SeriesInstanceUID = SeriesInstanceUID
        self.study_id = study_id
        self.SeriesDate = SeriesDate
        self.SeriesDescription = SeriesDescription
        self.SeriesNumber = SeriesNumber
        self.SeriesTime = SeriesTime


class Image:
    def __init__(self, image_id, series_id, file_id, ImageType, PixelData, Modality):
        self.image_id = image_id
        self.series_id = series_id
        self.file_id = file_id
        self.ImageType = ImageType
        self.PixelData = PixelData
        self.Modality = Modality


class ImageFile:
    def __init__(self, image, file, file_fields):
        self.image = image
        self.file = file
        self.file_fields = file_fields
