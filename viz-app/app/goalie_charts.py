import requests
import pandas as pd
import hockey_vars as hov
from bokeh.layouts import gridplot, column
from bokeh.models import HoverTool
from bokeh.plotting import figure, ColumnDataSource


BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'

def get_roster_data():
    rosters = requests.get(BASE_URL + 'teams', params={'expand': 'team.roster',
                                                   'season': '20192020'})
    roster_dict = rosters.json()
    rosters = [{'team_name': team['name'],
                'team_roster': team['roster']} for team in roster_dict['teams']]
    return rosters


def get_goalie_data(name_id):
    gid = name_id['id']
    goalie_info = requests.get(f'{BASE_URL}people/{gid}/stats',
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

    # Only include goalies that have played at least 5 games.
    goalie_df = goalie_df.loc[goalie_df.games >= 5]

    # Add colors for each team
    goalie_df = goalie_df.assign(
        team_color=goalie_df.team.apply(lambda x: get_team_color(x)))
    return goalie_df


def basic_svp_graph(goalie_df):
    source = ColumnDataSource(data=goalie_df)
    p = figure(tooltips=hov.TOOLTIPS)
    p.circle('savePercentage', 'goalAgainstAverage', size=10, source=source,
             color='team_color')
    return p


def faceted_svp_plot(goalie_df):
    source = ColumnDataSource(data=goalie_df)

    # Plot overall save percentage
    overall = figure(title='Overall', plot_width=300, plot_height=300,
                     tools=hov.TOOLS, tooltips=hov.TOOLTIPS)
    overall.circle('savePercentage', 'goalAgainstAverage', size=10, color='team_color',
                   source=source)

    # Plot even strength save percentage
    even_strength = figure(title='Even Strength', plot_width=300, plot_height=300,
                           tools=hov.TOOLS, tooltips=hov.ES_TOOLTIPS)
    even_strength.circle('evenStrengthSavePercentage', 'goalAgainstAverage',
                         size=10, color='team_color', source=source)

    # Plot SH save percentage
    shorthanded = figure(title='Shorthanded', plot_width=300, plot_height=300,
                         tools=hov.TOOLS, tooltips=hov.SH_TOOLTIPS)
    shorthanded.circle('shortHandedSavePercentage', 'goalAgainstAverage',
                       size=10, color='team_color', source=source)

    # Plot PP save percentage
    power_play = figure(title='Power Play', plot_width=300, plot_height=300,
                        tools=hov.TOOLS, tooltips=hov.PP_TOOLTIPS)
    power_play.circle('powerPlaySavePercentage', 'goalAgainstAverage',
                      size=10, color='team_color', source=source)

    return gridplot([[overall, even_strength], [shorthanded, power_play]])
