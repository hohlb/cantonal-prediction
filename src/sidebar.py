import streamlit as st
import src.equipment as eq
from src.main_area import create_main_area
from src.data_prep import prep_data


def create_equipment_inputs(sidebar):
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


def create_canton_selector(sidebar):
    data = prep_data()
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = sidebar.selectbox("Select a canton", cantons, 0)
    create_main_area(data, canton)


def create_sidebar():
    sidebar = st.sidebar

    sidebar.markdown("# Frame")

    create_canton_selector(sidebar)
    create_equipment_inputs(sidebar)
