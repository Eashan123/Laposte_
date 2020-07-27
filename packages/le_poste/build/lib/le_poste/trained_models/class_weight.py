#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.utils import class_weight
import pandas as pd
import numpy as np
from le_poste.config import config as cf
import logging

_logger = logging.getLogger(__name__)


# In[22]:


def classweights_sklearn():
    dat = pd.read_excel(cf.DATASET_DIR/cf.TRAINING_DATA_FILE)
    dat[cf.TARGET].fillna('other', inplace=True)
    label = dat[cf.TARGET].astype(str).values.tolist()

    class_weights = class_weight.compute_class_weight('balanced', np.unique(label), label)

    cw = dict(zip(np.unique(label), class_weight.compute_class_weight('balanced',
                                                 np.unique(label),
                                                 label))) 
    return cw

