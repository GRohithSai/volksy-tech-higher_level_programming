-- It is used to display the records in a table with condition
SELECT id, name FROM cities INNER JOIN states ON cities.state_id = states.id;
