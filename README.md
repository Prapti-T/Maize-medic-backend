# MaizeMedic: A CNN-Based Maize Leaf Disease Detection System

MaizeMedic is a deep learning-based application built with Python and PyTorch to classify maize leaf diseases into four categories. The system aims to assist farmers and agricultural professionals in the early detection and prevention of crop diseases through image-based analysis.
This is the backend part of the project.
---

## Features

- Disease classification into 4 categories:
  - Common Rust  
  - Gray Leaf Spot  
  - Northern Leaf Blight  
  - Healthy (Normal)
- Custom CNN model built using PyTorch
- Data preprocessing and augmentation for improved generalization
- Hyperparameter tuning for better model performance
- Django REST API integration for backend deployment

---

## Tech Stack
- Python  
- PyTorch  
- Django 

---

## Dataset

The dataset includes images of maize leaves labeled in four categories. It was preprocessed (resized, normalized) and augmented (rotation, flipping, etc.) to improve model robustness and reduce overfitting.

> **Note:** The dataset is a subset of the [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease) dataset.

---

## Model Performance

- **Train/Test Split:** 80/20  
- **Achieved Accuracy:** 85%+  
- **Evaluation Metrics:**
  - Accuracy
  - Loss Curves
  - Confusion Matrix

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MaizeMedic.git
cd MaizeMedic
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Run the Django API

```bash
cd backend
python manage.py runserver
```

### 4. Test the API

Use Postman or cURL to send POST requests with image files to the appropriate endpoint.

---
