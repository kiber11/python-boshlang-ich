-- CREATE TABLE Meva (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     nomi VARCHAR(50),
--     narxi DECIMAL(10, 2),
--     navi VARCHAR(50)
-- );

-- INSERT INTO Meva (nomi, narxi, navi)
-- VALUES 
-- ('Olma', 15000, 'Oq olma'),
-- ('Anor', 20000, 'Oʻzbek anori'),
-- ('Banan', 5000, 'Tropik banan'),
-- ('Apelsin', 12000, 'Qizil apelsin'),
-- ('Kivi', 18000, 'Yashil kivi'),
-- ('Uzum', 25000, 'Qora uzum'),
-- ('Nok', 14000, 'Shirin nok'),
-- ('Shaftoli', 10000, 'Oltin shaftoli'),
-- ('Ananas', 60000, 'Gavayi ananasi'),
-- ('Mandarin', 22000, 'Xitoy mandarini');

-- SELECT * FROM Meva;

-- select nomi,narxi from meva
-- where narxi between 10000 and 50000;

-- use dars_data;
-- SELECT *
-- FROM meva m1
-- WHERE EXISTS (
--     SELECT 1
--     FROM meva m2
--     WHERE LENGTH(m1.nomi) = LENGTH(m2.nomi)
--     GROUP BY LENGTH(m2.nomi)
--     HAVING COUNT(*) > 1  
-- )
-- ORDER BY m1.narxi DESC;








