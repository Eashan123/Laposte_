#!/usr/bin/env python
# coding: utf-8


from le_poste.config import entity_config as config

import logging
_logger = logging.getLogger(__name__)


import numpy as np
import pandas as pd
import re
import random


class Module_(object):
       
    
    def Module(self, corpus_l):
        
        
        pattern = config.mod1
        patt_ = config.mod2
        pat_ = config.mod3
        p = config.mod4
        
        re_mod_list = []

        for i in range(0, len(corpus_l)): 
       
            if re.findall(pattern, corpus_l[i]):
                        k = re.findall(pattern, corpus_l[i])
                
                        if re.findall(pat_, corpus_l[i]):          
                                k_ = re.findall(pat_, corpus_l[i])
                                new_list = k + k_
                                unique_values = set(new_list)
                                re_mod_list.append(unique_values)

                        elif re.findall(p, corpus_l[i]):
                                l = []
                                k_ = re.findall(p, corpus_l[i])
                                for it in k_:
                                    l.append((it[1], it[2]))

                                new_list = k + l
                                unique_values = set(new_list)
                                re_mod_list.append(unique_values)

                        elif re.findall(patt_, corpus_l[i]):
                            l = []
                            k_ = re.findall(patt_, corpus_l[i])
                            for it in k_:
                                l.append(it[1])

                            new_list = k + l
                            unique_values = set(new_list)
                            re_mod_list.append(unique_values)


                        else:
                            unique_values = set(k)
                            re_mod_list.append(unique_values)


            elif re.findall(pat_, corpus_l[i]):
                    k_ = re.findall(pat_, corpus_l[i])

                    if re.findall(p, corpus_l[i]):
                                l_ = []
                                k_ = re.findall(p, corpus_l[i])
                                for it in k_:
                                    l_.append((it[1], it[2]))

                                new_list = k_ + l_
                                unique_values = set(new_list)
                                re_mod_list.append(unique_values)

                    else:

                                unique_values = set(k_)
                                re_mod_list.append(unique_values)


            elif re.findall(p, corpus_l[i]):

                            k_ = re.findall(p, corpus_l[i])
                            l = []
                            for it in k_:
                                l.append((it[1], it[2]))



                            unique_values = set(l)
                            re_mod_list.append(unique_values)


            elif re.findall(patt_, corpus_l[i]):
                        l = []
                        k_ = re.findall(patt_, corpus_l[i])
                        for it in k_:
                            l.append(it[1])

                        if re.findall(p, corpus_l[i]):
                                l_ = []
                                k_ = re.findall(p, corpus_l[i])
                                for it in k_:
                                    l_.append((it[1], it[2]))

                                new_list = l + l_
                                unique_values = set(new_list)
                                re_mod_list.append(unique_values)


                        elif re.findall(pat_, corpus_l[i]):
                                k_ = re.findall(pat_, corpus_l[i])
                                new_list = l + k_
                                unique_values = set(new_list)
                                re_mod_list.append(unique_values)


                        else:
                            unique_values_ = set(l)
                            re_mod_list.append(unique_values_)


            else:
                t = {config.nan}
                re_mod_list.append(t)

        del_item_lookup = config.mod_lk
        a = 0
        l = []
        for i in re_mod_list:
            b = 0
            cnt = 0
            try:
                for j in i:

                    if j == del_item_lookup[cnt]:
                        i.remove(j)
                    b += 1
            except:
                pass
            a += 1                

            for ind, i in enumerate(re_mod_list):
                if not i:
                    re_mod_list[ind] = {config.nan}  

            
            for ind, i in enumerate(re_mod_list):
                l.append(str(i)[1:-1])        

        df_mod = pd.DataFrame(l, columns=[config.mod])
        _logger.info("module entity extracted")            

        
        return df_mod

