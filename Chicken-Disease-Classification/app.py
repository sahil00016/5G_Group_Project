import os
from flask import Flask, request, jsonify
from PIL import Image
from src.pipelines.predict_pipeline import PredictPipeline
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow all domains to access the API
predictor = PredictPipeline()

# Ensure temp directory exists
os.makedirs("temp", exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Chicken Disease Classification API Running!"})

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    # Check if the file is an image
    try:
        img = Image.open(file)
        img.verify()  # Verify that the file is an actual image
        file.seek(0)  # Reset file pointer
    except Exception as e:
        return jsonify({"error": f"Invalid image file: {str(e)}"}), 400

    # Save file to temp directory
    file_path = f"temp/{file.filename}"
    file.save(file_path)
    print(f"[INFO] File saved at: {file_path}")

    # Ensure the model is loaded
    if not predictor:
        return jsonify({"error": "Prediction model is not initialized"}), 500
    
    # Run prediction
    try:
        prediction = predictor.predict(file_path)
        print(f"[INFO] Prediction result: {prediction}")
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
