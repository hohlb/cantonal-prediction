import pandas as pd


def calc_equip(data, ratio_dict):
    '''provides rows with prediction results'''
    pd.to_numeric(data['ncumul_conf'])

    for key, value in ratio_dict.items():
        data[key] = data['ncumul_conf'].apply(lambda x: value * x)

    return data


def calculate_needed_equipment(data, canton, masks, gloves_pair, sanitizer):
    # filter by canton
    region_data = data[data['abbreviation_canton_and_fl'] == canton]

    equip = {
        'masks': masks,
        'gloves_pairs': gloves_pair,
        'sanitizers': sanitizer
    }

    needed_equip = calc_equip(region_data, equip)

    # show needed equipment for the newest time period
    days = 7
    recent_period = needed_equip.tail(days)
    recent_period = recent_period[[
        'masks', 'gloves_pairs', 'sanitizers'
    ]]

    return recent_period
