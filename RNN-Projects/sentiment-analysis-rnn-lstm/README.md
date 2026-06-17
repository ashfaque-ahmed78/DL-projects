# 💬 Sentiment Analysis Using LSTM

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange.svg)
![LSTM](https://img.shields.io/badge/Model-LSTM-green.svg)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📌 Project Overview

This project implements a **Sentiment Analysis System** using **Deep Learning (LSTM - Long Short-Term Memory Networks)**.

The model analyzes textual data and predicts whether the sentiment expressed in the text is:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

The project demonstrates the practical application of **Natural Language Processing (NLP)** and **Recurrent Neural Networks (RNNs)** for text classification tasks.

---

# 🎯 Objectives

The main objectives of this project are:

✅ Understand Natural Language Processing (NLP)

✅ Learn Text Preprocessing Techniques

✅ Implement Deep Learning for Text Classification

✅ Build and Train an LSTM Network

✅ Predict Sentiment from User Input

✅ Deploy the Model through a Streamlit Application

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Neural Network API |
| NumPy | Numerical Computing |
| Pandas | Data Manipulation |
| Streamlit | Web Application |
| NLP Techniques | Text Processing |

---

# 📚 Deep Learning Concepts Used

This project covers:

### Recurrent Neural Networks (RNN)

RNNs are neural networks designed to process sequential data such as text and sentences.

### Long Short-Term Memory (LSTM)

LSTM is an advanced type of RNN capable of learning long-term dependencies in textual sequences.

### Word Embedding

Text is converted into numerical vectors before being passed to the neural network.

### Sequence Padding

All text sequences are padded to the same length for efficient training.

### Binary Classification

The model predicts the sentiment class based on learned textual patterns.

---

# 📂 Project Structure

```text
Sentiment-Analysis-LSTM/
│
├── README.md
├── Sentiment Analysis (LSTM).ipynb
├── app.py
├── model.h5
└── text.txt
```

---

# ⚙️ Workflow

### Step 1: Data Collection

Collect textual data containing sentiments.

↓

### Step 2: Data Preprocessing

- Lowercasing
- Removing unwanted characters
- Tokenization
- Sequence Encoding
- Padding

↓

### Step 3: Model Building

LSTM Architecture:

```python
Embedding Layer
        ↓
LSTM Layer
        ↓
Dense Layer
        ↓
Output Layer
```

↓

### Step 4: Model Training

The model learns sentiment patterns from textual sequences.

↓

### Step 5: Evaluation

Performance is measured using classification metrics.

↓

### Step 6: Prediction

The trained model predicts sentiment on unseen text.

---

# 🏗️ Model Architecture

```text
Input Text
     ↓
Tokenizer
     ↓
Sequence Conversion
     ↓
Padding
     ↓
Embedding Layer
     ↓
LSTM Layer
     ↓
Dense Layer
     ↓
Sigmoid Output
     ↓
Sentiment Prediction
```

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/Ashfaque-Ahmed786/sentiment-analysis-rnn-lstm.git
```

```bash
cd sentiment-analysis-rnn-lstm
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install tensorflow
pip install streamlit
pip install pandas
pip install numpy
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

---

# 💡 Example Predictions

### Positive Review

```text
This movie was amazing and I really enjoyed it.
```

Prediction:

```text
Positive 😊
```

---

### Negative Review

```text
The product quality was very poor and disappointing.
```

Prediction:

```text
Negative 😞
```

---

# 📈 Applications

This project can be used in:

- Social Media Monitoring
- Customer Feedback Analysis
- Product Review Analysis
- Movie Review Classification
- Brand Sentiment Tracking
- Opinion Mining Systems

---

# 🎓 Learning Outcomes

After completing this project, I gained practical experience in:

- Natural Language Processing (NLP)
- Text Preprocessing
- Deep Learning
- Recurrent Neural Networks (RNN)
- Long Short-Term Memory Networks (LSTM)
- TensorFlow & Keras
- Streamlit Deployment
- Model Training & Evaluation

---

# 🔮 Future Improvements

- Multi-Class Sentiment Analysis
- Attention Mechanism
- Bidirectional LSTM
- Transformer-Based Models
- Hugging Face Integration
- Real-Time Sentiment Prediction API

---

# 👨‍💻 Author

### Ashfaque Ahmed

Software Engineering Student  
Data Science & AI Enthusiast

🔗 GitHub:
https://github.com/Ashfaque-Ahmed786

🔗 LinkedIn:
https://www.linkedin.com/in/ashfaque-ahmed-917560324/

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🧠 Share feedback and suggestions

---

## 🙏 Thank You

Thank you for visiting this project.

Happy Coding! 🚀
