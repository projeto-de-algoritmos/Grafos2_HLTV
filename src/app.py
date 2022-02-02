from flask import Flask
from flask import render_template

from graph import Graph

app = Flask(__name__)

@app.route("/")
def index():
    c = Graph()
    c.load()
    return render_template('form.html', grafo=c)

@app.route("/ans/")
def ans(list_players=None):
    return render_template('ans.html', list_players=list_players)

if __name__ == "__main__":
    #Verifica se tem o arquivo csv, se nao tem, busca na hltv

    #Executa o app.
    app.run(debug=False)
