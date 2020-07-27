#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import re
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem.snowball import FrenchStemmer
from le_poste.processing.errors import InvalidModelInputError


# In[13]:


class Regex(BaseEstimator, TransformerMixin):
#  https://stackoverflow.com/questions/52123026/sklearn-pipeline-valueerror-could-not-convert-string-to-float   
    def fit(self, X, y = None):
        return self
    
    def transform(self, text):
        
        if not isinstance(text, list):
            raise InvalidModelInputError(f"text not a list", f"list is a valid data structures")
        
        for i in range(0, len(text)):
            text[i] = text[i].lower()
            text[i] = re.sub('\d{2}/\d{2}/\d{4}', ' ', text[i])
            text[i] = re.sub(r'\d{2}:\d{2}:\d{2}', ' ', text[i])
            text[i] = re.sub(r"[a-z0-9]+[\.'\-]*[a-z0-9]+@(laposte|googlemail)\.(com|fr)$", ' ', text[i])
            text[i] = re.sub(r'[?|$|.|!|-|#|*|&|/|%|,|"|:|;|*|@|#]',r'',text[i])
        return text


# In[14]:


class Fr_Stemmer(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, corpus):
        st = FrenchStemmer()
        stem = []
        for sentence in corpus:
            stem.append(" ".join([st.stem(i) for i in sentence.split()]))
        return stem


# In[15]:


class df_tolist(BaseEstimator, TransformerMixin):
    
    def __init__(self, feature = None):
        self.feature = feature
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, corpus):
        corpus = corpus.copy()
        dat = corpus[self.feature].values.tolist()
        return dat


# In[16]:


class fill_na(BaseEstimator, TransformerMixin):

    def __init__(self, feature = None):
        self.feature = feature
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, corpus):
        corpus = corpus.copy()
        corpus[self.feature].fillna('other', inplace=True)
        return corpus


# In[ ]:




