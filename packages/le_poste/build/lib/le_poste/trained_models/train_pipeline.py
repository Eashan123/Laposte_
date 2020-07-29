#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import logging
from sklearn.externals import joblib
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split, GridSearchCV


from le_poste.trained_models import pipeline
from le_poste.config import config as config
from le_poste.processing.data_management import load_dataset, save_pipeline
from le_poste import __version__ as _version

_logger = logging.getLogger(__name__)


def run_training():
    """Train the model."""

    # read training data
    data = pd.read_excel(config.DATASET_DIR / config.TRAINING_DATA_FILE)
    dat_short = data[[config.FEATURES]].copy()
    
    dat_targ = data[[config.TARGET]].copy()
    dat_arr = dat_targ.values
    
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        dat_short,
        dat_arr,
        test_size=0.03,
        random_state=32)  # we are setting the seed here
    
    pipeline.pipe.fit(X_train, y_train)
    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.pipe)



if __name__ == '__main__':
    run_training()


# In[ ]:




