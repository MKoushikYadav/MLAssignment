from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def predict_brain(number):
    """Predicts weight of brain in grams for size of head in cubic centimeter which is provided using linear regression."""

    data = pd.read_csv("headbrain6.csv")
    if number >=441: 
        x=data.iloc[:,2:3].values
        y=data.iloc[:,3:4].values
        model = LinearRegression()
        model.fit(x,y)
        prediction =model.predict([[number]])
        return int(prediction)
    else: return number

@app.route("/", methods=["POST"])
def predict():
    """Returns the predicted value of the brain weight"""
    number = request.json["number"]
    return {"prediction": predict_brain(number)}

if __name__ == "__main__":
    app.run(debug=True)
