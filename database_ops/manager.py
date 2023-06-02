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
class Manager:
    
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
    
    def total_ex_by_users(self,exdf):
        return exdf.groupby(["user_id"])["experiment_id"].count().reset_index(name='total_experiments')
    
    def avg_experiments_amount_per_user(self,exdf):
        try:
            return exdf.groupby(["user_id"])["experiment_run_time"].mean().reset_index(name='avg_runtime')   
            
        except Exception as e:
            print(e)
    
    def get_most_common_compound_by_user(self,user_df,comp_df,exdf):
        try:
            compounds = defaultdict(list)
            for idx,row in exdf.iterrows():
                compounds[row["user_id"]] +=[int(i) for i in row["experiment_compound_ids"].split(";")]
                
            #print(compounds)    
            counts={user_id:defaultdict(int) for user_id in compounds}
            for user_id in compounds:
                #print(user_id)
                for num in compounds[user_id]:
                    counts[user_id][num]+=1
            
            ans= {user_id:[] for user_id in compounds}
            print(counts)
            for user_id in compounds:
                
                max_count=max(counts[user_id].values())
                comp_ids = []
                for key in counts[user_id]:
                    if counts[user_id][key]==max_count:
                        comp_ids.append(key)
                print(user_id,comp_ids)
                ans[user_id] = ",".join(list(comp_df[comp_df['compound_id'].isin(comp_ids)]["compound_name"]))
            
            #print(ans)
            print(ans)
            return ans
        
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
    
    