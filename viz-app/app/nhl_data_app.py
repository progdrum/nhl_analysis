from flask import Flask, render_template, request
from bokeh.embed import server_document


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
    if stats_view == 'basic':
        script = server_document('https://localhost:5006/goalies_basic')
        return render_template("goalies_basic.html", script=script)
    elif stats_view == 'enhanced':
        script = server_document('https://localhost:5006/goalies_faceted')
        return render_template("goalies_advanced.html", script=script)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
