-- Displays all cities in the database hbtn_0d_usa
SELECT cities.id, states.name, cities.name FROM states INNER JOIN states ON cities.id=state.state_id;
