import csv
from mimetypes import init
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


    def bfs(self,init_point=50,end_point=360):
        visited = [False] * (len(self.players) + 1)
        leave = False
        predecessors = [0] * (len(self.players) + 1)
        caminho = []
        queue = []

        visited[init_point] = True
        queue.append(init_point)
        
        if init_point == end_point:
            return 0

        while queue:
            current_node = queue.pop(0)
            for i in list(self.players[current_node].conexoes.split(", ")):
                i = int(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    predecessors[i] = current_node
                if i == end_point:
                    leave = True
                    break
            if leave:
                break
        
        x = end_point
        while x != init_point:
            caminho.append(x)
            x = predecessors[x]
        print(caminho)
        return caminho


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
                p.conexoes = row[4]
                rows.append(p)
        self.players = rows
        return rows