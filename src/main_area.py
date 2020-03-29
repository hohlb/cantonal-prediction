import streamlit as st


def create_main_area(data, canton):
    st.write(data[data['abbreviation_canton_and_fl'] == canton])
