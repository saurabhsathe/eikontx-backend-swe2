# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""
from sqlalchemy.orm import sessionmaker
from database_ops.connection import get_connection,get_engine
import pandas as pd

class Handler:
    
    def __init__(self):
        #import connection details and get the connection object
        self.conn = get_connection()
        self.engine = get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def add_users(self,df):
        for idx, row in df.iterrows():
            print(type(row["user_id"]))
           
        #df.to_sql("users",if_exists='append',con = self.conn,index=False)
        print("users added successfully")
        
    
    def add_compound(self):
        pass
    
    
    
    def add_experiment(self):
        pass
    
    def total_ex_by_user(self):
        pass
    
    def avg_experiments_per_user(self):
        pass
    
    def get_most_common_compound_user(self):
        pass
    
    
    