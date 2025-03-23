import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from src.utils.logger import get_logger

logger = get_logger(__name__)

class PredictPipeline:
    def __init__(self, model_path="src/models/chicken_disease_model.h5"):
        self.model = tf.keras.models.load_model("src/models/chicken_disease_model.h5")


    def predict(self, img_path):
        logger.info(f"Predicting for {img_path}...")
        img = image.load_img(img_path, target_size=(64, 64))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = self.model.predict(img_array)
        logger.info(f"Prediction: {prediction}")
        return prediction
