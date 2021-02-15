import networkx as nx
import numpy as np

if __name__ == '__main__':
	test1 = nx.cycle_graph(70)
	test2 = nx.path_graph(70)
	nx.write_gml(test1, "test1.gml")
	nx.write_gml(test2, "test2.gml")