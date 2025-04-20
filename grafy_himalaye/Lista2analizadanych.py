from Lista1analizadanychgraf import g
import matplotlib.pyplot as plt
import networkx as nx


class GrafLista2:
    def __init__(self, graf):
        self.g = graf
        self.g.vs["degree"] = self.g.degree()
        self.g.vs["closeness"] = self.g.closeness()

    def stopnie(self):
        """Rozkład stopni wierzchołków"""
        degrees = self.g.degree()
        return degrees

    def bliskosc(self):
        """Rozkład stopni wierzchołków"""
        bliskosc = self.g.closeness()
        return bliskosc

    def gęstosc(self):
        """Gęstość sieci"""
        return self.g.density()

    def średnica(self):
        """Średnica sieci"""
        return self.g.diameter(directed=False)

    def średnia_długość_ścieżki(self):
        """Średnia długość ścieżki"""
        return self.g.average_path_length(directed=False)

    def najkrótsza_ścieżka(self, start, end):
        """Najkrótsza ścieżka pomiędzy wierzchołkami"""
        return self.g.get_shortest_paths(start, to=end, output="vpath")

    def miary_centralnościnodes(self):
        """Obliczanie miar centralności"""
        self.g.vs["betweenness"] = self.g.betweenness()
        self.g.vs["pagerank"] = self.g.pagerank()
        return self.g.vs["betweenness"], self.g.vs["pagerank"]

    def miary_centralnościedges(self):
        self.g.vs["betweennessed"] = self.g.edge_betweenness()
        return self.g.vs["betweennessed"]

    def składowe_spójne(self):
        """Składowe spójne grafu"""
        return self.g.components()

    def k_spójność(self, k):
        """K-spójność grafu"""
        return self.g.k_core(k)

    def huby_i_mosty(self):
        """Huby i mosty w grafie"""
        hubs = [v.index for v in self.g.vs if v.degree() > 5]
        bridges = self.g.bridges()
        return hubs, bridges

    def przeguby(self):
        """Przeguby w grafie"""
        articulation_points = self.g.articulation_points()
        return articulation_points

    def rozkład_długości_ścieżek(self):
        lengths = []
        dist_matrix = self.g.distances()

        for row in dist_matrix:
            lengths.extend([length for length in row if length != float('inf')])

        return lengths

    def klik(self, min_size=3):
        """Wyszukiwanie klik w grafie"""
        cliques = self.g.cliques(min=min_size)
        return cliques

    def klika_n_tego_rzedu(self, cliques):
        """Wyszukiwanie klik n-tego rzędu"""
        return [clique for clique in cliques if len(clique) >= 5]

    def klika_maksymalna(self, cliques):
        """Wyszukiwanie kliki maksymalnej"""
        return max(cliques, key=len)  # Największa klika

    def near_klike(self, cliques, tolerance):
        """Wyszukiwanie n-podkliki (near clique)"""
        near_cliques = []

        for clique in cliques:
            subgraph = self.g.subgraph(clique)
            missing_edges = 0
            for i in range(len(clique)):
                for j in range(i + 1, len(clique)):
                    if not self.g.are_adjacent(clique[i], clique[j]):
                        missing_edges += 1
            if 0 < missing_edges <= tolerance:
                near_cliques.append(clique)

        return near_cliques


subgraph = g.subgraph(g.components().subgraphs()[0].vs)
# print(f"Podgraf składowej spójnej: {subgraph}")
maly_graf = subgraph.induced_subgraph(subgraph.vs.select(_degree_gt=3))
bardzo_maly_graf = subgraph.induced_subgraph(subgraph.vs[:10000])
print("bardzomaly")

maly_graflista2 = GrafLista2(maly_graf)
print("maly")
bardzo_maly_graflista2 = GrafLista2(bardzo_maly_graf)

#pomocne do rysowania wykresów pożniej
g_networkx = nx.Graph()
g_networkx.add_edges_from(bardzo_maly_graf.get_edgelist())
g_networkx = nx.Graph()
g_networkx.add_edges_from(maly_graf.get_edgelist())

#bardzo_bardzomalygraf gdy pozostale podgrafy byly za duze
bardzo_bardz0_maly = bardzo_maly_graf.induced_subgraph(bardzo_maly_graf.vs[:3000])
g_networkx2 = nx.Graph()
g_networkx2.add_edges_from(bardzo_bardz0_maly.get_edgelist())
bardzo_bardz0_maly_graflista2 = GrafLista2(bardzo_bardz0_maly)

#1
#rozklad stopni wierzchołków
degrees = maly_graflista2.stopnie()
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1))
plt.xlabel("Stopień wierzchołka")
plt.ylabel("Liczba wierzchołków")
plt.title("Rozkład stopni wierzchołków")
plt.show()

# kolejne wartosci do policzenia
print("Gęstość sieci:", maly_graflista2.gęstosc())
print("Średnica sieci:", maly_graflista2.średnica())
print("Średnia długość ścieżki:", maly_graflista2.średnia_długość_ścieżki())

start, end = "Pasang Sherpa", "Lhakpa Nuru Sherpa"
print(f"Najkrótsza ścieżka między wierzchołkami {start} i {end}:", maly_graflista2.najkrótsza_ścieżka(start, end))

print("Miary centralności nodes:", bardzo_maly_graflista2.miary_centralnościnodes())
print("Miary centralności edges:", bardzo_maly_graflista2.miary_centralnościedges())


