from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
from scipy.ndimage import convolve

app = Flask(__name__)

def convert_to_base64(image):
    """Convert an image to Base64 string."""
    image_pil = Image.fromarray(image)
    buffered = BytesIO()
    image_pil.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()


def apply_laplacian_edge_detection(image):
    """Apply Laplacian edge detection to an image."""
    laplacian_kernel = np.array([[-1, -1, -1],
                                 [-1,  8, -1],
                                 [-1, -1, -1]])

    if image.ndim == 3 and image.shape[2] == 3:
        # Convert image to grayscale
        image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    
    edges = convolve(image, laplacian_kernel)
    edges = np.clip(edges, 0, 255).astype(np.uint8)
    return edges

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        # Read the image file
        in_memory_file = BytesIO()
        file.save(in_memory_file)
        data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, cv2.IMREAD_COLOR)

        # Convert from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Apply Gaussian Blur
        kernel_size = 49  # Positive odd number
        sigma = 10
        blurred_image = cv2.GaussianBlur(image_rgb, (kernel_size, kernel_size), sigma)

        # Convert images to Base64 strings
        original_image_base64 = convert_to_base64(image_rgb)
        blurred_image_base64 = convert_to_base64(blurred_image)

        edge_detected_image = apply_laplacian_edge_detection(image_rgb)
    edge_detected_image_base64 = convert_to_base64(edge_detected_image)

    # Return the images as JSON
    return jsonify({
        'original_image': original_image_base64,
        'blurred_image': blurred_image_base64,
        'edge_detected_image': edge_detected_image_base64
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
