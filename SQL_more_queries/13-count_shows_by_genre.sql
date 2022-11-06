-- list shows
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY number_of_shows DESC
