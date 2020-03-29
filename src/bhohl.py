import streamlit as st
import pandas as pd
import requests
import re
import src.equipment as eq

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

    return data


def bhohl():
    st.title('START bhohl')

    data = load_data()
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = st.selectbox("Select a canton", cantons, 0)
    st.write(data[data['abbreviation_canton_and_fl'] == canton])

    st.slider('Masks (per day, coworker, and patient)',
              min_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    st.slider('Pair of Gloves (per day, coworker, and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    st.slider('Units of Sanitizer (per day, coworker, and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__STEP)

    st.title('END bhohl')
