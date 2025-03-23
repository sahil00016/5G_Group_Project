import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ModelTrainer:
    def __init__(self):
        self.model = Sequential([
            Flatten(input_shape=(64, 64, 3)),
            Dense(128, activation="relu"),
            Dense(64, activation="relu"),
            Dense(5, activation="softmax")
        ])

    def compile_model(self):
        logger.info("Compiling model...")
        self.model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    def train(self, X_train, y_train, X_val, y_val, epochs=10):
        logger.info("Starting training...")
        self.model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs)
        logger.info("Training complete!")

    def save_model(self, model_path="src/models/chicken_disease_model.h5"):
        self.model.save(model_path)
        logger.info(f"Model saved at {model_path}")
        print("✅ Model saved successfully!")


# 🟢 ADD THIS BLOCK TO ACTUALLY TRAIN AND SAVE THE MODEL
if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.compile_model()
    
    # 🔴 YOU NEED TO LOAD YOUR TRAINING DATA HERE
    # Example (replace with actual data loading)
    import numpy as np
    X_train = np.random.rand(100, 64, 64, 3)  # Dummy data
    y_train = np.random.randint(0, 5, 100)  # Dummy labels
    X_val = np.random.rand(20, 64, 64, 3)
    y_val = np.random.randint(0, 5, 20)

    trainer.train(X_train, y_train, X_val, y_val)
    trainer.save_model()
