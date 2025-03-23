import React, { useState } from "react";
import "./ImageUploader.css";

function ImageUploader() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
    setPrediction(null);
  };

  const handleUpload = async () => {
    if (!selectedImage) return;

    const formData = new FormData();
    formData.append("file", selectedImage);

    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error("Error uploading image:", error);
      setPrediction("Error: Unable to process image");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Chicken Disease Classifier</h1>
      <input type="file" onChange={handleImageChange} accept="image/*" />
      <button onClick={handleUpload} disabled={!selectedImage}>
        {loading ? "Processing..." : "Upload & Predict"}
      </button>
      {selectedImage && (
        <div className="image-preview">
          <img src={URL.createObjectURL(selectedImage)} alt="Preview" />
        </div>
      )}
      {prediction && <div className="result">Prediction: {prediction}</div>}
    </div>
  );
}

export default ImageUploader;
