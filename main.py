import matplotlib.pyplot as plt # required by lab reqs, used for displaying graph
import networkx as nx # required by lab reqs, used for plotting, saving, reading graphs, and include erdos theorem function
import numpy as np # used for log function
import argparse as ap # used to handle arguments when running program

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
    path = breadth_first_search(graph, initial_node)
    nx.draw(graph, path) # networkx function for creating graph w/ BFS path shown
    plt.show() # displays graph with function from matplotlib
    return 0

def breadth_first_search(graph, initial_node): # determines path using bfs algorithm
    bfs_path = nx.bfs_edges(graph, initial_node) # goes from node to node through edges using bfs
    return bfs_path

# we need console command in this format
# python ./graph.py --input graph_file.gml --create_random_graph 
# --nodes n --constant c --plot --BFS a --output out_graph_file.gml
# done through arg parse, used in previous classes

def main(): # handles arguments required to run program, argparse ensure handling for arguments
    parser = ap.ArgumentParser(description='creates graph based on erdos-renyl theorum + BFS algorith')

    parser.add_argument('--input', type=str, help='filename of graph, ex. "out_graph_file.gml"')
    parser.add_argument('--create_random_graph', action='store_true')
    parser.add_argument('--nodes', type=int, help='possitive integer amount of nodes for your graph')
    parser.add_argument('--constant', type=float)
    parser.add_argument('--BFS', type=int, help='number of node you want to start BFS from')
    parser.add_argument('--plot', action='store_true')
    parser.add_argument('--output', type=str, help='name of file for new graph, ex. "out_graph_file.gml"')

    args = parser.parse_args()

    # checks what arguments are met when running file
    if args.create_random_graph:
        graph = create_random_graph(args.nodes, args.constant)
    elif args.input:
        graph = read_graph(args.input)

    if args.BFS:
        breadth_first_search(graph, args.BFS)

    if args.plot:
        plot_graph(graph, args.BFS)

    if args.output:
        write_graph(graph, args.output)
    
if __name__ == "__main__":
    main()