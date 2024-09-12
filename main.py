import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


#bfs layout, only a couple of lines

#python ./graph.py --input graph_file.gml --create_random_graph 
#--nodes n --constant c --plot --BFS a --output out_graph_file.gml

def create_random_graph(nodes, constant):
    probability = (constant * np.log(nodes)) / nodes
    graph = nx.erdos_renyi_graph(nodes, probability)
    return graph

def read_graph(filename): 
    file = nx.read_gml(filename)
    return file

def write_graph(graph, file): 
    nx.write_gml(graph, file)   
    return 0

def main():
    
    return 0