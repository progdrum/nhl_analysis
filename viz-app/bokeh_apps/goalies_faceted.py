import hockey_vars as hov
import goalie_charts as gc

from bokeh.io import curdoc
from bokeh.layouts import gridplot, column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool, Slider


GDF = gc.create_goalie_df(gc.get_roster_data())
SOURCE = ColumnDataSource(data=GDF)
MIN_GAMES = Slider(title='Minimum Number of Games Played (Default: 5)',
                   start=1, end=GDF.games.max(), value=5, step=1)

def faceted_svp_plot():
    # Plot overall save percentage
    overall = figure(title='Overall', plot_width=500, plot_height=500,
                     tools=hov.TOOLS, tooltips=hov.TOOLTIPS)
    overall.circle('savePercentage', 'goalAgainstAverage', size=10, color='team_color',
                   source=SOURCE)

    # Plot even strength save percentage
    even_strength = figure(title='Even Strength', plot_width=500, plot_height=500,
                           tools=hov.TOOLS, tooltips=hov.ES_TOOLTIPS)
    even_strength.circle('evenStrengthSavePercentage', 'goalAgainstAverage',
                         size=10, color='team_color', source=SOURCE)

    # Plot SH save percentage
    shorthanded = figure(title='Shorthanded', plot_width=500, plot_height=500,
                         tools=hov.TOOLS, tooltips=hov.SH_TOOLTIPS)
    shorthanded.circle('shortHandedSavePercentage', 'goalAgainstAverage',
                       size=10, color='team_color', source=SOURCE)

    # Plot PP save percentage
    power_play = figure(title='Power Play', plot_width=500, plot_height=500,
                        tools=hov.TOOLS, tooltips=hov.PP_TOOLTIPS)
    power_play.circle('powerPlaySavePercentage', 'goalAgainstAverage',
                      size=10, color='team_color', source=SOURCE)

    return gridplot([[overall, even_strength], [shorthanded, power_play]])


def change_min_games(attr, old, new):
    return GDF.loc[GDF.games >= MIN_GAMES.value]


def update():
    filtered_gdf = GDF.loc[GDF.games >= MIN_GAMES.value]
    SOURCE.data = filtered_gdf

MIN_GAMES.on_change('value', lambda attr, old, new: update())

update()

LAYOUT = column(faceted_svp_plot(), MIN_GAMES)
curdoc().add_root(LAYOUT)
curdoc().title = 'Advanced Goalie Stats'
