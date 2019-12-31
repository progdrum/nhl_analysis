from flask import Flask, render_template, request
from bokeh.embed import server_document, server_session
from bokeh.client import pull_session


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/goalie-stats')
def goalie_stats():
    stats_view = request.args.get('statsview', default='basic')
    if stats_view == 'basic':
        with pull_session(url='http://localhost:5006/goalies_basic') as session:
            script = server_session(session_id=session.id,
                                    url='http://localhost:5006/goalies_basic')
            return render_template("goalies_basic.html", script=script)
    elif stats_view == 'enhanced':
        with pull_session(url='http://localhost:5007/goalies_faceted') as session:
            script = server_session(session_id=session.id,
                                    url='http://localhost:5007/goalies_faceted')
            return render_template("goalies_advanced.html", script=script)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
