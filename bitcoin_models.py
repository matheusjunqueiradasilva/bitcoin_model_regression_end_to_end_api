# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

model = load_model("bitcoin_models")

class BitcoinInput(BaseModel):
    open: float
    high: float
    low: float
    volume: float
    number_of_trades: float
    taker_buy_base_asset_volume: float
    taker_buy_quote_asset_volume: float

class BitcoinOutput(BaseModel):
    prediction: float

@app.post("/predict", response_model=BitcoinOutput)
def predict(data: BitcoinInput):
    data_df = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data_df)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)