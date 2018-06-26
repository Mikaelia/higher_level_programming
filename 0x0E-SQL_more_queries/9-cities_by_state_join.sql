-- Displays all cities in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.id=state.state_id;
