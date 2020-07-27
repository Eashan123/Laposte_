#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import Pipeline  ### use this one only
from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.over_sampling import SMOTE
from  le_poste.processing import preprocessors as pp
import class_weight as cw
from le_poste.config import config as cf

import logging


_logger = logging.getLogger(__name__)


# In[3]:


pipe = Pipeline([
 ('na', pp.fill_na(cf.FEATURES)),
 ('lis', pp.df_tolist(cf.FEATURES)),
 ('reg', pp.Regex()),
 ('stem', pp.Fr_Stemmer()),
 ('vect', CountVectorizer(ngram_range = (1, 1))),
 ('tfidf', TfidfTransformer(use_idf = False)),
 ('sm', SMOTE(sampling_strategy = 'minority', random_state=32, n_jobs = -1, k_neighbors = 1)), 
 ('rfc', RandomForestClassifier(n_estimators = 1200, criterion = 'entropy', random_state = 32, 
                                max_depth = 80, min_samples_split = 2, min_samples_leaf = 1, 
                                class_weight = cw.classweights_sklearn()) )])


# In[ ]:




