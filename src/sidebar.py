import streamlit as st
import src.constants as eq


def create_inputs(sidebar):
    masks = sidebar.slider('Masks (per day and patient)',
              min_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_PER_PATIENT__DEFAULT)

    gloves_pair = sidebar.slider('Pairs of Gloves (per day and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__DEFAULT)

    sanitizer = sidebar.slider('Liters of Sanitizer (per day and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__STEP)

    hospitalized = sidebar.slider('Percentage of Hospitalized Cases',
              min_value=eq.HOSPITALIZED_CASES_PERCENTAGE__MIN,
              max_value=eq.HOSPITALIZED_CASES_PERCENTAGE__MAX,
              value=eq.HOSPITALIZED_CASES_PERCENTAGE__DEFAULT)

    return masks, gloves_pair, sanitizer, hospitalized


def create_canton_selector(sidebar, data):
    cantons = sorted(data.abbreviation_canton_and_fl.unique())
    canton = sidebar.selectbox("Select a canton", cantons, index = cantons.index('CH'))

    return canton


def create_sidebar(data):
    sidebar = st.sidebar

    sidebar.title("Settings")

    canton = create_canton_selector(sidebar, data)
    inputs = canton, *create_inputs(sidebar)

    return inputs
