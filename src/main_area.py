import os.path
import streamlit as st
from src.calc_equip import calculate_needed_equipment


def create_main_area(data, canton, masks, gloves_pair, sanitizer):
    st.title('COVID19 Equipment Predictor')

    place_icons()

    needed_equipment = calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer)
    st.write(needed_equipment)


def place_icons():
    script_directory = os.path.dirname(__file__)
    icons_directory = os.path.join(script_directory, '..', 'icons')

    st.image(os.path.join(icons_directory, 'mask.jpg'),
             width=200,
             caption="Masks")

    st.image(os.path.join(icons_directory, 'gloves.jpg'),
             width=200,
             caption="Gloves")

    st.image(os.path.join(icons_directory, 'sanitizer.png'),
             width=200,
             caption="Sanitizer")

    style_icons()


def style_icons():
    # since streamlit is lacking a grid as for now,
    # we use CSS via markdown to style the icons

    css = """
    <style>
        /* align icons horizontally */
        .main .element-container:nth-of-type(2),
        .main .element-container:nth-of-type(3),
        .main .element-container:nth-of-type(4) {
            display: table-cell;
            width: 200px !important;
        }
        .main .element-container:nth-of-type(2) > .fullScreenFrame > div,
        .main .element-container:nth-of-type(3) > .fullScreenFrame > div,
        .main .element-container:nth-of-type(4) > .fullScreenFrame > div {
            width: 200px !important;
        }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
