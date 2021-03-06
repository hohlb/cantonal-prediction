import streamlit as st
import src.constants as eq


def create_inputs(sidebar):
    masks = sidebar.slider('Masks (per day and patient)',
              min_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_PER_PATIENT__DEFAULT)

    # visual separation
    sidebar.markdown('')

    gloves_pair = sidebar.slider('Pairs of Gloves (per day and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__DEFAULT)

    # visual separation
    sidebar.markdown('')

    sanitizer = sidebar.slider('Liters of Sanitizer (per day and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__STEP)

    # visual separation
    sidebar.markdown('')
    sidebar.markdown('')
    sidebar.markdown('')

    hospitalized = sidebar.slider('Hospitalized Cases (percentage)',
              min_value=eq.HOSPITALIZED_CASES_PERCENTAGE__MIN,
              max_value=eq.HOSPITALIZED_CASES_PERCENTAGE__MAX,
              value=eq.HOSPITALIZED_CASES_PERCENTAGE__DEFAULT)

    return masks, gloves_pair, sanitizer, hospitalized


def create_canton_selector(sidebar, data):
    cantons = sorted(data.abbreviation_canton_and_fl.unique())
    canton = sidebar.selectbox("Select a canton", cantons, index = cantons.index('ZH'))

    return canton


def create_sidebar(data):
    sidebar = st.sidebar

    sidebar.title("Settings")

    # visual separation
    sidebar.markdown('')
    sidebar.markdown('')

    canton = create_canton_selector(sidebar, data)

    # visual separation
    sidebar.markdown('')
    sidebar.markdown('')
    sidebar.markdown('')

    inputs = canton, *create_inputs(sidebar)

    # visual separation
    sidebar.markdown('')
    sidebar.markdown('')

    sidebar.markdown('[This project is open-source](https://github.com/hohlb/cantonal-prediction)')

    return inputs
