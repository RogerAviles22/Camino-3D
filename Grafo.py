import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    source = []
    target = []
    weight = []
    vertex = []
    distances={}

    undirected = 0

    def __init__(self, source=[], target=[], weight=[], directed=True):
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)
        self.directed = directed

        self.set_vertex()

    #Imprime los valores de nodos fuentes, nodos destino, pesos de cada arco y nos los nodos como tal (vertex)
    def print_r(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.vertex)

    #Dependiendo de los nodos fuentes y destino,
    #realiza una lista de los nodos existentes del grafo, importantes para usarlo en los algoritmos.
    def set_vertex(self):
        vertex = np.unique(self.source)
        vertex2 = np.unique(self.target)
        self.vertex = np.unique(np.concatenate([vertex, vertex2]))
        return self.vertex

    #Dado dos nodos encontrar el peso de su arco.
    def get_weight(self, n1, n2):
        return self.weight[np.logical_and(self.source == n1, self.target == n2)]

    #Exportar todos los datos de arco en una matriz
    def export(self):
        array_export = [(int(self.source[i]), int(self.target[i]), self.weight[i]) for i in range(self.source.size)]
        return array_export

    def dijkstra(self):
        nodes = list(self.graph.nodes)

        for i in nodes:  # Set first values
            dict_i = {}
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                else:
                    dict_i[j] = float("inf")
            self.distances[i] = dict_i

        for oneNode in nodes:  # Start algoritm
            Q = []
            for node in nodes: Q.append(node)

            while len(Q) != 0:
                v = 0
                min = float("inf")
                for node_q in Q:
                    if self.distances[oneNode][node_q] <= min:
                        min = self.distances[oneNode][node_q]
                        v = node_q

                Q.remove(v)

                neighbors = list(self.graph.neighbors(v))

                for neighborV in neighbors:
                    w = self.graph[v][neighborV]['weight']
                    alt = self.distances[oneNode][v] + w
                    if alt < self.distances[oneNode][neighborV]:
                        self.distances[oneNode][neighborV] = alt

        return self.distances

    def create_network(self, source, target, weight):

        self.graph = nx.DiGraph()
        count = len(source)

        edges = []

        for i in range(0, count):
            edges.append((source[i], target[i], weight[i]))

        self.graph.add_weighted_edges_from(edges)
        return self.graph

    def floyd_warshall(self):
        nodes = list(self.graph.nodes)

        for i in nodes:
            dict_i = {}
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                    continue
                try:
                    dict_i[j] = self.graph[i][j]['weight']
                except:
                    dict_i[j] = float("inf")

            self.distances[i] = dict_i

        for i in nodes:
            for j in nodes:
                for k in nodes:
                    ij = self.distances[i][j]
                    ik = self.distances[i][k]
                    kj = self.distances[k][j]

                    if ij > ik + kj:
                        self.distances[i][j] = ik + kj

        return self.distances

    def print_distances(self):
        printt = ""
        for i in self.distances:
            printt = printt + str(i) + ": \t"
            for j in self.distances[i]:
                printt = printt + str(self.distances[i][j]) + "\t"
            printt = printt + "\n"
        print("\n------------------------------------")
        print(printt)
        return

    def draw(self, with_weight=True):
        Gr = nx.DiGraph()
        Gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(Gr)
        list_edges = list(Gr.edges())
        last = ()

        # if self.last_vertex_modified.size > 0:
        #    last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]))
        #    list_edges.remove(last)

        nx.draw(Gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in Gr.edges(data=True)])
            nx.draw_networkx_edge_labels(Gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        if len(last) > 0:
            nx.draw_networkx_edges(Gr, pos=pos, edgelist=[last], width=2.0, edge_color='b')

        plt.axis('off')
        plt.show()