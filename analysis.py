import re
import time, requests, pandas as pd,matplotlib.pyplot as plt
from pprint import pprint
import numpy as np

from data_funcs import *
from sklearn.preprocessing import StandardScaler
import os


fig, ax = plt.subplots()
pd.set_option('display.max_columns', None)
fpl_base_url = 'https://fantasy.premierleague.com/api/'

EMPTY_GAMEWEEK_ROW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,False,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,False,0]

def main():
    #minutes = map(lambda filename : pd.read_csv("./2024-25/players/"+filename+"/gw.csv")['minutes'],
    #                os.listdir("./2024-25/players/"))
    #minutes = pd.DataFrame(list(filter(hasEnoughMins, minutes)))
    #minutes = minutes.drop(columns=38,axis=1)

    all_player_gws = map(lambda filename : pd.read_csv("./2024-25/players/"+filename+"/gw.csv"),os.listdir("./2024-25/players/"))
    all_player_gws = list(filter(hasEnoughMins, all_player_gws))

    for player_gws in all_player_gws:
        if len(player_gws)<38:
            fillEmptyWeeks(player_gws)


    #scaler = StandardScaler()
    #minutes = scaler.fit_transform(minutes)


def fillEmptyWeeks(player_gws):
    gws_played = (player_gws['fixture'] // 10)
    for i in range(38):
        if i not in gws_played:
            player_gws.loc[-1] = EMPTY_GAMEWEEK_ROW
            player_gws.index += 1
    player_gws.sort_index(inplace=True)



def hasEnoughMins(player_gws):
    return sum(player_gws['minutes']) >= 500

def plotGameweekMins(player_gw_data,filename):
    plt.plot(player_gw_data['minutes'])
    plt.title(filename)
    plt.xlabel("Game Week")
    plt.ylabel("Minutes Played")
    plt.show()

if __name__ == '__main__':
    main()