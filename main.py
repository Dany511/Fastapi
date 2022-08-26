from array import array
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import predict

app=FastAPI()

@app.get('/')
def home():
    return{"home":"wine prediction api"}

class StockIn(BaseModel):
    tenure:array



class StockOut(StockIn):
    forecast: array


@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    data = payload.data

    prediction_list = predict(tenure)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"forecast":prediction_list }
    return response_object