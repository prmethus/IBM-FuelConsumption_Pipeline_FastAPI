import os, json
from datetime import datetime
from utils import *
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import pandas as pd
import joblib

pipeline_path = os.path.join("Pipeline", "pipeline.pkl")
pipeline = joblib.load(pipeline_path)

API = FastAPI()


class Data(BaseModel):
    ENGINESIZE: int
    CYLINDERS: int
    FUELCONSUMPTION_CITY: float
    FUELCONSUMPTION_HWY: float
    FUELCONSUMPTION_COMB: float
    FUELCONSUMPTION_COMB_MPG: float


def save_request(data_dict, output):
    request_time = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    request_data = {request_time: {"data": data_dict, "output": output}}
    request_json = json.dumps(request_data)
    requests_data_json = os.path.join("Data", "requests.json")
    with open(requests_data_json, "a") as json_file:
        json_file.write(request_json)
        json_file.write("\n")


def prediction(data_dict):
    df_data = pd.DataFrame(data_dict, index=[0])
    output = pipeline.predict(df_data)
    return float(output[0])


# Server Definition
@API.get("/")
def root():
    return {"GoTo": "/docs"}


@API.post("/predict")
def prediction_request(request: Data):
    try:
        data_dict = request.dict()
        output = prediction(data_dict)
        save_request(data_dict, output)
        return {"output": output}
    except:
        raise HTTPException(
            status_code=418, detail="Exceptions can't be handheld by a teapot"
        )


if __name__ == "__main__":
    uvicorn.run(API, host="127.0.0.1", port=5000, log_level="info")
