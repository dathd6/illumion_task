import numpy as np

MOVIE_FILE = 'movie.npy'
TIME_FILE = 'time.npy'

if __name__ == "__main__":
    df_m = np.load(MOVIE_FILE, mmap_mode='r')
    df_t = np.load(TIME_FILE)

    print(df_t[:10])
    print(df_m[:10])
