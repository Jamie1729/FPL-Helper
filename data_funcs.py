import time, requests, pandas as pd,matplotlib.pyplot as plt, os
from importlib.metadata import distribution
fpl_base_url = 'https://fantasy.premierleague.com/api/'

def playerFileExists(path):
    return os.path.exists("./players/"+path+".json")

def get_gameweek_history(player_id):
    r = requests.get(
        fpl_base_url + 'element-summary/' + str(player_id) + '/'
    ).json()
    df = pd.json_normalize(r['history'])
    return df

def get_season_history(player_id):
    r = requests.get(
        fpl_base_url + 'element-summary/' + str(player_id) + '/'
    ).json()
    df = pd.json_normalize(r['history_past'])
    return df


def plot_player_metric_history(player_id, metric):
    try:
        plt.plot(get_season_history(player_id)['season_name'], get_season_history(player_id)[metric])
        plt.title(player_id)
        plt.show()
    except KeyError:
        print("No data found for metric: "+metric)