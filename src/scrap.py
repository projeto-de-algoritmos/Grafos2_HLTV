from bs4 import BeautifulSoup
import requests
import re

from graph import Graph
from player import Player

class Crawler:
    def __init__(self,link_root=""):
        self.link_root = "https://www.hltv.org/stats/teams"
        self.headers = {}
        self.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KH    TML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        self.headers["Refer"] = "https://www.hltv.org/stats/teams"
        self.grafo = Graph()

    def get_page(self, link):
        return requests.get(link,headers=self.headers)

    def walk_teams(self):
        page = self.get_page(self.link_root)
        soup = BeautifulSoup(page.text, 'html.parser')

        for team in soup.find_all("td", {"class":"teamCol-teams-overview"}):
            link_team = self.link_root + "/lineups/" + team.a['href'][13:]
            self.get_lineups(link_team)

    def get_lineups(self,link_team):
        page = self.get_page(link_team)
        soup = BeautifulSoup(page.text,'html.parser')

        for line in soup.find_all("div",{"class":"lineup-container"}):
            self.extract_players(line)

    def connect_lineup(self,list_players):
        for i in range(len(list_players)):
            list_players[i] = self.grafo.add_player(list_players[i])

        for i in range(len(list_players) - 1) :
            for j in range( i + 1, len(list_players)):
                self.grafo.connect(list_players[i].identificador,list_players[j].identificador)

    def extract_players(self, line):
        line_player = []
        for raw_player in line.find_all("div", {"class":"col teammate"}):
            p = Player()
            p.conexoes = []
            p.foto = raw_player.img['src']
            p.nome = re.match(r'/stats/players/\d+/(.+)',raw_player.div.a['href']).group(1)
            p.nacionalidade = raw_player.div.img['alt']
            line_player.append(p)
        self.connect_lineup(line_player)
