import base64
from io import BytesIO

from PIL import Image
import numpy as np

from models.prediction import Algorithm
from services.factory import Factory

def predict_image(request_prediction):
    factory = Factory()

    # decode image
    base64img = request_prediction.image.split(",")[1]
    im = Image.open(BytesIO(base64.b64decode(base64img))).convert("L")
    pic = np.array(im)

    # remove unneeded image
    idx = np.argwhere(np.all(pic[..., :] == 0, axis=1))
    pic = np.delete(pic, idx, axis=0)
    idx = np.argwhere(np.all(pic[..., :] == 0, axis=0))
    pic = np.delete(pic, idx, axis=1)
    im = Image.fromarray(pic)

    # resize to 20xAUTO or AUTOx20
    if pic.shape[0] > pic.shape[1]:
        size = (int(pic.shape[1]*20/pic.shape[0]), 20)
    else:
        size = (20, int(pic.shape[0]*20/pic.shape[1]))
    im = im.resize(size, Image.LANCZOS)
    pic = np.array(im)

    # paste small image into 28x28
    img = Image.new("L", (28, 28))
    img.paste(im, box=(int(14-im.size[0]/2), int(14-im.size[1]/2)))
    final_pic = np.array(img)
    
    if request_prediction.algorithm == Algorithm.svm_linear:
        predictor = factory.get_svm_linear_predictor()
        return str(predictor.predict(final_pic))
    elif request_prediction.algorithm == Algorithm.svm_rbf:
        return "disabled"
    elif request_prediction.algorithm == Algorithm.knn:
        return "disabled"
    else:
        raise NotImplementedError()
