# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""
from sqlalchemy.orm import sessionmaker
from database_ops.connection import get_connection,get_engine
import pandas as pd
from sqlalchemy import text

class Handler:
    
    def __init__(self):
        #import connection details and get the connection object
        self.conn = get_connection()
        self.engine = get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def preprocess(self,df):
        for col in df.columns:
            data = df[col]
            if isinstance(data[0], str):
                data = [line.strip() for line in data if "\t" in line]
            del df[col]
            df[col.strip()]=data
        return df
            
    def add_users(self,df):
        df = self.preprocess(df)   
        df.to_sql("users",if_exists='append',con = self.conn,index=False)
        print("users added successfully")
        
    
    def add_compounds(self,df):
        df =self.preprocess(df)
        df.to_sql("compounds",if_exists='append',con = self.conn,index=False)
        print("compounds added successfully")
    
    
    def add_experiments(self,df):
        df =self.preprocess(df)
        df.to_sql("experiments",if_exists='append',con = self.conn,index=False)
        print("experiements added successfully")
    
    def remove_all_data(self,table):
        try:
            self.conn.execute(text("delete from {};".format(table)))
            print("data deleted successfully")
        except Exception as e:
            print(e)
    
    def total_ex_by_user(self,user_id):
        pass
    
    def avg_experiments_per_user(self):
        pass
    
    def get_most_common_compound_by_user(self,user_id):
        pass
    
    
    