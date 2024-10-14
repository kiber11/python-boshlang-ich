-- use dars_data;
-- CREATE TABLE AEROPORT (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     samolyot_turi VARCHAR(50),
--     uchish_sanasi DATE,
--     uchish_shaxri VARCHAR(50),
--     qonish_shaxri VARCHAR(50),
--     uchish_vaqti TIME
-- );

-- INSERT INTO AEROPORT (samolyot_turi, uchish_sanasi, uchish_shaxri, qonish_shaxri, uchish_vaqti)
-- VALUES 
-- ('Boeing 737', '2024-01-15', 'Toshkent', 'New York', '10:30'),
-- ('Airbus A320', '2024-02-16', 'Toshkent', 'Istanbul', '14:45'),
-- ('Boeing 777', '2024-03-17', 'Toshkent', 'London', '18:00'),
-- ('Airbus A380', '2024-04-18', 'Toshkent', 'London', '09:15'),
-- ('Embraer E190', '2024-05-19', 'Toshkent', 'Doha', '13:30'),
-- ('Boeing 787', '2024-06-20', 'Toshkent', 'London', '16:45'),
-- ('Boeing 747', '2024-07-21', 'Toshkent', 'Tokyo', '08:00'),
-- ('Airbus A350', '2024-08-22', 'Toshkent', 'Paris', '12:20'),
-- ('Bombardier CRJ', '2024-09-23', 'Toshkent', 'Dubai', '17:50'),
-- ('Boeing 737 Max', '2024-10-24', 'Toshkent', 'Seoul', '07:30');
-- SELECT samolyot_turi, uchish_sanasi, uchish_shaxri, qonish_shaxri, uchish_vaqti, COUNT(*)
-- FROM AEROPORT
-- GROUP BY samolyot_turi, uchish_sanasi, uchish_shaxri, qonish_shaxri, uchish_vaqti
-- HAVING COUNT(*) > 1;

WITH DuplicateRows AS (
    SELECT id, ROW_NUMBER() OVER (PARTITION BY samolyot_turi, uchish_sanasi, uchish_shaxri, qonish_shaxri, uchish_vaqti ORDER BY id) AS row_num
    FROM AEROPORT
)
DELETE FROM AEROPORT
WHERE id IN (SELECT id FROM DuplicateRows WHERE row_num > 1);



select * from aeroport;
-- select samolyot_turi,uchish_sanasi from aeroport
-- where month(uchish_sanasi)>2 and month(uchish_sanasi)<6;

-- delete from aeroport
-- where hour(uchish_vaqti)>14 and hour(uchish_vaqti)<18 and qonish_shaxri="London";

