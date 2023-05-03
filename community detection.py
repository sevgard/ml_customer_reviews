import numpy as np
import json
import networkx as net
# from networkx.algorithms import community
import matplotlib.pyplot as mat
import itertools as itr
from community import community_louvain as comm

# Load list of toothpastes and assign its asin values as product tags
with open ('product_titles.json', 'r') as json1:
    titles = json.load(json1)
print("Size of titles dictionary: ")
print(len(titles))

# Load product list and collect the product names
with open ('list_products.json', 'r') as json1:
    asins = json.load(json1)
print("Size of asins list: ")
print(len(asins))

# DRMABS 1 - COMMUNITY DETECTION
# Local Competitive Asymmetry Matrix converted to a graph
matrix = np.load('Z_S.npy')
print("Dimensions of the asymmetry matrix: ")
print(matrix.shape)
graph = net.DiGraph()
graph = net.from_numpy_array(matrix)
graph.edges(data = True)
net.transitivity(graph)

# Find modularity
part = comm.best_partition(graph)
mod = comm.modularity(part, graph)

# Plot, color nodes using community structure
# Add Labels of the products
values = [part.get(node) for node in graph.nodes()]
net.draw_spring(graph, cmap=mat.get_cmap('jet'), node_color = values, node_size=10)

# TODO
# Add node labels on the graph
pos = net.spring_layout(graph)
index = list(range(0, len(asins)))
# for t in titles:
#     for i in range(len(asins)):
#         if asins[i] == t[i]:
#             labels += {asins[i], t[str(i)]}
labels = dict(zip(index, asins))
print("Index list: ")
print(labels)
net.draw_networkx_labels(graph, pos, labels, font_size=10)
mat.show()

# Add weighted edges from the matrix
# Make the diagonal nan, so that loops are excluded on the graph

# The modularity value which indicates the partition quality
print("Modularity value obtained using Louvain Algorithm: ")
print(mod)

# The partition dictionary using Louvain Algorithm
print(max(part.values()))




# COMMUNITIES REPRESENTED AS GRAPHS

# Communities represented as nodes
# part_graph = comm.induced_graph(part, graph)
# print(type(graph))
# print(type(part_graph))
# print(type(part))
# net.draw_spring(part_graph, cmap=mat.get_cmap('jet'), node_color = values, node_size=100, with_labels=False)
# mat.show()


#########################################################


# GIRVAN NEWMAN

# # Community Detection with Girvan-Newman Algorithm
# comm = community.girvan_newman(graph)
# # print(tuple(sorted(c) for c in next(comm)))
# for communities in itr.chain(comm):
#     print(tuple(sorted(c) for c in communities))
#     # Calculate modularity and store in a list,
#     # Store the max modularity value,
#     # Store the index of the max modularity value
#     # Modularity = Sum(e - a^2)
#     # e = num edges with both endpoints in community k / # edge endpoints
#     # a = num of edge endpoints in community k / # edge endpoints
#     # a =
#     # numComm = len()
#     # for i in numComm
#     # e
#     # q += e - a**2
#
# # net.draw(graph)
# mat.draw()
# mat.show()


# Find the titles of asins, make sure the asin is ordered with matrix indices

# pos = net.spring_layout(graph)

# Display node labels on the graph
# net.draw_networkx_labels(graph, pos, products, font_size=10)

# # Build the graph
# G=nx.DiGraph()
# G.add_nodes_from(df.emp_name)
# G.nodes()
# G.add_node('None')
# #
# #Over here, you are manually adding 'None' but in reality
# #your nodes are the unique entries of the concatenated
# #columns, i.e. emp_name, mgr_name. You could achieve this by
# #doing something like
# #
# #G.add_nodes_from(list(set(list(D.emp_name.values) + list(D.mgr_name.values))))
# #
# # Which does exactly that, retrieves the contents of the two columns
# #concatenates them and then selects the unique names by turning the
# #combined list into a set.
#
# # Add edges
# subset = df[['mgr_name','emp_name']]
# tuples = [tuple(x) for x in subset.values]
# G.add_edges_from(tuples)
# G.number_of_edges()
#
# # Perform Graph Drawing
# # A star network  (sort of)
# nx.draw_networkx(G)
# plt.show()
# t = raw_input()
#
# # A tree network (sort of)
# nx.draw_graphviz(G, prog = 'dot')
# plt.show()
