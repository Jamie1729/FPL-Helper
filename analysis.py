import re
import time, requests, pandas as pd,matplotlib.pyplot as plt

import numpy as np

from data_funcs import *
from sklearn.preprocessing import StandardScaler
import os

fig, ax = plt.subplots()
pd.set_option('display.max_columns', None)
fpl_base_url = 'https://fantasy.premierleague.com/api/'

def main():
    minutes = map(lambda filename : pd.read_csv("./2024-25/players/"+filename+"/gw.csv")['minutes'],
                    os.listdir("./2024-25/players/"))
    minutes = pd.DataFrame(list(filter(hasEnoughMins, minutes)))
    print(minutes)

    #scaler = StandardScaler()
    #minutes = scaler.fit_transform(minutes)


    #plt.plot(player_gw_data['minutes'])
    #plt.title(filename)
    #plt.xlabel("Game Week")
    #plt.ylabel("Minutes Played")
    #plt.show()


def hasEnoughMins(arr):
    return sum(arr) >= 500



if __name__ == '__main__':
    main()