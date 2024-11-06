import logging

import pytest
from sklearn.model_selection import train_test_split

from red_wine_mm.config.core import config
from red_wine_mm.processing.data_manager import load_dataset

logger = logging.getLogger(__name__)


@pytest.fixture
def sample_input_data():
    data = load_dataset(file_name=config.app_config.raw_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.m_config.features],  # predictors
        data[config.m_config.target],
        test_size=config.m_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.m_config.random_state,
        stratify=data[config.m_config.target],
    )

    return X_test, y_test
