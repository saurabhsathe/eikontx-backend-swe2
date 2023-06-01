# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    signup_date = Column(DateTime(), default=datetime.now)
     
            
    def __init__(self,user_id,name,email,signup_date):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.signup_date =signup_date

from connection import get_connection,get_engine    
engine =get_engine()
try:
    Base.metadata.create_all(bind=engine)
    print("database creation done")
except Exception as e:
    print(e)

        
    