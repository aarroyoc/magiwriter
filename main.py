from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from models.prediction import RequestPrediction
from usecases.predict_image import predict_image

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.post("/api/mnist")
def predict_mnist(request_prediction: RequestPrediction):
    prediction = predict_image(request_prediction)
    return {"prediction": prediction}