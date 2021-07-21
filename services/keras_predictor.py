import numpy as np
import tensorflow as tf

class KerasPredictor:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, pic):
        pixels = np.reshape(pic, (28, 28, 1))
        return np.argmax(self.model.predict(np.array([pixels,]))[0])