# funkcje pomagające w rysowania policzonych wartości
def visualize_components(g, components):
    # Kolorowanie składowych - lista kolorów, używając prostych nazw kolorów
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'brown', 'gray']
    pos = nx.spring_layout(g)  # Układ siłowy
    plt.figure(figsize=(10, 8))

    # Tworzymy listę kolorów dla każdego wierzchołka
    node_colors = []
    for node in g.nodes:
        for i, component in enumerate(components):
            if node in component:
                node_colors.append(colors[i % len(colors)])  # Cykl przez kolory, jeśli jest ich więcej
                break

    # Rysowanie grafu
    nx.draw(g, pos, node_color=node_colors, with_labels=True, node_size=500, font_size=10)
    plt.title("Wizualizacja Składowych Spójnych")
    plt.show()

def visualize_hubs_and_bridges(g, hubs, bridges):
    pos = nx.spring_layout(g)
    node_colors = ['red' if node in hubs else 'lightblue' for node in g.nodes]
    edge_colors = ['green' if (u, v) in bridges or (v, u) in bridges else 'lightgray' for u, v in g.edges]

    plt.figure(figsize=(10, 8))
    nx.draw(g, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=500, font_size=10)
    plt.title("Wizualizacja Hubów i Mostów")
    plt.show()

def visualize_kcore(k_core):
    pos = nx.spring_layout(k_core)
    plt.figure(figsize=(10, 8))

    nx.draw(k_core, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
    plt.title(f"Wizualizacja K-core (k={2})")
    plt.show()

def visualize_articulation_points(g, articulation_points):
    pos = nx.spring_layout(g)
    node_colors = ['red' if node in articulation_points else 'lightblue' for node in g.nodes]

    plt.figure(figsize=(10, 8))
    nx.draw(g, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
    plt.title("Wizualizacja Przegubów (Articulation Points)")
    plt.show()

def visualize_cliques(g, cliques, min_size=3):
    filtered_cliques = [clique for clique in cliques if len(clique) >= min_size]
    pos = nx.spring_layout(g)
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'brown', 'gray']
    plt.figure(figsize=(10, 8))

    for i, clique in enumerate(cliques):
        nx.draw(g.subgraph(clique), pos, with_labels=True, node_color=colors[i % len(colors)], node_size=500, font_size=10)

    plt.title("Wizualizacja Klik")
    plt.show()


# Wizualizacja składowych spójnych
components = bardzo_bardz0_maly_graflista2.składowe_spójne()
visualize_components(g_networkx2, components)

# # Wizualizacja hubów i mostów
hubs, bridges = bardzo_maly_graflista2.huby_i_mosty()
visualize_hubs_and_bridges(g_networkx, hubs, bridges)

# Wizualizacja k-core
k_coreg = bardzo_bardz0_maly_graflista2.k_spójność(2)
k_core = nx.Graph()
k_core.add_edges_from(k_coreg.get_edgelist())
visualize_kcore(k_core)

# # Wizualizowanie przegubów
przeguby = bardzo_maly_graflista2.przeguby()
visualize_articulation_points(g_networkx, przeguby)

# Wizualizowanie klik
kliki = bardzo_bardz0_maly_graflista2.klik()
visualize_cliques(g_networkx2, kliki)

#   rozklad dlugosci sciezek
lengths = bardzo_bardz0_maly_graflista2.rozkład_długości_ścieżek()
plt.hist(lengths, bins=30, color='green', edgecolor='black')
plt.title("Rozkład długości ścieżek")
plt.xlabel("Długość ścieżki")
plt.ylabel("Liczba ścieżek")
plt.show()

# Teraz rysuję histogramy miar centralnosci,
# aby łatwiej było zauważyć z jakim grafem mamy doczyniena
# i dowiedzieć się więcej o wierzchołkach i krawiędzich.

beetweeness, page = bardzo_maly_graflista2.miary_centralnościnodes()
beetweenesenges = bardzo_maly_graflista2.miary_centralnościedges()

plt.hist(beetweeness, bins=40, color='blue')
plt.show()

plt.hist(beetweenesenges, bins=40, color='red')
plt.show()

bliskosc = bardzo_maly_graflista2.bliskosc()
plt.hist(bliskosc, bins=40, color='green')
plt.show()

degree = bardzo_maly_graflista2.stopnie()
plt.hist(degree, bins=40, color='purple')
plt.show()

plt.hist(page, bins=40, color='purple')
plt.show()
# Jest to oczywiście graf bezskalowy

# Dalej eksprolujemy graf,
# licząc kliki, klitka to graf pełny
n_order_cliques = bardzo_bardz0_maly_graflista2.klika_n_tego_rzedu(kliki)
print("Klika n-tego rzędu:", len(n_order_cliques), n_order_cliques)

max_clique = bardzo_bardz0_maly_graflista2.klika_maksymalna(kliki)
print("Klika maksymalna:", max_clique)

near_cliques = bardzo_bardz0_maly_graflista2.near_klike(kliki, 1)
print("n-podkliki (Near Clique):",len(near_cliques), near_cliques)

# WYNIKI LICZBOWE:
# Gęstość sieci: 0.0008302133686299701
# Średnica sieci: 10
# Średnia długość ścieżki: 3.5929043423502436
# Najkrótsza ścieżka między wierzchołkami Pasang Sherpa i Lhakpa Nuru Sherpa: [[6052, 22583]]
# Klika n-tego rzędu: 503
# Klika maksymalna: (241, 542, 563, 738, 1864, 1901, 2100, 2295, 2762)
# n-podkliki (Near Clique): 0 []

#   Uwaga ten kod częściowo był wykonywany w google colab dlatego,
#   że graf ten ma 40tys krawiędzi i 600 tys wierzchołków i w zwiąsku z tym
#   bardzo długo prawie wszystko się liczy.

