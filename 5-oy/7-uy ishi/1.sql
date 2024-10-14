-- Ma'lumotlar bazasini yaratish
-- CREATE DATABASE BOZOR;

-- BOZOR ma'lumotlar bazasiga ulanish
-- USE BOZOR;

-- meva nomli jadvalni yaratish
-- CREATE TABLE meva (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     meva_nomi VARCHAR(50),
--     meva_narxi DECIMAL(10, 2),
--     meva_turi VARCHAR(50)
-- );

-- meva jadvaliga ma'lumotlarni qo'shish
-- INSERT INTO meva (meva_nomi, meva_narxi, meva_turi) VALUES
-- ('Olma', 5000, 'Daraxt mevalari'),
-- ('Banan', 8000, 'Tropik mevalar'),
-- ('Olma', 5000, 'Daraxt mevalari'),
-- ('Anor', 10000, 'Daraxt mevalari'),
-- ('Apelsin', 12000, 'Sitrus mevalar'),
-- ('Banan', 8000, 'Tropik mevalar'),
-- ('Nok', 7000, 'Daraxt mevalari'),
-- ('Shaftoli', 9000, 'Daraxt mevalari'),
-- ('Olma', 5000, 'Daraxt mevalari'),
-- ('Anor', 10000, 'Daraxt mevalari');

-- 1
-- select * from meva;
-- create table meva_1 as
-- select distinct meva_nomi,meva_narxi,meva_turi from meva;
-- delete from meva;

-- insert into meva(meva_nomi,meva_narxi,meva_turi)
-- select meva_nomi,meva_narxi,meva_turi from  meva_1;
-- drop table meva_1;

-- 2
-- select * from meva
-- order by meva_narxi desc
-- limit 5;

