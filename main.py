import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import os

app = FastAPI()

class Item(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float

model = tf.keras.models.load_model('./model/somethingidk.h5')

def predict(sl, sw, pl, pw):
    # sl = 5.8
    # sw = 2.6
    # pl = 4.0
    # pw = 1.2
    # should output 'Iris-versicolor'

    resmessage = "undefined"
    temp = np.array([[sl, sw, pl, pw]])
    result = model.predict(temp)
    clas = np.argmax(result)

    if (clas == 0):
        resmessage = "Iris-setosa"
    elif (clas == 1):
        resmessage = "Iris-versicolor"
    elif (clas == 2):
        resmessage = "Iris-virginica"
    else:
        resmessage = "undefined"

    return resmessage


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}

@app.post("/")
def add_item(item: Item):
    result = predict(item.sl, item.sw, item.pl, item.pw)
    return {result}

port = int(os.environ.get('PORT',8080))
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=port, timeout_keep_alive=1200)