"""
This file defines the server
and the class we use to predict using our trained classifier

We will put the two into one file to save some time for the tutorial.
In practice make sure to have them in separate classes.
"""
import numpy as np
from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier


# Define object we classify
class PersonInformation(BaseModel):
    sex: str
    pclass: int


class SurvivePredictor:
    """
    Holds the actual process of doing the prediction
    """

    def __init__(self):
        self.clf: DecisionTreeClassifier = load("./model_weights/clf.bin")

    def predict(self, item: PersonInformation):
        # make sure that here the order is the same as in the model training
        print("item:", item)
        x = np.array([1 if item.sex == "female" else 0, item.pclass])
        x = x.reshape(1, -1)
        # be careful to only transform and not fit
        print("numeric representation:", x)
        y = self.clf.predict_proba(x)
        print("survival probability:", y)
        # y looks now like: [[0.78 0.21]] so the second number is probability of survived
        return y[0][1]


app = FastAPI()
predictor = SurvivePredictor()


# Server Definition
@app.get("/")
def root():
    return {"GoTo": "/docs"}


@app.post("/will_survive")
def is_user_item(request: PersonInformation):
    try:
        return {"survival_probability": predictor.predict(request)}
    except:
        raise HTTPException(status_code=418, detail="Exceptions can't be handheld by a teapot")
