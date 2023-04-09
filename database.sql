CREATE DATABASE db_calendar
    DEFAULT CHARACTER SET = 'utf8mb4';

USE db_calendar;

CREATE TABLE tb_calendar(
    idCalendar INT PRIMARY KEY AUTO_INCREMENT
    ,uidCalendar VARCHAR(50)
    ,summaryCalendar VARCHAR(100)
    ,descriptionCalendar TEXT
    ,dtEndCalendar DATETIME
    ,categoriesCalendar VARCHAR(100)
);

