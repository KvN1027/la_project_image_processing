# -*- coding: utf-8 -*-
"""
Edge Detection with Laplacian Kernel
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
from scipy.ndimage import convolve

# Laplacian edge detection kernel
laplacian_kernel = np.array([[-1, -1, -1],
                             [-1,  8, -1],
                             [-1, -1, -1]])

# Read the original image
image_path = 'meowmeow.jpg'  # Replace with your image path
image = mpimg.imread(image_path)
if image.ndim == 3 and image.shape[2] == 3:
    # Convert image to grayscale if it's color
    image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

# Apply Laplacian kernel to the grayscale image for edge detection
edges = convolve(image, laplacian_kernel)

# Ensure the pixel values are properly scaled
edges = np.clip(edges, 0, 255).astype(np.uint8)

# Save the edge-detected image without axis
fig, ax = plt.subplots()
ax.imshow(edges, cmap='gray')
ax.axis('off')  # Turn off the axis
plt.savefig('edge_detected_image.png', bbox_inches='tight', pad_inches=0)
plt.close(fig)  # Close the figure to free up memory
