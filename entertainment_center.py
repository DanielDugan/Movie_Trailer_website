import dd_fresh_tomatoes
import media

# The structure from media was (self, movie_title,movie_storyline,poster_image, trailer_youtube)
# It is repeated below with other films in the website project

princess_bride = media.Movie ("Princess Bride",
"A dread pirate and a princess who started out two different people remember the value of true love",
"http://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
"www.youtube.com/watch?v=VYgcrny2hRs")

groundhog_day = media.Movie ("Groundhog Day",
"A reporter who loses love of his job and his life discovers a path to recover it. Over and over again",
"http://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
"www.youtube.com/watch?v=tSVeDx9fk60")


life_is_beautiful = media.Movie ("Life is Beautiful",
"A jewish immegrant in Italy makes the best of a dark time in history",
"http://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
"www.youtube.com/watch?v=16RZHqCIy9M")


Indiana_Jones_L_C = media.Movie ("Indiana Jones and The Last Crusade",
"The last great adventure movie featuring Indiana Jones. Featuring Nazis, Fathers and Sons, the Holy Grail and explosions.",
"http://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg","https://www.youtube.com/watch?v=a6JB2suJYHM")

Airplane = media.Movie ("Airplane!",
"A pun-filled and silly movie gets nearer to perfection each time you watch it.",
"http://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
"https://www.youtube.com/watch?v=rzRJWy-3_Dc")

movies = [princess_bride, groundhog_day, life_is_beautiful, Indiana_Jones_L_C, Airplane]
dd_fresh_tomatoes.open_movies_page(movies)
# The above lines create an array of the movies described above and a call to open the generated fresh_tomatoes.html.
""" entertainment_center is a student built portion of the Udemy Full Stack Nano Degree Project 1 "Movie Trailer Website"""

