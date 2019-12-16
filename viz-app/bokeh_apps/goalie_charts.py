import requests
import pandas as pd
import hockey_vars as hov
from bokeh.layouts import gridplot, column


def get_roster_data():
    rosters = requests.get(hov.BASE_URL + 'teams', params={'expand': 'team.roster',
                                                   'season': '20192020'})
    roster_dict = rosters.json()
    rosters = [{'team_name': team['name'],
                'team_roster': team['roster']} for team in roster_dict['teams']]
    return rosters


def get_goalie_data(name_id):
    gid = name_id['id']
    goalie_info = requests.get(f'{hov.BASE_URL}people/{gid}/stats',
                               params={'stats': 'statsSingleSeason',
                                       'season': '20192020'}).json()
    splits = goalie_info['stats'][0]['splits']
    if len(splits) > 0:
        return {**name_id, **splits[0]['stat']}
    return {**name_id, **goalie_info}


# Return team colors for the plot
def get_team_color(team_name):
    return hov.TEAM_COLORS_DICT[team_name]


def create_goalie_df(rosters):
    goalies = []
    for roster in rosters:
        for player in roster['team_roster']['roster']:
            if player['position']['code'] == 'G':
                player['team'] = roster['team_name']
                goalies.append({'id': player['person']['id'],
                                'name': player['person']['fullName'],
                                'team': player['team']})
    goalie_stats = [get_goalie_data(goalie) for goalie in goalies]
    goalie_stats = list(filter(lambda x: 'copyright' not in x.keys(), goalie_stats))
    goalie_df = pd.DataFrame(goalie_stats)

    # Clean up some of the save percentages
    goalie_df[['evenStrengthSavePercentage',
            'powerPlaySavePercentage',
            'shortHandedSavePercentage']] = (goalie_df[['evenStrengthSavePercentage',
            'powerPlaySavePercentage',
            'shortHandedSavePercentage']] / 100).round(3)

    # Add colors for each team
    goalie_df = goalie_df.assign(
        team_color=goalie_df.team.apply(lambda x: get_team_color(x)))
    return goalie_df
