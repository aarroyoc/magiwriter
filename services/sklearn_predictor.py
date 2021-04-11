from joblib import load

class SklearnPredcitor():
    def __init__(self, path):
        self.model = load(path)

    def predict(self, pic):
        pixels = pic.reshape(1, -1)
        return self.model.predict(pixels)[0]