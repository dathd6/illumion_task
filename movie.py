import matplotlib.pyplot as plt
from  matplotlib.widgets import Slider

from utils import format_time

SLIDER_SIZE = (0.25, 0.1, 0.5, 0.03)

class Movie:
    def __init__(self, movie, time):
        self.movie = movie
        self.time = time
        self.frame_index = 0
        self.fig, self.ax = plt.subplots()

    # Visualize the movie by going through images over period of time 
    def visualize(self):
        # Make room for the time axis
        plt.subplots_adjust(bottom=0.2)

        # Display the movie (first frame)
        self.display = self.ax.imshow(
            self.movie[self.frame_index],
            vmin=0,
            vmax=4095
        )
        self.ax.set_title(
            f"Movie Presented by Illumion"
        )
        self.ax.axis('off') # Remove original axis

        # Add time slider
        ax_slider = self.fig.add_axes(SLIDER_SIZE)
        self.frame_slider = Slider(
            ax=ax_slider,
            label=f'''{format_time(self.time[self.frame_index])}/
                  {format_time(self.time[-1])}''',
            valmin=0,
            valmax=self.movie.shape[0] - 1,
            valinit=self.frame_index,
            valstep=1
        )
        
        # Update the frame on scrolling
        self.frame_slider.on_changed(self.update_frame)

        plt.show()

    def update_frame(self, val):
        # Update the frame index based on the slider's position
        self.frame_index = int(val)
        
        # Update the displayed frame
        self.display.set_data(self.movie[self.frame_index])

        # Update the current time
        self.frame_slider.label.set_text(
            f'''{format_time(self.time[self.frame_index])}/
            {format_time(self.time[-1])}'''
        )
        
        # Redraw the figure canvas
        self.fig.canvas.draw_idle()


    # Draw shape on the image
    def draw(self, shape='rectangle', color='#7CAE00'):
        pass

    # Plot relative intensity
    def plot_relative_intensity(self, draw, color):
        pass

