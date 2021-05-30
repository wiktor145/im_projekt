drop database if exists imdb;

create database imdb;

use imdb;

create table files(
   file_id INT NOT NULL AUTO_INCREMENT,
   file_name VARCHAR(200) NOT NULL,
   processed_date DATETIME,
   was_successful INT NOT NULL,
   content VARCHAR(10000),
   comment VARCHAR(5000),
   PRIMARY KEY ( file_id )
);

create table patients(
    patient_id INT NOT NULL AUTO_INCREMENT,
    PatientAge VARCHAR(200),
    PatientBirthDate VARCHAR(200),
    PatientID VARCHAR(200),
    PatientName VARCHAR(200),
    PatientOrientation VARCHAR(200),
    PatientPosition VARCHAR(200),
    PatientSex VARCHAR(200),
    PRIMARY KEY ( patient_id )
);

create table studies(
    study_id INT NOT NULL AUTO_INCREMENT,
    --patient_id INT
    StudyDate VARCHAR(200),
    StudyDescription VARCHAR(200),
    StudyID VARCHAR(200),
    StudyIDIssuer VARCHAR(200),
    StudyInstanceUID VARCHAR(200),
    StudyTime VARCHAR(200),
    PRIMARY KEY ( study_id )
--, FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);


create table series(
    series_id INT NOT NULL AUTO_INCREMENT,
    -- study_id INT,
    SeriesDate VARCHAR(200),
    SeriesDescription VARCHAR(200),
    SeriesInstanceUID VARCHAR(200),
    SeriesNumber VARCHAR(200),
    SeriesTime VARCHAR(200),
    PRIMARY KEY ( series_id )
--, FOREIGN KEY (study_id) REFERENCES studies(study_id)
);


create table images(
    image_id INT NOT NULL AUTO_INCREMENT,
    ImageType VARCHAR(200),
    --content BLOB,
    PRIMARY KEY ( series_id )
--, FOREIGN KEY (series_id) REFERENCES series(series_id)
);