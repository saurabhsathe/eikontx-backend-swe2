import pandas as pd
import sqlalchemy
from database_ops.handler import Handler
from database_ops.manager import Manager
myhandler =Manager()

df_users =None
df_experiments = None
df_compounds =None

def add_data(df_users,df_experiments,df_compounds):
    try:
        
        myhandler.add_users(df_users)
    except Exception as e:
        print(e)
    try:
        myhandler.add_experiments(df_experiments)
    except Exception as e:
        print(e)
    try:
        myhandler.add_compounds(df_compounds)
    except Exception as e:
        print(e)
    return True
    
def read_data():
    pass

def remove_data():
    myhandler.remove_all_data("experiments")
    myhandler.remove_all_data("compounds")
    myhandler.remove_all_data("users")
    
    

def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    #myhandler.total_ex_by_users()
    #remove_data()
    
    df_users = myhandler.preprocess(pd.read_csv("data/users.csv"))
    df_experiments = myhandler.preprocess(pd.read_csv("data/user_experiments.csv"))
    df_compounds  = myhandler.preprocess(pd.read_csv("data/compounds.csv"))

    #add_data(df_users,df_experiments,df_compounds)
    #tot_exp = myhandler.total_ex_by_users(df_experiments)
    
    #avg_runtimes = myhandler.avg_experiments_amount_per_user(df_experiments)
    print(myhandler.get_most_common_compound_by_user(df_users, df_compounds, df_experiments))
    
    
    
    
# Your API that can be called to trigger your ETL process
def trigger_etl():
    # Trigger your ETL process here
    etl()
    return {"message": "ETL process started"}, 200



trigger_etl()
print("running")