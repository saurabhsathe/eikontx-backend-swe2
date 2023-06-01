# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""

class Experiment:
    
    def __init__(self,ex_id,uid,ex_comp_ids,ex_time):
        self.experiment_id = ex_id
        self.user_id = uid
        self.experiment_compound_ids =ex_comp_ids
        self.experiment_run_time = ex_time

