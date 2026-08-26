from pydantic import BaseModel,Field

SPECIES_MAP: dict[int, str] = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}

class PredictionRequest(BaseModel):
    sepal_length: float = Field(gt=0,description="sepal_length of the flower")
    sepal_width: float = Field(gt=0,description="sepal_width of the flower")
    petal_length: float = Field(gt=0,description="petal_length of the flower")
    petal_width: float = Field(gt=0,description="petal_width of the flower")
    model_config = {
    "json_schema_extra": {
        "examples": [
            {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        ]
    }
}

class PredictionResponse(BaseModel):
    prediction: int = Field(description="Predicted class index (0, 1, or 2)")
    species_name: str = Field(description="Predicted Iris species name")
    probability: float = Field(description="Prediction confidence score")



    


