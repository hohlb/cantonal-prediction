import streamlit as st
import src.equipment as eq


def create_equipment_inputs(sidebar):
    masks = sidebar.slider('Masks (per day, coworker, and patient)',
              min_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    gloves = sidebar.slider('Pair of Gloves (per day, coworker, and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT)

    sanitizer = sidebar.slider('Units of Sanitizer (per day, coworker, and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_COWORKER_PER_PATIENT__STEP)

    return masks, gloves, sanitizer


def create_canton_selector(sidebar, data):
    cantons = data.abbreviation_canton_and_fl.unique()
    canton = sidebar.selectbox("Select a canton", cantons, 0)

    return canton


def create_sidebar(data):
    sidebar = st.sidebar

    sidebar.markdown("# Frame")

    canton = create_canton_selector(sidebar, data)
    masks, gloves, sanitizer = create_equipment_inputs(sidebar)

    return canton, masks, gloves, sanitizer
