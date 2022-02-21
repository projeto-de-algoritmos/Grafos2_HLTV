from typing import Type, List
from graph import Graph
from player import Player
from ufds import UFDS

class Control:
    def __init__(self) -> None:
        pass

    @staticmethod
    def bfs(G:Type[Graph],init_point:int=9,end_point:int=30) ->List[Type[Player]]:
        visited = [False] * (len(G.players) + 1)
        leave = False
        predecessors = [0] * (len(G.players) + 1)
        caminho = []
        queue = []

        visited[init_point] = True
        queue.append(init_point)
        
        if init_point == end_point:
            return [G.players[init_point],G.players[init_point]]

        while queue:
            current_node = queue.pop(0)
            for i in G.players[current_node].conexoes:
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
            caminho.append(G.players[x])
            x = predecessors[x]
        caminho.append(G.players[x])
        return caminho


    def scc(self,G:Type[Graph], id_player:int) -> List[Type[Player]]:
        size_players = G.size

        list_tree = []
        index = 0
        visited = [False] * (size_players)

        sets = UFDS(size_players)
        sets_header = set()

        # Monta os conjuntos
        for i in range(size_players):
            if not visited[i]:
                self.dfs(G,sets,i,visited)

        # Encontra o no principal de cada conjunto
        for i in range(size_players):
            sets.findSet(i)
            sets_header.add(sets.parents[i])

        # Cria listas com o no dominante do conjunto
        for s in sets_header:
            list_tree.append([ G.players[s] ])
        
        # Adiciona os players em seu conjunto pertinente
        for i in range(size_players):
            for j in range(len(sets_header)):
                if sets.isSameSet(i,list_tree[j][0].identificador):
                    list_tree[j].append(G.players[i])
                    if i == id_player:
                        index = j
                        print("Entrei, id_Player:{}".format(id_player))
            
        #for j in range(len(list_tree)):
        #    print("Nome:{}".format(list_tree[j][0].nome))
        #    print("Size set:{}".format(len(list_tree[j])))

        print("Index:{}".format(index))
        return list_tree[index]

    def dfs(self,G:Type[Graph],conjunto:Type[UFDS],u:int,visited:List[bool]):
        if visited[u]:
            return None

        visited[u] = True
        for v in G.players[u].conexoes:
            if not visited[v]:
                self.dfs(G,conjunto,v,visited)
                conjunto.unionSet(u,v)