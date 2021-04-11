from services.sklearn_predictor import SklearnPredcitor

class Factory:
    knn_predictor = None
    svm_rbf_predictor = None
    svm_linear_predictor = None

    def __init__(self):
        #if Factory.knn_predictor is None:
        #    Factory.knn_predictor = SklearnPredcitor("trainer/knn.joblib")
        #if Factory.svm_rbf_predictor is None:
        #    Factory.svm_rbf_predictor = SklearnPredcitor("trainer/svm_rbf.joblib")
        if Factory.svm_linear_predictor is None:
            Factory.svm_linear_predictor = SklearnPredcitor("trainer/svm_linear.joblib")

    def get_knn_predictor(self):
        return Factory.knn_predictor

    def get_svm_rbf_predictor(self):
        return Factory.svm_rbf_predictor

    def get_svm_linear_predictor(self):
        return Factory.svm_linear_predictor