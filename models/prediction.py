from enum import Enum

from pydantic import BaseModel

class Algorithm(str, Enum):
    knn = "knn"
    svm_linear = "svm_linear"
    svm_rbf = "svm_rbf"
    keras = "keras"

class RequestPrediction(BaseModel):
    algorithm: Algorithm
    image: str