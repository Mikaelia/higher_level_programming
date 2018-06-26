-- Lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name, COUNT(*) AS 'number of shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY 'number of shows' DESC
