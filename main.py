import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


#bfs layout, only a couple of lines

#python ./graph.py --input graph_file.gml --create_random_graph 
#--nodes n --constant c --plot --BFS a --output out_graph_file.gml

def read_graph(filename): # reads graph from file if there is one
    file = nx.read_gml(filename) # networkx function for reading files
    return file

def write_graph(graph, file): # saves graph to file
    nx.write_gml(graph, file) # networkx function for writing graph into file
    return 0

def create_random_graph(nodes, constant): # creates random graph using erdos renyl theorem
    probability = (constant * np.log(nodes)) / nodes # probability for erdos renyl graph found from class notes
    graph = nx.erdos_renyi_graph(nodes, probability) # netowrkx has function for erdos renyl graph
    return graph

def plot_graph(graph, initial_node): # plots graph
    path = BFS(graph,initial_node)
    nx.draw(graph, path) # networkx function for creating graph w/ BFS path shown
    plt.show() # displays graph with function from matplotlib
    return 0

def BFS(graph, initial_node): # determines path using bfs algorithm
    bfs_path = nx.bfs_edges(graph, initial_node)
    return bfs_path

def main():
    
    return 0