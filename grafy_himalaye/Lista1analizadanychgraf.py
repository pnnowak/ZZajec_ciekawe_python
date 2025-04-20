import igraph as ig
import pandas as pd
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


himal = pd.read_csv("himalgotowe.csv", encoding='utf-8')

himal_do_obliczeńdlugosc = himal.drop_duplicates(subset=["FNAME", "LNAME"])

ilosc_wierzcholkow = len(himal_do_obliczeńdlugosc)
# print(ilosc_wierzcholkow)
himal_unikalne_wyprawy = himal.drop_duplicates(subset=["Numer_wyprawy"])

# print(himal_unikalne_wyprawy)

lista_ilosci_dupli = []
edges = []

for wycieczka, grupa in himal.groupby("Numer_wyprawy"):
    uczestnicy = grupa[["FNAME", "LNAME"]].drop_duplicates().values.tolist()

    duplikaty = grupa[["FNAME", "LNAME"]].duplicated(keep='first')
    ile_duplikatow = duplikaty.sum()
    lista_ilosci_dupli.append(ile_duplikatow)

    for para in combinations(uczestnicy, 2):
        edges.append(para)

print(sum(lista_ilosci_dupli))
print(edges[:5])

edges_str = [(f"{a[0]} {a[1]}", f"{b[0]} {b[1]}") for a, b in edges]

g = ig.Graph()
g.add_vertices(list({v for edge in edges_str for v in edge}))
g.add_edges(edges_str)

g.write_gml("himalaisci.gml")

# yo = g.is_connected()
# print("yo:", yo)
#
# components = g.components()
# print(f"Składowe spójne: {components}")
#
# subg = g.induced_subgraph(g.vs[0:10000])
# GN = ig.Graph.to_networkx(subg)
# pos = nx.spring_layout(GN, seed=42)
#
# degree_dict = dict(GN.degree())
# colors = [degree_dict[n] for n in GN.nodes()]
#
# nx.draw(GN,pos, node_color=colors, node_size=500,cmap=plt.cm.viridis,edge_color="black",linewidths=2)
# plt.show()
#
# print(f"Rząd (liczba wierzchołków): {g.vcount()}")
# print(f"Rozmiar (liczba krawędzi): {g.ecount()}")
# print("Graf skierowany" if g.is_directed() else "Graf nieskierowany")
# g.vs["degree"] = g.degree()
# g.vs["closeness"] = g.closeness()
#
# maly_graf = g.induced_subgraph(g.vs.select(_degree_gt=1)[:30000])
# maly_graf.vs["betweenness"] = maly_graf.betweenness()
# maly_graf.es["betweenness"] = maly_graf.edge_betweenness()
#
# for i,miary in enumerate(["degree", "closeness"]):
#     najw_wierzcholkibet = sorted(g.vs, key=lambda v: v[miary], reverse=True)
#     print(f"Top wierzchołki wg {miary}]:")
#     for v in najw_wierzcholkibet[:3]:
#         print(f"{v['name']} ({miary}: {v[miary]:.3f})")
#     print("\n")
#
# najw_wierzcholkibet = sorted(maly_graf.vs, key=lambda v: v["betweenness"], reverse=True)
# print(f"Top wierzchołki wg beetweeness]")
# for v in najw_wierzcholkibet[:3]:
#     print(f"{v['name']}: {v['betweenness']:.3f})")
# print("\n")
#
# najw_wierzcholkied = sorted(maly_graf.es, key=lambda v: v["betweenness"], reverse=True)
# print(f"Top wierzchołki wg betweenness edges]:")
# for v in najw_wierzcholkied[:3]:
#     print(f"Krawędź {maly_graf.vs[v.source]['name']}-{maly_graf.vs[v.target]['name']} (Betweenness: {v['betweenness']:.3f})")
# print("\n")
#
# bardzo_maly_graf = g.induced_subgraph(g.vs.select(_degree_gt=2)[:3000])
# bardzo_maly_grafnx = ig.Graph.to_networkx(bardzo_maly_graf)
#
# M = nx.incidence_matrix(bardzo_maly_grafnx, oriented=False)
# M_array = M.toarray()
# print(M_array[0:100])
# # adj_matrix = subg.get_adjacency()
#
# adj_matrix = nx.adjacency_matrix(bardzo_maly_grafnx)
# adj_matrix_num = adj_matrix.toarray()
# print("Macierz sąsiedztwa:", adj_matrix_num[0:100])
#
# plt.imshow(M_array, cmap="viridis", vmin=0, vmax=1)
# plt.title("Macierz incydencji – mapa kolorów")
# plt.colorbar(label="Połączenie")
# plt.show()
#
# plt.imshow(adj_matrix_num, cmap="viridis", vmin=0, vmax=1)
# plt.title("Macierz sąsiedztwa – mapa kolorów")
# plt.colorbar(label="Połączenie")
# plt.show()
#
# # Uwaga, Kosztowne obliczenia! Dopiero od 3 listy obliczenia tylko na bardzo małym podgrafie.
#
# # Top wierzchołki wg degree]:
# # Pasang Sherpa (degree: 4246.000)
# # Jangbu Sherpa (degree: 3623.000)
# # Lhakpa Nuru Sherpa (degree: 3164.000)
#
# # Top wierzchołki wg closeness]:
# # Bernard Christian D'Hoine (closeness: 1.000)
# # Frank Yates (closeness: 1.000)
# # Rod Turner (closeness: 1.000)
#
# # Oznacza to, że byli prawdopodobnie ze wsyzstkim sherpami w grafie n wyprawach, mimo, że byli na mniejszej liczbie
# # niż sami sherpowie prawdopodobnie sherpowie mają osobne grupy i rzadko się przecinają zwłaszcza szefowie z szefami
#
# # Top wierzchołki wg betweenness]:
# # Jangbu Sherpa (betweenness: 65405489.976)
# # Pasang Sherpa (betweenness: 64712060.629)
# # Lhakpa Nuru Sherpa (betweenness: 42385337.811)
#
# # Krawędź Pasang Sherpa-Reinhold Messner (Betweenness: 418880.111)
# # Krawędź Pemba Lama Sherpa-Mingma Sherpa (Betweenness: 374643.850)
# # Krawędź Ryszard Jan Pawlowski-Pasang Sherpa (Betweenness: 368574.203)
# #beetweness cen
#
#
