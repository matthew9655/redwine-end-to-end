from typing import Any, List, Optional

from pydantic import BaseModel
from red_wine_mm.processing.validation import WineDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[WineDataInputSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "inputs": [
                    {
                        "fixed acidity": 7.4,
                        "volatile acidity": 0.25,
                        "citric acid": 0.29,
                        "residual sugar": 2.2,
                        "chlorides": 0.054,
                        "free sulfur dioxide": 19.0,
                        "total sulfur dioxide": 49.0,
                        "sulphates": 0.76,
                        "alcohol": 10.9,
                        # output should be "good" == 1
                    }
                ]
            }
        }
