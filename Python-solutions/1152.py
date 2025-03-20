# Estradas Escuras

# 1. Definir o Grafo

class Graph:
  def __init__(self, V):
    self.V = V
    self.E = 0
    self.edges = []
    self.cost = 0
    
  def add_edge(self, u, v, weight):
    self.edges.append((u, v, weight))
    self.E += 1
    self.cost += weight

# 2. Estrutura Union-Find 

class UnionFind:
  def __init__(self, V):
    self.V = V
    self.parent = list(range(V))
    self.rank = [1] * V
    
  def find(self, u):
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]
  
  def union(self, v, w):
    rootV = self.find(v)
    rootW = self.find(w)
    
    if rootV != rootW:
      if self.rank[rootV] > self.rank[rootW]:
        self.parent[rootW] = rootV
      elif self.rank[rootV] < self.rank[rootW]:
        self.parent[rootV] = rootW
      else:
        self.parent[rootW] = rootV
        self.rank[rootV] += 1
    

# 3. Kruskal

def Kruskal(G):
  UF = UnionFind(G.V)
  MST = []
  MSTCost = 0
  
  G.edges.sort(key = lambda x: x[-1])
  
  for edge in G.edges:
    if UF.find(edge[0]) != UF.find(edge[1]):
      UF.union(edge[0], edge[1])
      MST.append(edge)
      MSTCost += edge[-1]
  
  return MSTCost

# Main

def main():
  while True:
    m, n = map(int, input().split()) # m: vertexes number; n: edges number
    if m == n == 0:
      break
    
    G = Graph(m)
    
    for _ in range(n):
      x, y, z = map(int, input().split()) # x, y: edge x-y; z: edge weight
      G.add_edge(x, y, z)
      
    MSTCost = Kruskal(G)
    
    print(G.cost - MSTCost)
    
    
if __name__ == '__main__':
  main()