import streamlit as st
from src.calc_equip import calculate_needed_equipment


def create_main_area(data, canton, masks, gloves_pair, sanitizer):
    st.title('COVID19 Equipment Predictor')

    needed_equipment = calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer)
    st.write(needed_equipment)
