# 🧠 Brain Tumor Detection AI using Deep Learning

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow">

<img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">

<img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv">

<img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap">

<img src="https://img.shields.io/badge/Plotly-Interactive_Charts-blueviolet?style=for-the-badge&logo=plotly">

<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">

</p>

---

# 📌 Project Overview

Brain Tumor Detection AI is an end-to-end Deep Learning web application that automatically classifies Brain MRI images into one of four categories using an EfficientNetB0 Transfer Learning model.

The project provides a complete AI-powered healthcare workflow, including image preprocessing, deep learning inference, probability visualization, disease information, and downloadable PDF reports through a modern Flask web application.

This project demonstrates practical implementation of Computer Vision, Transfer Learning, Medical Image Classification, and Full-Stack AI deployment.

---

# 🎯 Objectives

- Detect brain tumors from MRI images.
- Build an end-to-end Deep Learning pipeline.
- Develop a modern Flask web application.
- Visualize prediction confidence.
- Generate downloadable AI medical reports.
- Demonstrate production-ready AI deployment.

---

# 🧠 Tumor Classes

The model classifies MRI images into four categories:

| Class | Description |
|--------|-------------|
| 🧠 Glioma | Tumor originating from glial cells |
| 🧠 Meningioma | Tumor developing from brain membranes |
| 🧠 Pituitary | Tumor affecting the pituitary gland |
| ✅ No Tumor | Healthy brain MRI |

---

# ✨ Key Features

- Deep Learning Brain Tumor Classification
- EfficientNetB0 Transfer Learning
- TensorFlow/Keras Model
- Flask Web Application
- Bootstrap Responsive UI
- MRI Image Upload
- AI Prediction Dashboard
- Confidence Score
- Probability Analysis
- Disease Information Panel
- Medical Disclaimer
- PDF Report Generation
- Responsive Design
- GitHub Portfolio Ready

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Deep Learning

- TensorFlow
- Keras
- EfficientNetB0

## Computer Vision

- OpenCV
- Pillow
- NumPy

## Backend

- Flask

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Visualization

- Plotly

## PDF Generation

- ReportLab

---

# 📂 Dataset

**Dataset:** Brain Tumor MRI Dataset

The dataset contains MRI brain images divided into four categories.

### Classes

- Glioma
- Meningioma
- Pituitary
- No Tumor

### Image Size

224 × 224 pixels

---

# 🏗️ Deep Learning Architecture

The project uses Transfer Learning with **EfficientNetB0**.

Pipeline:

MRI Image

↓

Image Preprocessing

↓

EfficientNetB0 Feature Extraction

↓

Global Average Pooling

↓

Dense Layers

↓

Softmax Classification

↓

Prediction

---

# 📊 Model Performance

The trained model achieved the following performance during evaluation.

| Metric | Score |
|---------|-------|
| Test Accuracy | **88.25%** |
| Precision | **89.31%** |
| Recall | **87.69%** |

---

# 📈 Classification Report

| Class | Precision | Recall | F1 Score |
|--------|----------:|-------:|---------:|
| Glioma | 88.29% | 73.50% | 80.22% |
| Meningioma | 83.17% | 82.75% | 82.96% |
| No Tumor | 88.84% | 99.50% | 93.87% |
| Pituitary | 92.40% | 97.25% | 94.76% |

---

# 📁 Project Structure

```text
Brain-Tumor-Detection-AI/

│── app.py

│── requirements.txt

│── README.md

│

├── model/

│ └── brain_tumor_ai_final.keras

│

├── utils/

│ ├── predictor.py

│ ├── preprocess.py

│ └── report_generator.py

│

├── templates/

│ ├── index.html

│ └── result.html

│

├── static/

│ ├── css/

│ ├── uploads/

│ └── reports/

│
---

# 📸 Application Screenshots

> **Note:** Add screenshots of your application inside a `screenshots` folder in the project root.

## 🏠 Home Page

![Home Page](screenshots/home_page.png)

---

## 🧠 AI Prediction Dashboard

![Prediction Result](screenshots/prediction_result.png)

---

## 📊 Probability Analysis

![Probability Chart](screenshots/probability_chart.png)

---

## 📄 AI Medical Report (PDF)

![PDF Report](screenshots/pdf_report.png)

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Brain-Tumor-Detection-AI.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd Brain-Tumor-Detection-AI
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🚀 How to Use

### Step 1

Open the web application.

---

### Step 2

Upload a Brain MRI image.

---

### Step 3

Click

```
🔍 Analyze MRI
```

---

### Step 4

The AI model will display:

- Predicted Class
- Confidence Score
- Probability Distribution
- Disease Information
- Medical Disclaimer

---

### Step 5

Download the AI-generated medical report as a PDF.

---

# 📄 AI Medical Report

The application automatically generates a downloadable PDF report containing:

- Uploaded MRI Image
- Predicted Tumor Class
- Confidence Percentage
- Class Probability Analysis
- AI Model Information
- Medical Disclaimer

---

# 🌐 Deployment

The project is deployment-ready and can be hosted on:

- Render
- Railway
- PythonAnywhere
- Azure App Service
- AWS Elastic Beanstalk

---

# 📦 Project Workflow

```text
Brain MRI Image
        │
        ▼
Image Upload
        │
        ▼
Image Preprocessing
        │
        ▼
EfficientNetB0 Model
        │
        ▼
Softmax Prediction
        │
        ▼
Probability Analysis
        │
        ▼
Disease Information
        │
        ▼
PDF Report Generation
```

---

# 🎯 Real-World Applications

- Medical Imaging
- Computer Vision
- Healthcare AI
- Clinical Decision Support
- Medical Research
- AI-assisted Diagnosis
- Educational Demonstration
- Deep Learning Portfolio Project

---

# 🔮 Future Improvements

- Grad-CAM Visualization
- DICOM Image Support
- Multi-language Interface
- User Authentication
- Prediction History
- Cloud Database Integration
- Doctor Dashboard
- REST API
- Docker Deployment
- Mobile Application
- Explainable AI (XAI)
- Model Monitoring

---

# ⚠️ Medical Disclaimer

This application is developed for **educational and research purposes only**.

The predictions generated by the AI model **must not** be considered a substitute for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional before making medical decisions.

---

# 👨‍💻 Author

**Ashfaque Ahmed**

Software Engineering Student

AI & Machine Learning Engineer

Pakistan 🇵🇰

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest improvements

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

Special thanks to:

- TensorFlow
- Keras
- Flask
- Bootstrap
- Plotly
- ReportLab
- Kaggle
- Open Source Community

---

<p align="center">

Made with ❤️ using TensorFlow, Flask & Deep Learning

</p>

<p align="center">

⭐ If you like this project, don't forget to star the repository!

</p>

└── screenshots/
```
