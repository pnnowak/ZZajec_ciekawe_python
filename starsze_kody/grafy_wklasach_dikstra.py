import random
import numpy as np
import heapq


class Grafy:
    def __init__(self, n):
        self.n = n
        self.list = [[] for i in range(n)]
        self.edges = []

    def oddaj_krawiedz(self, u, v):
        self.list[v].append(u)
        self.list[u].append(v)
        self.edges.append((u, v))

    def losowanie(self, p):
        for i in range(self.n):
            for j in range(i+1, self.n):
                r = random.random()
                if r < p:
                    self.oddaj_krawiedz(i, j)


    def DFS(self, v, visited, com):
        visited[v] = True
        com.append(v)
        for kolega in self.list[v]:
            if not visited[kolega]:
                self.DFS(kolega, visited, com)


    def znajdż_komponenty(self, n):
        visited = [False] * self.n
        comps = []
        cn = 0
        for i in range(self.n-1):
            if not visited[i]:
                comp = []
                self.DFS(i, visited, comp)
                comps.append(comp)
                cn =+ 1
        return comps, cn

    def pokaz_componenty(self, components):
        for i, component in enumerate(components):
            print(f"Składowa spójna {i + 1}: {component}")



    def dijkstra(self, start, end):
        adj = {i: [] for i in range(self.n)}
        for srs, cel in self.edges:
            adj[srs].append(cel)
            adj[cel].append(srs)

        shortest = {i: float('inf') for i in range(self.n)}
        shortest[start] = 0
        pq = [(0, start)]  # (distance, node)
        visited = set()

        while pq:
            dist, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                new_dist = dist + 1
                if new_dist < shortest[neighbor]:
                    shortest[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        for i in range(self.n):
            if shortest[i] == float('inf'):
                shortest[i] = -1

        return shortest


n = 10
p = 0.3
g = Grafy(n)
g.losowanie(p)

components, cn = g.znajdż_komponenty(n)
g.pokaz_componenty(components)
print(cn)

#2
start, end = random.choice(range(10)), random.choice(range(10))
dlugosci = g.dijkstra(start, end)

print(f"Najkrótsza ścieżka między {start} a {end} wynosi {dlugosci[end]}")
print(dlugosci)