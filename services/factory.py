from services.sklearn_predictor import SklearnPredictor
from services.keras_predictor import KerasPredictor

class Factory:
    knn_predictor = None
    svm_rbf_predictor = None
    svm_linear_predictor = None
    keras_predictor = None

    def __init__(self):
        #if Factory.knn_predictor is None:
        #    Factory.knn_predictor = SklearnPredcitor("trainer/knn.joblib")
        #if Factory.svm_rbf_predictor is None:
        #    Factory.svm_rbf_predictor = SklearnPredcitor("trainer/svm_rbf.joblib")
        if Factory.svm_linear_predictor is None:
            Factory.svm_linear_predictor = SklearnPredictor("trainer/svm_linear.joblib")
        if Factory.keras_predictor is None:
            Factory.keras_predictor = KerasPredictor("trainer/keras.h5")

    def get_knn_predictor(self):
        return Factory.knn_predictor

    def get_svm_rbf_predictor(self):
        return Factory.svm_rbf_predictor

    def get_svm_linear_predictor(self):
        return Factory.svm_linear_predictor

    def get_keras_predictor(self):
        return Factory.keras_predictor