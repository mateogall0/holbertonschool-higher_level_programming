-- list shows
SELECT title
FROM tv_shows
JOIN tv_genres ON tv_genres.name = tv_shows.genre
ORDER BY tv_shows.title, tv_genres.name
