-- lists all records of the table of the database hbtn_0c_0.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ''
ORDER BY `score` DESC
