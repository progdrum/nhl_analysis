import hockey_vars as hov
import goalie_charts as gc

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool, Slider


GDF = gc.create_goalie_df(gc.get_roster_data())
SOURCE = ColumnDataSource(data=GDF)
MIN_GAMES = Slider(title='Minimum Number of Games Played (Default: 5)',
                   start=1, end=GDF.games.max(), value=5, step=1)

def basic_svp_graph():
    p = figure(tooltips=hov.TOOLTIPS)
    p.circle('savePercentage', 'goalAgainstAverage', size=10, source=SOURCE,
             color='team_color')
    return p


def change_min_games(attr, old, new):
    return GDF.loc[GDF.games >= MIN_GAMES.value]


def update():
    filtered_gdf = GDF.loc[GDF.games >= MIN_GAMES.value]
    SOURCE.data = filtered_gdf

MIN_GAMES.on_change('value', lambda attr, old, new: update())

update()

LAYOUT = column(basic_svp_graph(), MIN_GAMES)

curdoc().add_root(LAYOUT)
curdoc().title = 'Basic Goalie Stats'
