import pandas as pd
import sqlalchemy
from database_ops.handler import Handler
myhandler =Handler()


def add_data():
    try:
        df_users = pd.read_csv("data/users.csv")
        myhandler.add_users(df_users)
    except Exception as e:
        print(e)
    try:
        df_experiments = pd.read_csv("data/user_experiments.csv")
    except Exception as e:
        print(e)
    try:
        df_compounds  = pd.read_csv("data/compounds.csv")
    except Exception as e:
        print(e)
    
    print("data insertion complete")
    

def remove_data():
    myhandler.remove_all_data("users")
    myhandler.remove_all_data("compounds")
    myhandler.remove_all_data("experiments")


def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    remove_data()    

# Your API that can be called to trigger your ETL process
def trigger_etl():
    # Trigger your ETL process here
    etl()
    return {"message": "ETL process started"}, 200



trigger_etl()
print("running")