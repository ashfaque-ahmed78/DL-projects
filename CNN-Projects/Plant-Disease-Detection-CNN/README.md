# 🌿 Plant Disease Prediction using Deep Learning (CNN + Streamlit)

## 📌 Overview
This project is a **Deep Learning-based Web Application** that detects plant diseases from leaf images using a **Convolutional Neural Network (CNN)**.  

Users can simply upload an image of a plant leaf, and the system will instantly predict the disease along with a **confidence score**.  

The goal of this project is to bring **Artificial Intelligence 🤖 into Agriculture 🌱** for early disease detection and better crop management.

---

## 🚀 Features
- 📤 Upload plant leaf images for prediction  
- 🧠 CNN-based deep learning model for image classification  
- ⚡ Real-time disease detection with confidence score  
- 🌐 Interactive and user-friendly Streamlit web app  
- 📊 Fast and accurate predictions  
- 🌿 Supports multiple plant disease categories  

---

## 🛠️ Technologies Used
- 🐍 Python  
- 🔥 TensorFlow / Keras  
- 📦 NumPy  
- 🖼️ Pillow (PIL)  
- 🌐 Streamlit  
- 📊 Matplotlib (optional for visualization)  

---

## 📁 Project Structure
Plant-Disease-Prediction/
│
├── app.py # Streamlit web application
├── model.h5 # Trained CNN model
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── dataset/ # Training dataset (if included)
├── notebooks/ # Jupyter notebooks for training
└── utils/ # Helper functions (if any)


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/plant-disease-prediction.git
cd plant-disease-prediction
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the Streamlit app
streamlit run app.py
📷 How It Works
User uploads a plant leaf image 🌿
Image is preprocessed (resize, normalize) 🖼️
CNN model analyzes features 🧠
Model predicts disease category 📊
Output is displayed with confidence score ⚡
🎯 Sample Output
Prediction: Tomato Leaf Bacterial Spot
Confidence: 94.32%
📈 Model Performance
High accuracy CNN model trained on plant disease dataset
Optimized for real-time predictions
Good generalization on unseen images
🌍 Impact

This project shows how AI can revolutionize agriculture 🌱 by:

Reducing crop loss
Helping farmers detect diseases early
Improving productivity
Providing affordable AI-based farming tools
🔮 Future Improvements
☁️ Deploy on cloud (AWS / Render / HuggingFace)
📷 Add real-time camera detection
📱 Mobile-friendly version
🧠 Improve accuracy with advanced architectures (ResNet, EfficientNet)
🌿 Expand dataset for more plant species
🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Ashfaque Ahmed
💡 Passionate about AI, Machine Learning, and Computer Vision
