

USE MediaGeneral


CREATE TABLE conversion_table (
    id BIGINT NOT NULL AUTO_INCREMENT,
    Website_ID INT,
    Clicks INT,
    Conversions INT,
    Flag1 INT,
    Flag2 INT,
    Flag3 INT,
    PRIMARY KEY (id));



#Load train table to sql
LOAD DATA INFILE '/var/lib/mysql-files/data-data_analyst.txt' 
INTO TABLE conversion_table 
FIELDS TERMINATED BY '\t' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Website_ID, Clicks,Conversions,Flag1,Flag2,Flag3);



