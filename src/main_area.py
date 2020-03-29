import streamlit as st


def create_main_area(data, canton, masks, gloves, sanitizer):
    st.write(data[data['abbreviation_canton_and_fl'] == canton])

    # this is just to show that we can use the variables
    # masks, gloves, sanitizer
    st.write(masks)
    st.write(gloves)
    st.write(sanitizer)
