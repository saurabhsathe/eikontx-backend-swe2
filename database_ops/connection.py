# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:29:59 2023

@author: 16692
"""


from sqlalchemy import create_engine
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

def show_databases():
    conn = get_connection()
    return conn

print(show_databases())

    