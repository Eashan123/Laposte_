#!/usr/bin/env python
# coding: utf-8


from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random


class RFC_(object):
          
    def Rfc(self, corpus_l):
        
        pattern_rfc = config.rfc

        re_rfc_list = []
        
        for i in range(0, len(corpus_l)):       

            if re.findall(pattern_rfc, corpus_l[i]):
                k = re.findall(pattern_rfc, corpus_l[i])
                unique_values = set(k)
                re_rfc_list.append(str(unique_values)[1:-1])

            else:
                t = {config.nan}
                re_rfc_list.append(str(t)[1:-1])
                
        df_rfc = pd.DataFrame(re_rfc_list, columns=[config.rf])
        _logger.info("rfc entity extracted")
        return df_rfc