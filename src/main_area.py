import streamlit as st
from src.calc_equip import calc_equip


def create_main_area(data, canton, masks, gloves_pair, sanitizer):
    st.title('COVID19 Equipment Predictor')

    needed_equipment = calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer)
    st.write(needed_equipment)


def calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer):
    # filter by canton
    region_data = data[data['abbreviation_canton_and_fl'] == canton]

    equip = {
        'mask': masks,
        'gloves_pair': gloves_pair,
        'sanitizer': sanitizer
    }

    needed_equip = calc_equip(region_data, equip)

    # show needed equipment for the newest time period
    days = 7
    recent_period = needed_equip.tail(days)
    recent_period = recent_period[[
        'mask', 'gloves_pair', 'sanitizer'
    ]]

    return recent_period
