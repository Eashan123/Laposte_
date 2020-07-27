#!/usr/bin/env python
# coding: utf-8


from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random


class Version_(object):
    
    def Version(self, corpus_s, corpus_l):
        
        pattern_ver = config.ver1
        pattern_ver_ = config.ver2
        pt_ = config.ver3

        re_ver_list = []
        for i in range(0, len(corpus_l)):       

            if re.findall(pattern_ver, corpus_l[i]):
                k = re.findall(pattern_ver, corpus_l[i])

                if re.findall(pattern_ver, corpus_s[i]):
                    k_ = re.findall(pattern_ver, corpus_s[i])
                    new_l = k + k_
                    unique_values_ = set(new_l)    
                    re_ver_list.append(unique_values_)

                else:
                    unique_values = set(k)    
                    re_ver_list.append(unique_values)


            elif re.findall(pattern_ver_, corpus_l[i]):
                k = re.findall(pattern_ver_, corpus_l[i])

                if re.findall(pattern_ver_, corpus_s[i]):
                    k_ = re.findall(pattern_ver_, corpus_s[i])
                    new_l = k + k_
                    unique_values_ = set(new_l)    
                    re_ver_list.append(unique_values_)

                else:
                    unique_values = set(k)    
                    re_ver_list.append(unique_values)

            elif re.findall(pt_, corpus_l[i]):
                k = re.findall(pt_, corpus_l[i])
        
                if re.findall(pt_, corpus_s[i]):
                    k_ = re.findall(pt_, corpus_s[i])
                    new_l = k + k_
                    unique_values_ = set(new_l)    
                    re_ver_list.append(unique_values_)
        
                else:
                    unique_values = set(k)    
                    re_ver_list.append(unique_values)

            elif re.findall(pattern_ver, corpus_s[i]):
                k = re.findall(pattern_ver, corpus_s[i])
                unique_values = set(k)    
                re_ver_list.append(unique_values)

            elif re.findall(pattern_ver_, corpus_s[i]):
                k = re.findall(pattern_ver_, corpus_s[i])
                unique_values = set(k)    
                re_ver_list.append(unique_values)

            elif re.findall(pt_, corpus_s[i]):
                    k = re.findall(pt_, corpus_s[i])
                    new_l = k
                    unique_values_ = set(new_l)    
                    re_ver_list.append(unique_values_)

            else:             
                t = {config.nan}
                re_ver_list.append(t)

        l = []
        for i in re_ver_list:
            l.append(str(i)[1:-1])

        df_ver = pd.DataFrame(l, columns=[config.ver])
        _logger.info("version entity extracted")

        return df_ver

