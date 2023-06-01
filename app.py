import pandas as pd
import sqlalchemy
def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    
    df_users = pd.read_csv("data/users.csv")
    df_experiments = pd.read_csv("data/user_experiments.csv")
    df_compounds  = pd.read_csv("data/compounds.csv")
    
    print(df_experiments.columns)
    print(df_users.columns)
    print(df_compounds.columns)
    
    

# Your API that can be called to trigger your ETL process
def trigger_etl():
    # Trigger your ETL process here
    etl()
    return {"message": "ETL process started"}, 200



trigger_etl()
print("running")