# 🐔 Chicken Disease Classification – Backend (Flask + TensorFlow)

This project provides a Flask-based backend API for classifying chicken diseases from images using a deep learning model trained with TensorFlow/Keras.

---

## 📌 Features

- ✅ REST API built with Flask  
- ✅ Deep learning model integration (`.h5`)  
- ✅ Accepts chicken images and returns disease predictions  
- ✅ Scalable for deployment and frontend integration  
- ✅ Includes preprocessing pipeline for inference

---

## 📁 Project Structure

Chicken-Disease-Classification/
│
├── app.py # Main Flask app
├── requirements.txt # Python dependencies
├── artifacts/
│ └── model.h5 # Trained model file
├── temp/
│ └── (Uploaded images go here)
├── src/
│ └── pipelines/
│ └── predict_pipeline.py # Model loading and prediction logic

yaml
Copy
Edit

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Place the trained model
Put your trained model file (model.h5) into the artifacts/ folder.

🧠 Model Info
The model is trained to detect common chicken diseases.

Expected input: image (JPG/PNG)

Output: Predicted disease class (as a label)

📡 Running the Flask App
bash
Copy
Edit
python app.py
The server will start at http://127.0.0.1:5000

🔍 API Endpoint
POST /predict
✅ Request:
Form-data:

file: (image file)

🧪 Example using curl:
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/predict -F "file=@path_to_image.jpg"
📤 Response:
json
Copy
Edit
{
  "prediction": "Coccidiosis",
  "confidence": "98.23%"
}
🛠️ Tech Stack
Python 3.10+

Flask

TensorFlow / Keras

Pillow (PIL)

NumPy

📷 Sample Image Flow
User uploads an image.

Image saved to temp/ folder.

Model processes and predicts the class.

Result returned in JSON format.

