import streamlit as st
from src.calc_equip import calc_equip


def create_main_area(data, canton, masks, gloves_pair, sanitizer):
    st.title('COVID19 Equipment Calculator')

    # filter by canton
    region_data = data[data['abbreviation_canton_and_fl'] == canton]

    equip = {
        'mask': masks,
        'gloves_pair': gloves_pair,
        'sanitizer': sanitizer
    }

    needed_equip = calc_equip(region_data, equip)
    st.write(needed_equip)
