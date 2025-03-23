import os
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, data_path="data/chicken_data.csv"):
        self.data_path = data_path

    def load_data(self):
        try:
            logger.info("Loading dataset...")
            df = pd.read_csv(self.data_path)
            logger.info(f"Dataset loaded with shape {df.shape}")
            return df
        except Exception as e:
            raise CustomException(e, sys)
