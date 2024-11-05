import matplotlib.pyplot as plt

class Movie:
    def __init__(self, movie, time):
        self.movie = movie
        self.time = time
        self.fig, self.ax = plt.subplots(figsize=(8, 6))

    # Visualize the movie by going through images over period of time 
    def visualize(self):
        pass

    # Draw shape on the image
    def draw(self, shape='rectangle', color='#7CAE00'):
        pass

    # Plot relative intensity
    def plot_relative_intensity(self, draw, color):
        pass

