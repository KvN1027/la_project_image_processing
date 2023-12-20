# -*- coding: utf-8 -*-
"""
Create a larger Gaussian Kernel with a higher standard deviation for more blur
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from scipy import signal

# Set the size of the Gaussian kernel and standard deviation
kernel_size = 49  # A larger kernel size
sigma = 10  # A higher standard deviation for more blur

# Create Gaussian filter
ax = np.linspace(-(kernel_size - 1) / 2., (kernel_size - 1) / 2., kernel_size)
x, y = np.meshgrid(ax, ax)
gaussian_kernel = np.exp(-0.5 * (np.square(x) + np.square(y)) / np.square(sigma))
gaussian_kernel = gaussian_kernel / np.sum(gaussian_kernel)  # Normalization

# Read the original image
image_path = 'meowmeow.jpg'  # Replace with your image path
image = mpimg.imread(image_path)

# Save the original image without axis
fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('off')  # Turn off the axis
plt.savefig('original_image.png', bbox_inches='tight', pad_inches=0)
plt.close(fig)  # Close the figure to free up memory

# Apply Gaussian filter (convolution) to each channel
red = signal.convolve2d(image[:,:,0], gaussian_kernel, boundary='symm', mode='same')
green = signal.convolve2d(image[:,:,1], gaussian_kernel, boundary='symm', mode='same')
blue = signal.convolve2d(image[:,:,2], gaussian_kernel, boundary='symm', mode='same')

# Stack the channels back into a 3D array
blurred_image = np.stack([red, green, blue], axis=2)

# Ensure the pixel values are properly scaled
blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8)

# Save the blurred image without axis
fig, ax = plt.subplots()
ax.imshow(blurred_image)
ax.axis('off')  # Turn off the axis
plt.savefig('enhanced_blurred_image-less.png', bbox_inches='tight', pad_inches=0)
plt.close(fig)  # Close the figure to free up memory
