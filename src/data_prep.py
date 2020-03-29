import pandas as pd
import requests
import re


def load_data():
    '''This function gets the data from the api openzh'''
    resp = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/all')
    data = pd.DataFrame(resp.json()['records'])

    return data

def pre_process(data):
    '''create summary rows, transform col to lowercase, create prediciton column'''
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    DATE_COLUMN = 'date'
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.set_index('date', inplace=True)
    df_switzerland = data.sum(level=0)
    df_switzerland['abbreviation_canton_and_fl'] = 'CH'
    data = data.append(df_switzerland)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['prediction'] = 0

    return data


def predict(data):
    '''provides rows with prediction results'''

    # TODO predict next days
    #      maybe divide yesterday by today and multiplicate it with today
    #      to predict it with tomorrow

    return data


def postprocess_data(data):
    '''ensure all col are lowercase, transform date to index, and change all data to numeric, add prediction column'''

    for column in list(data.columns.values):
        if re.search("ncumul|ninst|Total", column):
            data[column] = pd.to_numeric(data[column])

    return data


def prep_data():
    '''calls all above functions'''
    data = load_data()
    data = pre_process(data)
    data = predict(data)
    data = postprocess_data(data)

    return data
