import streamlit as st
import pandas as pd
import numpy as np
import requests
import re


# ATTENTION
# this is for now just the uber_pickup tutorial, it will be replaced soon with our actual code

st.title('COVID19 Equipment Calculator')

from src import data_prep

ratio_dict = {'mask_ratio' : 35, 'desinf_ratio' : 0.5, 'overall_ratio': 25}
data_prep.prep_all(ratio_dict)


# DATE_COLUMN = 'date'
# resp = requests.get('https://covid19-rest.herokuapp.com/api/openzh/v1/all')
#
# @st.cache
# def load_data(nrows):
#     data = pd.DataFrame(resp.json()['records'])
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     for column in list(data.columns.values):
#         if re.search("ncumul|ninst|Total", column):
#             data[column] = pd.to_numeric(data[column])
#     data.set_index('date', inplace = True)
#     #data.rename(columns={'ncumul_conf': 'confirmed', 'ncumul_deceased': 'deaths', 'abbreviation_canton_and_fl' : 'country'}, inplace=True)
#     return data

data_load_state = st.text('Loading data...')
data = data_prep.load_data()
data_load_state.text('Loading data... done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
    

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
