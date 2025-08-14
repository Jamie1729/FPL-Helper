import time, requests, pandas as pd,matplotlib.pyplot as plt
from data_funcs import *
from importlib.metadata import distribution

fig, ax = plt.subplots()
pd.set_option('display.max_columns', None)
fpl_base_url = 'https://fantasy.premierleague.com/api/'

def main():
    for i in range(1,39):
        url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/gws/gw{i}.csv"
        pd.read_csv(url).to_csv(f'./2425_gws/gw{i}.csv')

def learn_points_distribution(df):
    #NOT YET IMPLEMENTED
    return None


if __name__ == '__main__':
    main()