-- It is used to list all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_shows ON tv_genres.id = tv_show_genres.genre_id ORDER BY tv_genres.name;
