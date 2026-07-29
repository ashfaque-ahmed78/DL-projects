"""
preprocess.py
-------------
Preprocess MRI image for Brain Tumor Detection.
"""

import numpy as np
from PIL import Image

IMG_SIZE = (224, 224)


def preprocess_image(uploaded_file):
    """
    Load and preprocess image for inference.

    Returns:
        image_array
        original_image
    """

    # Reset file pointer (important for Streamlit uploads)
    uploaded_file.seek(0)

    # Read image
    original_image = Image.open(uploaded_file).convert("RGB")

    # Resize
    image = original_image.resize(IMG_SIZE)

    # Convert to numpy
    image_array = np.array(image, dtype=np.float32)

    # IMPORTANT:
    # Do NOT divide by 255
    # This matches the notebook inference.
    image_array = np.expand_dims(image_array, axis=0)

    return image_array, original_image