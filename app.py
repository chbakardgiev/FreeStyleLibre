import pandas as pd
import os
import requests
import time
from pathlib import Path

# here goes your bearer token
token = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

directory = os.path.dirname(os.path.abspath(__file__))
permanent_storage = "storage.txt"

def make_query(start_at_line):
    directory = os.path.dirname(os.path.abspath(__file__))
    permanent_storage = "storage.txt"
    # opens csv file from current directory
    csv = [x for x in os.listdir(directory) if x.endswith(".csv")][0]
    # parse csv to df
    df_clean = pd.read_csv(os.path.join(directory, csv), engine="python")
    # remove strange indexation
    df_clean.reset_index(inplace=True)
    df_clean.drop(df_clean.index[0], inplace=True)
    last_index = 0
    for i, v in df_clean.iterrows():
        last_index = i
        # filter out rows that have no info
        if v["level_4"] != float('nan') and str(v["level_4"]) != "nan" and i>= start_at_line and len(df_clean)>0:
            data = {'activity': (None, """{"gameDescriptor":61,"dataProvider":1,"date":""" + str(time.time()).replace('.', "")[0:13]  + ""","propertyInstances":[{"property":87,"value":null},{"property":88,"value":""" + str(v["level_4"]) + """},{"property":89,"value":"6"}],"players":[332]}""")}
            request = requests.post(url=API_ENDPOINT, files=data, headers=headers)
            print(request.text)
            time.sleep(0.15)
    print("done")
    f = open(os.path.join(directory, permanent_storage), "w")
    f.write(str(last_index))
    f.close()

# defining the api-endpoint
API_ENDPOINT = "https://api3.gamebus.eu/v2/activities?dryrun=false&fields=personalPoints.value"

headers = {"Authorization": "Bearer " + token}

# read the currect directory
directory = os.path.dirname(os.path.abspath(__file__))

permanent_storage = "storage.txt"

path_pernament_storage = os.path.join(directory, permanent_storage)
if not Path(path_pernament_storage).exists():
    f = open(path_pernament_storage, "w")
    last_row_index = 0
    f.write(str(last_row_index))
    f.close()
    make_query(last_row_index)
else:
    f = open(path_pernament_storage, "r")
    last_row_index = int(f.read())
    f.close()
    make_query(last_row_index)
