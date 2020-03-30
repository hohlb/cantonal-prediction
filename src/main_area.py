import os.path
from pandas import Timestamp
import streamlit as st
from src.calc_equip import calculate_needed_equipment


def create_main_area(data, canton, masks, gloves_pair, sanitizer, hospitalized):
    needed_equipment = calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer, hospitalized)
    day = get_day(needed_equipment)

    st.title('COVID19 Equipment Predictor')

    st.markdown(f"## Needed Equipment on {day}")
    st.write(f"Region: {canton}")

    place_icons(needed_equipment)

    st.write(needed_equipment)


def get_furthest_prediction(needed_equipment):
    return needed_equipment.tail(1)


def get_day(needed_equipment):
    furthest_prediction = get_furthest_prediction(needed_equipment)
    day = furthest_prediction.index.values[0]
    day = Timestamp(day).to_pydatetime()
    day = day.strftime("%A, %d %B %Y")

    return day


def place_icons(needed_equipment):
    script_directory = os.path.dirname(__file__)
    icons_directory = os.path.join(script_directory, '..', 'icons')

    image_width = 200  # pixels

    st.image(os.path.join(icons_directory, 'mask.jpg'),
             width=image_width,
             caption=needed_equipment_count(needed_equipment, 'masks', 'Masks'))

    st.image(os.path.join(icons_directory, 'gloves.jpg'),
             width=image_width,
             caption=needed_equipment_count(needed_equipment, 'gloves_pairs', 'Pairs of Gloves'))

    st.image(os.path.join(icons_directory, 'sanitizer.png'),
             width=image_width,
             caption=needed_equipment_count(needed_equipment, 'sanitizers', 'Liters of Sanitizer'))

    style_icons(image_width)


def needed_equipment_count(needed_equipment, column, name):
    furthest_prediction = get_furthest_prediction(needed_equipment)
    equipment_count = int(furthest_prediction.iloc[0][column])
    equipment_count = f"{equipment_count:,}".replace(',', "'")  # separate thousands with ' (TODO use locale to determine separators)

    return f"{equipment_count} {name}"


def style_icons(image_width):
    # since streamlit is lacking a grid as for now,
    # we use CSS via markdown to style the icons

    position_of_first_icon = 4

    css = f"""
    <style>
        /* align icons horizontally */

        .main .element-container:nth-of-type({position_of_first_icon}),
        .main .element-container:nth-of-type({position_of_first_icon + 1}),
        .main .element-container:nth-of-type({position_of_first_icon + 2}) {{
            display: table-cell;
            width: {image_width}px !important;
        }}

        .main .element-container:nth-of-type({position_of_first_icon}) > .fullScreenFrame > div,
        .main .element-container:nth-of-type({position_of_first_icon + 1}) > .fullScreenFrame > div,
        .main .element-container:nth-of-type({position_of_first_icon + 2}) > .fullScreenFrame > div {{
            width: {image_width}px !important;
        }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
