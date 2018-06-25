-- Lists the number of records with the same score in the table second_table
-- Displays the score, number of records for this score
-- Sorted by the number of records (descending)
SELECT score, count(*) as number from second_table
group by score
order by score DESC
