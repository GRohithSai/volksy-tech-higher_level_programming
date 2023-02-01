-- It is used to display the records in a table with condition
SELECT c.id, c.name, s.name FROM cities as c INNER JOIN states AS s ON c.state_id = s.id ORDER BY c.id;
