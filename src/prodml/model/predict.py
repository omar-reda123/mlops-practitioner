from pathlib import Path
import joblib
import pandas as pd
import numpy as np

from prodml.utils.config import settings
from prodml.utils.logging_conf import logger


class ModelPredictor:
    def __init__(self):
        model_path=settings.MODELS_DIR/settings.MODEL_NAME

        try:
            self.loaded_model = joblib.load(model_path)
            logger.info("loaded model successfully!")
        except FileNotFoundError:
            logger.error("Can not find model at:%s",model_path)
            raise

    def predict(
        self,
        X: pd.DataFrame | np.ndarray | list,
        one_sample: bool = True,
    ) -> dict[str, int | float] | list[dict[str, int | float]]:
        if isinstance(X, list) and len(X) > 0 and not isinstance(X[0], (list, tuple)):
            X = [X]

        predictions = self.loaded_model.predict(X)
        probabilities = self.loaded_model.predict_proba(X)
        max_probs = np.max(probabilities, axis=1)

        logger.info("Generated predictions for %d sample(s)", len(predictions))

        if one_sample and len(predictions) == 1:
            return {
                "prediction": int(predictions[0]),
                "probability": float(max_probs[0]),
            }

        return [
            {"prediction": int(p), "probability": float(prob)}
            for p, prob in zip(predictions, max_probs)
        ]
       

        
    
if __name__ == "__main__":
    predictor = ModelPredictor()

    sample_data = pd.DataFrame(
        [[5.1, 3.5, 1.4, 0.2]],
        columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ],
    )

    result = predictor.predict(X=sample_data)
    print(f"Prediction result: {result}")