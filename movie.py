import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.widgets import Slider, RectangleSelector

from utils import format_time, get_random_color

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
        plt.subplots_adjust(bottom=0.15)

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
            label=f'{format_time(self.time[self.frame_index])}/'\
                  f'{format_time(self.time[-1])}',
            valmin=0,
            valmax=self.movie.shape[0] - 1,
            valinit=self.frame_index,
            valstep=1
        )

        self.selected_color = get_random_color()

        # Add rectangle selector for region selection
        self.selector = RectangleSelector(
            self.ax, 
            onselect=self.draw,
            useblit=True,
            spancoords='pixels',
            interactive=True,
            props = dict(
                facecolor=self.selected_color,
                edgecolor = self.selected_color,
                alpha=0.6,
                fill=True
            )
        )
        
        # Update the frame on scrolling
        self.frame_slider.on_changed(self.update_frame)

        plt.show()


    # Update the frame index based on the slider's position
    def update_frame(self, val):
        self.frame_index = int(val)
        
        # Update the displayed frame
        self.display.set_data(self.movie[self.frame_index])

        # Update the current time
        self.frame_slider.label.set_text(
            f'{format_time(self.time[self.frame_index])}/'\
            f'{format_time(self.time[-1])}'
        )
        
        # Redraw the figure canvas
        self.fig.canvas.draw_idle()
      

    # Draw shape on the image
    def draw(self, eclick, erelease):
        # Get the coordinates of the rectangle
        x1, y1 = int(eclick.xdata), int(eclick.ydata)
        x2, y2 = int(erelease.xdata), int(erelease.ydata)
        
        # Ensure coordinates are ordered correctly
        x_start, x_end = sorted([x1, x2])
        y_start, y_end = sorted([y1, y2])
        
        # Extract the region over all frames and calculate the mean intensity
        relative_intensity = self.calculate_mean_intensity(
                x_start,
                x_end,
                y_start,
                y_end
        )
        self.plot_relative_intensity(relative_intensity)

        self.selected_color = get_random_color()
        self.selector.set_props(
            facecolor=self.selected_color,
            edgecolor=self.selected_color,
        )


    # Calculate Mean Intensity
    def calculate_mean_intensity(self, x_start, x_end, y_start, y_end):
        # Extract pixel values within the rectangle for each frame
        region_intensities = [
            self.movie[frame, y_start:y_end, x_start:x_end].mean()
            for frame in range(self.movie.shape[0])
        ]
        
        # Normalize to the first value
        initial_intensity = region_intensities[0]
        relative_intensities = [intensity / initial_intensity \
                                for intensity in region_intensities]
        return relative_intensities
    

    # Plot relative intensity
    def plot_relative_intensity(self, relative_intensities):
        # Create a new figure for intensity plot
        _, ax = plt.subplots()
        
        # Plot the relative intensity
        ax.plot(self.time, relative_intensities, label="Relative Intensity", color=self.selected_color)
        ax.set_ylabel("Relative Intensity (%)")
        ax.set_xlabel("Time (HH:MM:SS)")
        ax.legend()
        
        # Limit to a maximum of 6 ticks on the x-axis
        num_ticks = min(6, len(self.time))
        tick_indices = np.linspace(0, len(self.time) - 1, num_ticks, dtype=int)
        ax.set_xticks(self.time[tick_indices])
        ax.set_xticklabels([format_time(self.time[i]) for i in tick_indices])

        # Limit to a maximum of 10 ticks on the y-axis
        num_ticks = min(10, len(relative_intensities))
        tick_values = np.linspace(np.min(relative_intensities), 
                                  np.max(relative_intensities),
                                  num_ticks)
        ax.set_yticklabels([f'{i * 100:.1f}%' for i in tick_values])

        # Show the plot
        plt.show()

