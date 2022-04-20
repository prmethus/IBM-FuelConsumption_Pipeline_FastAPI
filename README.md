# IBM-FuelConsumption_Pipeline_FastAPI

A complete end to end Data Science project on IBM'S Fuel Consumption dataset. <br> <br>

### Docker

Dockerized Version (Runs the API): https://hub.docker.com/repository/docker/prmethus/fuel_consumption_prediction

### Description

1. Data/FuelConsumption.csv contains the Fuel Consumption dataset.  <br>
2. train.ipynb contains the IPython Notebook where I performed Data Analysis and trained the ML pipeline.  <br>
3. Pipeline/pipeline.pkl contains the ML pipeline (XGBRegressor was used for training the model).  <br>
4. transformations.txt contain info about which columns were dropped and added.  <br>
5. utils.py contains the custom feature_engineering Transformer class, which is used in the Pipeline.  <br>
6. api.py contains the code for deploying the ML pipeline with FastAPI.  <br>
