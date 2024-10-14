-- CREATE DATABASE UNIVERSITET;
-- USE UNIVERSITET;
-- CREATE TABLE talaba (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     talaba_ismi VARCHAR(100),
--     talaba_kursi INT,
--     talaba_stipendiyasi DECIMAL(10, 2)
-- );
-- INSERT INTO talaba (talaba_ismi, talaba_kursi, talaba_stipendiyasi) VALUES 
-- ('Ali', 1, 500.00),
-- ('Oydin', 2, 600.50),
-- ('Diyor', 3, 550.00),
-- ('Sarina', 1, 700.00),
-- ('Rustam', 2, 500.00),
-- ('Malika', 3, 650.00),
-- ('Farhod', 1, 580.00),
-- ('Nodira', 2, 620.00),
-- ('Aziz', 3, 500.00),
-- ('Laylo', 1, 720.00);

-- insert into talaba(talaba_ismi,talaba_kursi,talaba_stipendiyasi)
-- values('Abdulloh',4,500.00),
-- ('Barno',4,400.00);
-- select * from talaba;

-- delete from talaba
-- where talaba_kursi=4;
-- update talaba
-- set talaba_kursi=talaba_kursi+1;

select talaba_kursi, count(talaba_kursi) as talabalarsoni from talaba
group by talaba_kursi;



