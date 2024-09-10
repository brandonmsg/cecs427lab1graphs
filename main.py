import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

nodes = 0
constant = 0

#python ./graph.py --input graph_file.gml --create_random_graph 
#--nodes n --constant c --plot --BFS a --output out_graph_file.gml

def generateGraph(nodes, constant):
    graph = nx.graph()
    nx.generate_gml(graph, stringizer=None)

    return 0
def input(path): #path = file name?
    nx.read_gml(path)
    #n.xwrite_gml(graph,path)

    return 0
def create_random_graph():

    return 0
def BFS(): #algorithm for breath first search

    return 0
def main():
    
    return 0