import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import json

# ------------------------------
# Setup paths
# ------------------------------
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = r"C:\Users\Hp\OneDrive\Desktop\CNN Plants Diseases Prediction ..Deep Learning\app\trained_model\model_small.h5"
class_indices_path = os.path.join(working_dir, "class_indices.json")

# ------------------------------
# Load model and class indices
# ------------------------------
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

@st.cache_data
def load_class_indices():
    try:
        with open(class_indices_path, "r") as f:
            class_indices = json.load(f)
        return class_indices
    except Exception as e:
        st.error(f"Error loading class indices: {e}")
        return None

model = load_model()
class_indices = load_class_indices()

# ------------------------------
# Preprocess image
# ------------------------------
def load_and_preprocess_image(image, target_size=(224, 224)):
    img = image.convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    return img_array

# ------------------------------
# Predict function
# ------------------------------
def predict_image_class(model, image, class_indices):
    try:
        preprocessed_img = load_and_preprocess_image(image)
        predictions = model.predict(preprocessed_img)
        predicted_index = np.argmax(predictions, axis=1)[0]
        predicted_class = class_indices[str(predicted_index)]
        confidence = predictions[0][predicted_index]
        return predicted_class, confidence
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None, None

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Plant Disease Prediction", layout="centered")
st.title("🌿 Plant Disease Prediction App")
st.write("Upload a leaf image and the model will predict its disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        st.write("Predicting…")
        with st.spinner("Model is predicting…"):
            predicted_class, confidence = predict_image_class(model, image, class_indices)
        
        if predicted_class:
            st.success(f"Predicted Class: **{predicted_class}**")
            st.info(f"Confidence: {confidence*100:.2f}%")
    except Exception as e:
        st.error(f"Error processing image: {e}")