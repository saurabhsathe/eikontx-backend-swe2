# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""


from sqlalchemy import create_engine
#connection_string ="postgresql://sathesaurabh30:HF32LKiPgJfS@ep-summer-butterfly-378832.us-east-2.aws.neon.tech/neondb"
connection_string = "postgresql://sathesaurabh30:HF32LKiPgJfS@ep-summer-butterfly-378832-pooler.us-east-2.aws.neon.tech/swe-backend"

try:
    engine =create_engine(connection_string)
except Exception as e:
    print(e)

def get_connection():
    try:
        conn = engine.connect()
        return conn
    except Exception as e:
        print(e)
    
def get_engine():
    return engine


    