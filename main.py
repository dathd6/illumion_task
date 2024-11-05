import numpy as np

from movie import Movie

MOVIE_FILE = 'movie.npy'
TIME_FILE = 'time.npy'

if __name__ == "__main__":
    df_m = np.load(MOVIE_FILE, mmap_mode='r')
    df_t = np.load(TIME_FILE)

    movie_player = Movie(movie=df_m, time=df_t)
    movie_player.visualize()
