"""
predictor.py
-------------
Load trained model and predict MRI images.
"""

import os
import numpy as np
import tensorflow as tf

# ----------------------------------------------------
# Model Path
# ----------------------------------------------------

MODEL_PATH = os.path.join(
    "model",
    "brain_tumor_ai_final.keras"
)
# ----------------------------------------------------
# Class Names
# ----------------------------------------------------

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------

print("=" * 60)
print("Loading Model...")
print(os.path.abspath(MODEL_PATH))

model = tf.keras.models.load_model(MODEL_PATH)

print("Model Loaded Successfully!")
print("=" * 60)

# ----------------------------------------------------
# Prediction Function
# ----------------------------------------------------

def predict_image(image_array):

    print("\n" + "=" * 60)
    print("IMAGE INFORMATION")
    print("=" * 60)

    print("Shape :", image_array.shape)
    print("Dtype :", image_array.dtype)
    print("Minimum Pixel :", np.min(image_array))
    print("Maximum Pixel :", np.max(image_array))

    # ------------------------------------------------

    prediction = model.predict(image_array, verbose=0)

    print("\nRAW MODEL OUTPUT")
    print(prediction)

    probabilities = prediction[0]

    print("\nCLASS PROBABILITIES")

    for i, class_name in enumerate(CLASS_NAMES):
        print(f"{class_name:12} : {probabilities[i]*100:.2f}%")

    # ------------------------------------------------

    predicted_index = np.argmax(probabilities)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(probabilities[predicted_index] * 100)

    print("\nFINAL PREDICTION")
    print("Predicted :", predicted_class)
    print("Confidence:", confidence)

    print("=" * 60)

    return predicted_class, confidence, probabilities