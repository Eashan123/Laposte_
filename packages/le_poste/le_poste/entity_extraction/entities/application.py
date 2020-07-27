#!/usr/bin/env python
# coding: utf-8

from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random

class Application_(object):
    
    def Application(self, corpus_s, corpus_l):

        patt_ = config.app1
        pattern_app = config.app2

        re_app_list = []

        for i in range(0, len(corpus_l)):   

            if re.findall(pattern_app, corpus_l[i]):

                k = re.findall(pattern_app, corpus_l[i])

                if re.findall(pattern_app, corpus_s[i]):

                    k_ = re.findall(pattern_app, corpus_s[i])
                    new_l = k + k_
                    unique_values_ = set(new_l)
                    re_app_list.append(unique_values_)

                elif re.findall(patt_, corpus_s[i]):
                    k_ = re.findall(patt_, corpus_s[i])
                    for it in k_:
                        l.append(it[0])
                    new_l = k + l
                    unique_values_ = set(new_l)
                    re_app_list.append(unique_values_)

                else:

                    unique_values = set(k)
                    re_app_list.append(unique_values)

            elif re.findall(patt_, corpus_l[i]):

                l = []
                k_ = re.findall(patt_, corpus_l[i])

                for it in k_:
                    l.append(it[0])

                if re.findall(pattern_app, corpus_s[i]):
                    k = re.findall(pattern_app, corpus_s[i])
                    new_l = l + k
                    unique_values_ = set(new_l)
                    re_app_list.append(unique_values_)

                elif re.findall(patt_, corpus_s[i]):
                    l_ = []
                    k = re.findall(patt_, corpus_s[i])
                    for it in k:
                        l_.append(it[0])
                    new_l = l + l_
                    unique_values_ = set(new_l)
                    re_app_list.append(unique_values_)

                else:

                    unique_values = set(l)
                    re_app_list.append(unique_values)


            elif re.findall(pattern_app, corpus_s[i]):

                k_ = re.findall(pattern_app, corpus_s[i])

                if re.findall(patt_, corpus_s[i]):
                    k = re.findall(patt_, corpus_s[i])
                    l = []
                    for it in k:
                        l.append(it[0])
                    new_l = k_ + l
                    unique_values_ = set(new_l)
                    re_app_list.append(unique_values_)

                else:

                    unique_values = set(k_)
                    re_app_list.append(unique_values)


            else:
                t = {config.nan}
                re_app_list.append(t)

        l = []
        for ind, i in enumerate(re_app_list):
            l.append(str(i)[1:-1])



        df_app = pd.DataFrame(l, columns=[config.app])
        _logger.info("application entity extracted")

        return df_app

