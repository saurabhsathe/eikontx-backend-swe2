# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""


from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, ARRAY
from sqlalchemy.orm import declarative_base
from datetime import datetime
from users import User
Base = declarative_base()


class Experiment(Base):
    
    __tablename__ = "experiments"
    experiment_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(),nullable=False)
    experiment_compound_ids= Column(ARRAY(Text), nullable=False)
    experiment_run_time = Column(Integer(),nullable=False)
    
    
    def __init__(self,ex_id,uid,ex_comp_ids,ex_time):
        self.experiment_id = ex_id
        self.user_id = uid
        self.experiment_compound_ids =ex_comp_ids
        self.experiment_run_time = ex_time


from connection import get_connection,get_engine    
engine =get_engine()
try:
    Base.metadata.create_all(bind=engine)
    print("database creation done")
except Exception as e:
    print(e)

