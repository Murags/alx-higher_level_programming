-- SELECT FORM TWO TABLES
SELECT tv_genres.name FROM tv_show_genres WHERE tv_show_genres.show_id=8
INNER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name 
ORDER BY tv_genres.name ASC
