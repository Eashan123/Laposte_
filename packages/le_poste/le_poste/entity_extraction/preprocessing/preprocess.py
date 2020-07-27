#!/usr/bin/env python
# coding: utf-8


from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random


class Preprocess_(object):
    
    def _reg(self, text):
        
        for i in range(0, len(text)):
            _RE_COMBINE_WHITESPACE = re.compile(config.spaces)
            text[i] = re.sub( config.exp1, config.subb, text[i])
            text[i] = re.sub( config.exp2, config.subb, text[i])
            text[i] = re.sub( config.exp3, config.subb, text[i])
            text[i] = re.sub( config.exp4, config.subb,text[i])
            text[i] = _RE_COMBINE_WHITESPACE.sub(config.space, text[i]).strip()
            text[i] = re.sub( config.exp5, config.subb_, text[i])
            text[i] = re.sub( config.exp6, config.subb_, text[i])
            text[i] = re.sub( config.exp7, config.subb_, text[i])
            text[i] = _RE_COMBINE_WHITESPACE.sub(config.space, text[i]).strip()
        return text

    def _preprocess(self, dat):
        
        data = self._reg(dat)
        _logger.info("preprocessing of entities done")
        return data

    
    
    def load_data(self, df):
        
#         dat = pd.read_excel( path)
        dat =  df.copy()
        dat_short = dat[[config.FEATURES[0]]].copy()
        dat_long = dat[[config.FEATURES[1]]].copy()
        dat_s = dat_short[config.FEATURES[0]].astype(str).values.tolist()
        dat_l = dat_long[config.FEATURES[1]].astype(str).values.tolist()
        data_l =  self._preprocess(dat_l)
        data_s =  self._preprocess(dat_s)
        df_des = pd.DataFrame(data_l, columns = [config.FEATURES[1]])
        df_res = pd.DataFrame(data_s, columns = [config.FEATURES[0]])
        dat = dat.drop(config.DROP_FEATURES, axis = 1)
        
        return data_s, data_l, dat, df_des, df_res
    