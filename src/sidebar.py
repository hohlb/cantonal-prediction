import streamlit as st
import src.equipment as eq


def create_equipment_inputs(sidebar):
    masks = sidebar.slider('Masks (per day and patient)',
              min_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.MASKS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.MASKS__PER_DAY_PER_PER_PATIENT__DEFAULT)

    gloves_pair = sidebar.slider('Pairs of Gloves (per day and patient)',
              min_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.GLOVES_PAIR__PER_DAY_PER_PER_PATIENT__DEFAULT)

    sanitizer = sidebar.slider('Units of Sanitizer (per day and patient)',
              min_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MIN,
              max_value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__MAX,
              value=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__DEFAULT,
              step=eq.SANITIZER_UNITS__PER_DAY_PER_PER_PATIENT__STEP)

    return masks, gloves_pair, sanitizer


def create_canton_selector(sidebar, data):
    cantons = sorted(data.abbreviation_canton_and_fl.unique())
    canton = sidebar.selectbox("Select a canton", cantons, index = cantons.index('CH'))

    return canton


def create_sidebar(data):
    sidebar = st.sidebar

    sidebar.markdown("# Frame")

    canton = create_canton_selector(sidebar, data)
    masks, gloves_pair, sanitizer = create_equipment_inputs(sidebar)

    return canton, masks, gloves_pair, sanitizer
