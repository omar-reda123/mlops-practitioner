from prodml.api.schemas import PredictionRequest, PredictionResponse, SPECIES_MAP
from prodml.model.predict import ModelPredictor
from prodml.utils.logging_conf import logger

from fastapi import FastAPI,HTTPException,status

predictor=ModelPredictor()

app=FastAPI(
    title="ProdML - Iris Classification API",
    description="Production-ready API for Iris flower classification.",
    version="1.0.0",
)

@app.get("/health",status_code=status.HTTP_200_OK)
async def health_check():
    return {
        "status":"healthy",
        "model_loaded":predictor.loaded_model is not None,
    }

@app.post("/predict",
          response_model=PredictionResponse,
          status_code=status.HTTP_200_OK
        )
async def predict_flower(payload:PredictionRequest):
    input_data=[
        [
            payload.sepal_length,
            payload.sepal_width,
            payload.petal_length,
            payload.petal_width
        ]
    ]

    try:
        result=predictor.predict(X=input_data,one_sample=True)
        pred_class=int(result["prediction"])
        proba=float(result["probability"])

        return PredictionResponse(
            prediction=pred_class,
            species_name=SPECIES_MAP.get(pred_class,"unknown"),
            probability=round(proba,5)
        )
    except Exception as exc:
        logger.error("Prediction inference failed: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during inference.",
        ) from exc
        






