drop database if exists imdb;

create database imdb;

use imdb;

create table files(
   file_id INT NOT NULL AUTO_INCREMENT,
   file_name VARCHAR(200) NOT NULL,
   processed_date DATE,
   was_successful INT NOT NULL,
   content VARCHAR(10000),
   PRIMARY KEY ( file_id )
);
