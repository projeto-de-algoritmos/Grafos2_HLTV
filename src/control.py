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

    @staticmethod
    def mst(G:Type[Graph]):
        list_tree = []

        return list_tree