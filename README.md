# IBM-FuelConsumption_Pipeline_FastAPI
A complete end to end Data Science project on IBM'S Fuel Consumption dataset.

Data/FuelConsumption.csv contains the Fuel Consumption dataset.  
train.ipynb contains the IPython Notebook where I performed Data Analysis and trained the ML pipeline.  
Pipeline/pipeline.pkl contains the ML pipeline (XGBRegressor was used for training the model).  
transformations.txt contain info about which columns were dropped and added.  
utils.py contains the custom feature_engineering Transformer class, which is used in the Pipeline.  
api.py contains the code for deploying the ML pipeline with FastAPI.  
