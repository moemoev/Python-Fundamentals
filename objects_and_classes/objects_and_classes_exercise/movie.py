'''
TASK:
Create a class Movie. The __init__ method should receive a name and a director. It should also have default value of an
attribute watched set to False. There should also be a class attribute __watched_movies which will keep track of the number of all the watched movies. The class should have the following methods:
change_name(new_name) - changes the name of the movie
change_director(new_director) - changes the director of the movie
watch() - change the watched attribute to True and increase the total watched movies class attribute
(if the movie is not already watched)
__repr__() - returns "Movie name: {name}; Movie director: {director}. Total watched movies: {__watched_movies}"
'''