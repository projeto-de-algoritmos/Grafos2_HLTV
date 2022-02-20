class UFDS:
    def __init__(self,N) -> None:
        self.size = N
        self.parents = [x for x in range(N)]
        self.rank = [0] * N
    
    def findSet(self,i:int) -> int:
        if self.parents[i] == i:
            return i
        self.parents[i] = self.findSet(self.parents[i])
        return self.parents[i]

    def isSameSet(self,i:int,j:int) -> bool:
        x = self.findSet(i)
        y = self.findSet(j)
        return x == y

    def unionSet(self,i:int,j:int) -> None:
        if self.isSameSet(i,j):
            return None
        x = self.findSet(i)
        y = self.findSet(j)

        if self.rank[x] > self.rank[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1