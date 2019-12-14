import goalie_charts as gc
from flask import Flask, render_template, request
from bokeh.embed import components


app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    if name == None:
        name = 'Postulio'
    return render_template('index.html', name=name)


@app.route('/goalie-stats')
def goalie_stats():
    stats_view = request.args.get('statsview', default='basic')
    gdf = gc.create_goalie_df(gc.get_roster_data())
    if stats_view == 'basic':
        script, div = components(gc.basic_svp_graph(gdf))
        return render_template("goalies_basic.html", script=script, div=div)
    elif stats_view == 'enhanced':
        return gc.faceted_svp_plot(gdf)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
