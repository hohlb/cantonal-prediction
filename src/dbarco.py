import streamlit as st


def get_selection(data):
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = st.selectbox("Select a canton", cantons, 0)
    st.write(data[data['abbreviation_canton_and_fl'] == canton])
