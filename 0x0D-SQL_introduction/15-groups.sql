-- Lists the number of records with the same score in the table second_table
-- Displays the score, number of records for this score
-- Sorted by the number of records (descending)
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
