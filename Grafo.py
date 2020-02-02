import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    source = []
    target = []
    weight = []
    vertex = []

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

