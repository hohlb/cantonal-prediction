import pandas as pd
import requests
import re
import datetime



def load_data():
    '''This function gets the data from the api openzh'''
    resp = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/all')
    data = pd.DataFrame(resp.json()['records'])

    return data

def pre_process(data):
    '''create summary rows, 'ensure all col are lowercase, transform date to index, and change all data to numeric, add prediction column'''
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    DATE_COLUMN = 'date'
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.set_index('date', inplace=True)
    for column in list(data.columns.values):
        if re.search("ncumul|ninst|Total", column):
            data[column] = pd.to_numeric(data[column])
    df_switzerland = data.sum(level=0)
    df_switzerland['abbreviation_canton_and_fl'] = 'CH'
    data = data.append(df_switzerland)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['prediction'] = 0
    data.sort_values(by=['date'], inplace = True)
    return data


def predict(data):
    '''provides rows with prediction results'''    
    growth_values_dict = {}
    growth_rate_dict = {}
    for canton in data.abbreviation_canton_and_fl.unique():
        growth_values_dict[canton]  = data[data['abbreviation_canton_and_fl'] == canton].sort_values(by=['date'])['ncumul_conf'][-8:]
    for key, value in growth_values_dict.items():
        diff_list = []
        valid_diff_list = []
        for i in range(1,len(value)-1):
            x = value[i] / value[i-1]
            diff_list.append(x)
        for elem in diff_list:
            if elem > 0 and elem < 5 and elem != None:
                valid_diff_list.append(elem)
        growth_rate_dict[key] = sum(valid_diff_list) / float(len(valid_diff_list))
    data = data.reset_index()
    data.sort_values(by=['date'], inplace = True)
    for canton in data.abbreviation_canton_and_fl.unique():
        add = [{'date': growth_values_dict[canton][-1:].index[0] + datetime.timedelta(days=1), 'abbreviation_canton_and_fl' : canton, 'ncumul_conf' : int(growth_rate_dict[canton] * (growth_values_dict[canton][-1])), 'prediction' : 1}]
        data = data.append(add)
    data.sort_values(by=['date'], inplace = True)
    data.set_index('date', inplace = True)
    return data


def prep_data():
    '''calls all above functions'''
    data = load_data()
    data = pre_process(data)
    data = predict(data)

    return data
