-- It is used to display data in a database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE genre_id is NULL ORDER BY tv_shows, tv_show_genres;
