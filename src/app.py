from crypt import methods
from flask import Flask, render_template, request

from scrap import Crawler
from graph import Graph
from control import Control

import os

app = Flask(__name__)

global G 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form_scc")
def form_scc():
    return render_template('form_scc.html', grafo=G)

@app.route("/ans_scc", methods=['POST'])
def ans_scc():
    main_player = G.players[int(request.form['player1'])]
    set_players = G.players[5:50]
    return render_template('scc.html',set_players=set_players, main_player=main_player)

@app.route("/form")
def form():
    return render_template('form.html', grafo=G)

@app.route("/ans", methods=['POST'])
def ans():
    list_players = Control.bfs(G,int(request.form['player2']),int(request.form['player1']))
    return render_template('ans.html', list_players=list_players)

if __name__ == "__main__":
    """
    Verifica se tem o arquivo csv, se nao tem, busca na hltv.
    Carrega o grafo G com o arquivo csv, ou com os dados da memoria gerados pelo crawler.
    """
    if not os.path.exists('./storage.csv'):
        print("FILE 'storage.csv' not found\nHunting data from hltv.org")
        c = Crawler()
        c.walk_teams()
        c.grafo.save()
        G = c.grafo
    else:
        G = Graph()
        G.load()
    #Executa o app.
    app.run(debug=False)
