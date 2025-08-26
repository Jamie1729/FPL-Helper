import re
import time, requests, pandas as pd,matplotlib.pyplot as plt
from pprint import pprint
import pickle
import numpy as np
from hmmlearn import hmm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from utilities import *
import sklearn.preprocessing as pp
import os


fig, ax = plt.subplots()
pd.set_option('display.max_columns', None)
fpl_base_url = 'https://fantasy.premierleague.com/api/'

EMPTY_GAMEWEEK_ROW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,False,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,False,0]

def main():
    all_players_gws = map(lambda filename : pd.read_csv("./2024-25/players/"+filename+"/gw.csv"),
                          os.listdir("./2024-25/players/"))
    all_players_gws = list(filter(hasEnoughMins, all_players_gws))
    for player_gws in all_players_gws:
        if len(player_gws)<38: fillEmptyWeeks(player_gws);

    scaler = StandardScaler()
    Xs = list(map(lambda player_gw: player_gw[['assists','bonus','bps','clean_sheets','creativity','expected_assists','expected_goal_involvements',
                                         'expected_goals','expected_goals_conceded','goals_conceded','goals_scored','ict_index','influence',
                                        'minutes','own_goals','penalties_missed','penalties_saved','red_cards','saves','threat',
                                         'yellow_cards','fixture']],all_players_gws))
    Xs = list(map(lambda player_gws: scaler.fit_transform(player_gws), Xs))

    Ys = list(map(lambda player_gw : player_gw[['total_points','minutes']],all_players_gws))
    points_in_90 = list(map(lambda player_points: 90 * sum(player_points['total_points']) / sum(player_points['minutes']),
                             Ys))
    points_mean = np.mean(points_in_90)
    points_std  = np.std(points_in_90)

    # noinspection PyTypeChecker
    bad_form_mean  = points_mean-1.5*points_std
    ok_form_mean   = points_mean
    # noinspection PyTypeChecker
    good_form_mean = points_mean+1.5*points_std

    n_form_states = 3
    model = hmm.GaussianHMM(n_form_states, covariance_type='full',
                            startprob_prior=np.array([0.2, 0.7, 0.1]),
                            transmat_prior =np.array([[0.4, 0.5, 0.1],
                                                      [0.2, 0.6, 0.2],
                                                      [0.1, 0.6, 0.3]])
                            )

    X = np.concatenate(Xs)

    model.fit(X, [38]*len(Xs))



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