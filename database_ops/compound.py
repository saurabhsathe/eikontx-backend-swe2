# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Compound(Base):
    
    __tablename__ = "compounds"
    compound_id = Column(Integer(), primary_key=True)
    compound_name = Column(String(100), nullable=False)
    compound_structure= Column(String(250), nullable=False)
    
    
    
    def __init__(self,compound_id,compound_name,email,compound_structure):
        self.compound_id = compound_id
        self.compound_name = compound_name
        self.compound_structure = compound_structure


from connection import get_connection,get_engine    
engine =get_engine()
try:
    Base.metadata.create_all(bind=engine)
    print("database creation done")
except Exception as e:
    print(e)
