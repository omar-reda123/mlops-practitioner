from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , classification_report
import joblib

from prodml.utils.config import settings
from prodml.data.loader import DataPrepare
from prodml.utils.logging_conf import logger


class ModelTrainer:
    def __init__(
        self,
        random_state: int = settings.RANDOM_STATE,
        max_depth: int = settings.MAX_DEPTH,
        n_estimators: int = settings.N_ESTIMATORS,
    ):
        self.random_state = random_state
        self.max_depth = max_depth
        self.n_estimators = n_estimators

        self.model = RandomForestClassifier(
            max_depth = self.max_depth,
            n_estimators = self.n_estimators,
            random_state = self.random_state,
        )
        logger.info(
            "RandomForest model initialized | n_estimators=%s, max_depth=%s",
            self.n_estimators,
            self.max_depth,
        )
    def training_pipeline(self)->None:
        #loading data
        data_loader = DataPrepare()
        X , y = data_loader.split_features_target()
        X_train , X_test , y_train , y_test = data_loader.split_train_test(X=X,y=y,stratify=True)

        #training
        self.model.fit(X_train,y_train)
        logger.info("model trained successfully!")

        #evaluation
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_pred=y_pred,y_true=y_test)
        logger.info("accuracy is:%s",accuracy)
        classification_rprt = classification_report(y_pred=y_pred,y_true=y_test)
        logger.info("classification_report is:\n%s",classification_rprt)

        #saving model
        self.save_model()

    def save_model(self)->None:
        model_path=settings.MODELS_DIR/settings.MODEL_NAME
        joblib.dump(self.model,model_path)
        logger.info("Model saved successfully to %s", model_path)



if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.training_pipeline()










    
    
    
        
        
        

