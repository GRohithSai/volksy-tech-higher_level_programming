-- It is used to count the number of records with the same value
SELECT score, COUNT(score) AS number FROM second_table ORDER BY(score) DESC;
