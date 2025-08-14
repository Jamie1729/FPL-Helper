import pandas as pd

from data_funcs import *
fig, ax = plt.subplots()
pd.set_option('display.max_columns', None)

from enum import Enum


class TEAM(Enum):
    ARS = 1
    AVL = 2
    BUR = 3
    BOU = 4
    BRE = 5
    BHA = 6
    CHE = 7
    CRY = 8
    EVE = 9
    FUL = 10
    LEE = 11
    LIV = 12
    MCI = 13
    MUN = 14
    NEW = 15
    NFO = 16
    SUN = 17
    TOT = 18
    WHU = 19
    WOL = 20
class POS(Enum):
    GKP = 1
    DEF = 2
    MID = 3
    ATK = 4

data_file_names = ["gks","defs","mids","atks"]
def main():
    if not all(map(playerFileExists, data_file_names)):
        all_data = requests.get(fpl_base_url+'bootstrap-static/').json()

        player_data = pd.json_normalize(all_data['elements'])
        teams = pd.json_normalize(all_data['teams'])
        positions = pd.json_normalize(all_data['element_types'])

        df = pd.merge(left=player_data, right=teams, left_on='team',right_on='id')
        df = df.merge(positions, left_on='element_type', right_on='id')
        df = df.rename( columns={'name': 'team_name', 'singular_name': 'position_name'} )
        #['id','first_name','second_name','web_name','team','element_type']

        for pid in player_data.index:
             player_season = get_season_history(pid+1)
             if player_season.size == 0:
                 df.drop(pid, inplace=True)
                 continue
             if sum(player_season['minutes']) <= 400:
                df.drop(pid, inplace=True)
                continue

        df[df['id']==1].to_csv('./players/gks.csv')
        df[df['id']==2].to_csv('./players/defs.csv')
        df[df['id']==3].to_csv('./players/mids.csv')
        df[df['id']==4].to_csv('./players/atks.csv')
    else:
        print("Player data already stored locally.")
        GKs = pd.read_csv('./players/gks.csv')
        DEFs = pd.read_csv('./players/defs.csv')
        MIDs = pd.read_csv('./players/mids.csv')
        ATKs = pd.read_csv('./players/atks.csv')

    


if __name__ == '__main__':
    main()

