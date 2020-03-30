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
        'mask': masks,
        'gloves_pair': gloves_pair,
        'sanitizer': sanitizer
    }

    needed_equip = calc_equip(region_data, equip)

    # show needed equipment for the newest time period
    days = 7
    recent_period = needed_equip.tail(days)
    recent_period = recent_period[[
        'mask', 'gloves_pair', 'sanitizer'
    ]]

    return recent_period
