-- It is used to display the date in the database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id
