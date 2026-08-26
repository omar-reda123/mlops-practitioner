from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

from prodml.utils.config import settings
from prodml.utils.logging_conf import logger

class DataPrepare:

    def __init__(
        self,
        data_path: str|Path = settings.DATA_RAW_DIR_FILE1
    ):
        self.path = Path(data_path)

        try:
            self.df = pd.read_csv(self.path)
            logger.info(
                "Data loaded successfully from %s",
                self.path
            )

        except FileNotFoundError:
            logger.error(
                "Cannot find file at %s",
                self.path
            )
            raise

    def split_features_target(
        self,
        target_col: str = settings.TARGET_COL
    ) -> tuple[pd.DataFrame, pd.Series]:
        if target_col not in self.df.columns:
            logger.error("Target column '%s' not found in dataset", target_col)
            raise KeyError(f"Target column '{target_col}' not found")

        y = self.df[target_col]
        X = self.df.drop(columns=[target_col])

        logger.info(
            "Features-target split completed | X shape=%s | y shape=%s",
            X.shape,
            y.shape
        )

        return X, y

    def split_train_test(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        stratify: bool = True
    ) -> tuple[
        pd.DataFrame,
        pd.DataFrame,
        pd.Series,
        pd.Series
    ]:
        stratify_target= y if stratify else None

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=settings.TEST_SIZE,
            random_state=settings.RANDOM_STATE,
            stratify=stratify_target
        )

        logger.info(
            "Train-test split completed | "
            "X_train=%s | X_test=%s",
            X_train.shape,
            X_test.shape
        )

        return X_train, X_test, y_train, y_test