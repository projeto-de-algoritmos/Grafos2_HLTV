import csv
from player import Player

class Graph:
    def __init__(self,players=[],storage="storage.csv"):
        self.players = players
        self.storage = storage
        self.size = len(players)

    def add_player(self,player):
        for p in self.players:
            if p.nome == player.nome:
                return p

        player.identificador = self.size
        self.size += 1
        self.players.append(player)
        return player

    def connect(self, id1, id2):
        self.players[id1].connect(id2)
        self.players[id2].connect(id1)

    def save(self):
        with open(self.storage,'w') as f:
            # Pega o primeiro player, transformou em dicionario e fez um array com o nome das chaves.
            header = [key for key in self.players[0].to_dict().keys()]
            list_players = [p.to_dict() for p in self.players]

            writer = csv.DictWriter(f, fieldnames=header, delimiter=";")
            writer.writeheader()
            writer.writerows(list_players)


    def load(self):
        with open(self.storage, newline='') as f:
            csvreader = csv.reader(f, delimiter=';')
            header = next(csvreader)
            rows = []
            for row in csvreader:
                p = Player()
                p.nome = row[0]
                p.foto = row[1]
                p.nacionalidade = row[2]
                p.identificador = row[3]
                p.conexoes = [int(x) for x in row[4].split(", ")]
                rows.append(p)
        self.players = rows
        self.size = len(self.players)
        return rows