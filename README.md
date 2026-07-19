# 🌿 Plant Disease Detection System

An AI-powered web application that detects plant diseases from leaf images using Deep Learning and TensorFlow. Users can upload an image of a plant leaf, and the model predicts the disease along with the confidence score.

---

## 📌 Features

- 🌱 Detects plant diseases from leaf images
- 🧠 Deep Learning model built using TensorFlow/Keras
- 📷 Upload image through an interactive Streamlit interface
- 📊 Displays predicted disease with confidence percentage
- 🎨 User-friendly interface with custom background and styling

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow
- OpenCV
- Matplotlib

---

## 📂 Project Structure

```
PlantDiseaseDetection/
│
├── app.py                     # Streamlit application
├── predict.py                 # Prediction logic
├── train_model.py             # Model training script
├── utils.py                   # Utility functions
├── requirements.txt           # Project dependencies
├── README.md
│
├── assets/
│   └── bg.png                 # Background image
│
├── model/
│   └── plant_model.keras      # Trained deep learning model
│
├── dataset/
│   ├── train/
│   └── valid/
│
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/reshamss/PlantDiseaseDetection.git
```

Navigate to the project directory:

```bash
cd PlantDiseaseDetection
```

---

### 2. Create a Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

If the above command doesn't work, run:

```bash
python -m streamlit run app.py
```

The application will automatically open in your browser.

If it doesn't open automatically, visit:

```
http://localhost:8501
```

---

## 📷 How to Use

1. Launch the application.
2. Click **Browse Files**.
3. Upload a plant leaf image (.jpg, .jpeg or .png).
4. Wait for the prediction.
5. View:
   - Predicted Disease
   - Confidence Score

---

## 🧠 Model Details

- Framework: TensorFlow / Keras
- Input Image Size: **224 × 224**
- Output: Plant Disease Class
- Confidence Score: Probability of the predicted class

---

## 📋 Requirements

- Python 3.10 or 3.11 (Recommended)
- pip

Required Python packages are listed in **requirements.txt**.

---

## 📸 Sample Output

The application displays:

- Uploaded leaf image
- Predicted disease
- Confidence percentage
- Progress bar representing prediction confidence

---

## 📈 Future Enhancements

- Support for multiple image uploads
- Disease treatment recommendations
- Mobile responsive interface
- Cloud deployment
- Real-time camera prediction

---

## 👩‍💻 Author

**Resham Shinalkar**

- GitHub: https://github.com/reshamss

---

## 📄 License

This project is developed for educational and learning purposes.
