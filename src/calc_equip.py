import pandas as pd


def calc_equip(data, equip, hospitalized_percentage):
    '''provides rows with prediction results'''
    hospitalized_ratio = hospitalized_percentage / 100

    for key, value in equip.items():
        data[key] = data['active_cases'].apply(lambda x: value * x * hospitalized_ratio)

    return data


def calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer, hospitalized):
    # filter by canton
    region_data = data[data['abbreviation_canton_and_fl'] == canton]

    equip = {
        'masks': masks,
        'gloves_pairs': gloves_pair,
        'sanitizers': sanitizer
    }

    needed_equip = calc_equip(region_data, equip, hospitalized)

    # show needed equipment for the newest time period
    days = 7
    recent_period = needed_equip.tail(days)
    recent_period = recent_period[[
        'masks', 'gloves_pairs', 'sanitizers', 'active_cases'
    ]]

    return recent_period
