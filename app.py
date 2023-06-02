import pandas as pd
import sqlalchemy
from database_ops.handler import Handler
from database_ops.manager import Manager
from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

myhandler =Manager()

df_users =None
df_experiments = None
df_compounds =None




def add_data(df_users,df_experiments,df_compounds):
    try:
        myhandler.add_users(df_users)
    except Exception as e:
        print("thrown here1",e)
    try:
        myhandler.add_experiments(df_experiments)
    except Exception as e:
        print(e)
    try:
        myhandler.add_compounds(df_compounds)
    except Exception as e:
        print(e)
    return True
    

def remove_data():
    myhandler.remove_all_data("experiments")
    myhandler.remove_all_data("compounds")
    myhandler.remove_all_data("users")
    
    

def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    #myhandler.total_ex_by_users()
    remove_data()
    
    df_users = myhandler.preprocess(pd.read_csv("data/users.csv"))
    df_experiments = myhandler.preprocess(pd.read_csv("data/user_experiments.csv"))
    df_compounds  = myhandler.preprocess(pd.read_csv("data/compounds.csv"))
    add_data(df_users.copy(),df_experiments.copy(),df_compounds.copy())
    
    f1 = myhandler.total_ex_by_users(df_experiments).set_index("user_id").to_dict()
    f2 = myhandler.avg_experiments_amount_per_user(df_experiments).set_index("user_id").to_dict()
    f3 = myhandler.get_most_common_compound_by_user(df_users, df_compounds, df_experiments)
    
    return {"total_experiments":f1["total_experiments"],"avg_runtimes":f2["avg_runtime"],"common_compounds":f3}
    
@app.route("/trigger_etl",methods=['POST'])
# Your API that can be called to trigger your ETL process
def trigger_etl():
    # Trigger your ETL process here
    resp = etl()
    
    return jsonify ({"message": "ETL process started","result": resp}), 200

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port=4000)

