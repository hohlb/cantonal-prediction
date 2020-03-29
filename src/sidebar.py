import streamlit as st
import pandas as pd
import requests
import re
import src.equipment as eq
from src.main_area import create_main_area

# TODO replace with data_prep.py
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


def create_sidebar():
    sidebar = st.sidebar

    sidebar.markdown("# Frame")

    data = load_data()
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = sidebar.selectbox("Select a canton", cantons, 0)
    create_main_area(data, canton)

    sidebar.slider('Masks (per day, coworker, and patient)',
              min_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    sidebar.slider('Pair of Gloves (per day, coworker, and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    sidebar.slider('Units of Sanitizer (per day, coworker, and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__STEP)
