-- It is used to count the number of records with the same value
SELECT score, COUNT(*) AS number FROM second_table GROUP BY(score) ORDER BY DESC;
