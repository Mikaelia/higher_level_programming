-- Lists all cities of California in database hbtn_0d_usa
SELECT id, name  FROM cities
WHERE id = (
	SELECT state_id FROM states
	WHERE name = 'California'
