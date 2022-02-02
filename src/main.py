from graph import Graph
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    c = Graph()
    c.load()
    return render_template('main.html', grafo=c)

@app.route("/ans/")
def ans(list_players=None):
    return render_template('ans.html', list_players=list_players)