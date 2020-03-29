import streamlit as st
import pandas as pd
import requests
import re


DATE_COLUMN = 'date'
resp = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/all')


# @st.cache
def load_data():
    data = pd.DataFrame(resp.json()['records'])
    lowercase = lambda x: str(x).lower()

    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    for column in list(data.columns.values):
        if re.search("ncumul|ninst|Total", column):
            data[column] = pd.to_numeric(data[column])

    data.set_index('date', inplace = True)

    #data.rename(columns={'ncumul_conf': 'confirmed', 'ncumul_deceased': 'deaths',
    # 'abbreviation_canton_and_fl' : 'country'}, inplace=True)
    return data




def bhohl():
    st.title('START bhohl')

    data = load_data()
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = st.selectbox("Select a canton", cantons, 0)
    st.write(data[data['abbreviation_canton_and_fl'] == canton])

    st.title('END bhohl')
