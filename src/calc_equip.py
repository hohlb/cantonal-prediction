import pandas as pd


def calc_equip(data, ratio_dict):
    '''provides rows with prediction results'''
    pd.to_numeric(data['ncumul_conf'])

    for key, value in ratio_dict.items():
        data[key] = data['ncumul_conf'].apply(lambda x: value * x)

    return data
