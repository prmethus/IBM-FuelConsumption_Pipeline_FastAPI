import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class feature_engineering(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return self.transform_fuel_data(X)

    def transform_fuel_data(self, data):
        input_columns = [
            "ENGINESIZE",
            "CYLINDERS",
            "FUELCONSUMPTION_CITY",
            "FUELCONSUMPTION_HWY",
            "FUELCONSUMPTION_COMB",
            "FUELCONSUMPTION_COMB_MPG",
        ]
        new_data = data[input_columns].copy()
        new_data["FUELCONSUMPTION_CITY_HWY_COMB_AVG"] = new_data[
            ["FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB"]
        ].mean(axis=1)
        return new_data
