from le_poste.config import entity_config as econfig
from le_poste.config import config
from le_poste import __version__ as _version

import logging
_logger = logging.getLogger(__name__)

from le_poste.entity_extraction.entities.application import Application_
from le_poste.entity_extraction.entities.module import Module_
from le_poste.entity_extraction.entities.rfc import RFC_
from le_poste.entity_extraction.entities.environment import Environment_
from le_poste.entity_extraction.entities.version import Version_
from le_poste.entity_extraction.preprocessing.preprocess import Preprocess_

import numpy as np
import pandas as pd
import re
import random
import pathlib
from sklearn.base import BaseEstimator, TransformerMixin


class Entity_Extraction(BaseEstimator, TransformerMixin, Application_, Module_, RFC_, Environment_, Version_, Preprocess_):
    
    def __init__(self, df, path_s, name):
        
        self.df = df
        self.path_s = path_s
        self.name = name
    
    def fit(self):
        
        corpus_s, corpus_l, df_, df_des, df_res = self.load_data(self.df)
        df_app = self.Application(corpus_s, corpus_l)
        df_mod = self.Module(corpus_l)
        df_rfc = self.Rfc(corpus_l)
        df_env = self.Environment(corpus_s, corpus_l)
        df_ver = self.Version(corpus_s, corpus_l)
        dff = self.Concatenation(df_, df_res, df_des, df_app, df_mod, df_rfc, df_env, df_ver)
        return dff
    
    def Concatenation(self, df_, df_res, df_des, df_app, df_mod, df_rfc, df_env, df_ver):
        
        dfr = pd.concat([df_, df_res, df_des, df_app, df_mod, df_rfc, df_env, df_ver], axis = 1)
        dfr = dfr[econfig.FEATURES_ORDER]
        return dfr
            
    def transform(self, dframe):
    # https://stackoverflow.com/questions/48001164/typeerror-unsupported-operand-types-for-posixpath-and-str
        dframe.to_excel(self.path_s / self.name)
        

# if __name__ == '__main__':
#     z = Entity_Extraction(path, path_s, name)
#     df = z.fit()
#     z.transform(df)
#     _logger.info(f"Extracted entities done")
  



