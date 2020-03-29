import streamlit as st

st.title('COVID19 Equipment Calculator')

from src import data_prep

ratio_dict = {'mask' : 35, 'desinfectant' : 0.5, 'overall': 25}

data_load_state = st.text('Loading data...')
data = data_prep.prep_all(ratio_dict)
data_load_state.text('Loading data... done!')

