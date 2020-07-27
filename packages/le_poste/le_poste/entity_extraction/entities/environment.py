#!/usr/bin/env python
# coding: utf-8


from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random


class Environment_(object):
    
    def Environment(self, corpus_s, corpus_l):
        
        add_item_lookup = config.env_lk

        
        re_env_list = []

        for i in range(0, len(corpus_l)):  

            k = []
            split_ = corpus_l[i].split(' ')
            for itr in split_:
                if itr in add_item_lookup:
                    k.append(itr)

                else:
                    pass

            k_ = []
            split_ = corpus_s[i].split(' ')
            for itr in split_:
                if itr in add_item_lookup:
                    k_.append(itr)

                else:
                     pass

            new_l = k + k_
            unique_values = set(new_l)
            re_env_list.append(unique_values)
            

        for ind, i in enumerate(re_env_list):
            if not i:
                re_env_list[ind] = {config.nan}
        
        l = []
        for ind, i in enumerate(re_env_list):
            l.append(str(i)[1:-1])

        df_env = pd.DataFrame(l, columns=[config.env])
        _logger.info("environment entity extracted")
        
        return df_env
