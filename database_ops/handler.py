# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""
from sqlalchemy.orm import sessionmaker
from database_ops.connection import get_connection,get_engine
import pandas as pd
from sqlalchemy import text
from collections import defaultdict
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
            if not self.conn:
                self.conn = get_connection()
            sql ="drop table {};".format(table)
            print(sql)
            self.session.execute(text(sql))
            self.session.commit()
            print("data deleted successfully")
            
        except Exception as e:
            print(e)
    
    def total_ex_by_users(self):
        try:
            if not self.session:
                self.session = sessionmaker(bind=self.engine)()
            sql='select user_id,count(*) as "total experiments" from experiments group by user_id;'
            result = self.session.execute(text(sql))
            result = pd.DataFrame(result,index=None)
            #print(result)
            self.session.commit()
            return result
        except Exception as e:
            print(e)
    
    def avg_experiments_per_user(self):
        try:
            if not self.session:
                self.session = sessionmaker(bind=self.engine)()
            sql='select AVG(total) from (select count(*) as "total" from experiments group by user_id) as x;'
            result = self.session.execute(text(sql))
            result = pd.DataFrame(result,index=None)
            #print(result)
            self.session.commit()
            return result
        except Exception as e:
            print(e)
    
    def get_most_common_compound_by_user(self,user_id):
        try:
            if not self.session:
                self.session = sessionmaker(bind=self.engine)()
            sql='select * from experiments where user_id = {};'.format(user_id)
            result = self.session.execute(text(sql))
            
            result = pd.DataFrame(result,index=None)
            compounds =[]
            
            for idx,row in result.iterrows():
                compounds.append(row["experiment_compound_ids"])
                
                
            if not compounds:
                return None
            counts=defaultdict(int)
            for s in compounds:
                for num in s.split(";"):
                    counts[int(num)]+=1
                    
            max_count=max(counts.values())
            comp_ids = []
            for key in counts:
                if counts[key]==max_count:
                    comp_ids.append(key)
            
                    
            print(comp_ids)    
            self.session.commit()
                
            x= ",".join([str(v) for v in comp_ids])
            sql='select * from compounds where compound_id in ({});'.format(x)
            print(sql)
            result = self.session.execute(text(sql))
            result = pd.DataFrame(result,index=None)
            self.session.commit()
            
            return result
        
        except Exception as e:
            print(e)
        
    def ex_for_user(self,user_id):
        try:
            if not self.session:
                self.session = sessionmaker(bind=self.engine)()
            sql='select user_id,count(*) as "total experiments" from experiments group by user_id having user_id = {};'.format(user_id)
            result = self.session.execute(text(sql))
            result = pd.DataFrame(result,index=None)
            #print(result)
            self.session.commit()
            return result
        except Exception as e:
            print(e)
    
    