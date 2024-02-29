import networkx as nx  # igraph is also supported
import pseudoflow

G = nx.DiGraph()
G.add_edge(0, 1, const=1, mult=5)
G.add_edge(1, 2, const=9, mult=-3)


source = 0
sink = 2
lambda_range = [0., 2.]

breakpoints, cuts, info = pseudoflow.hpf(
    G,  # Networkx or igraph directed graph.
    source,  # Node id of the source node.
    sink,  # Node id of the sink node.
    const_cap="const",  # Edge attribute with the constant capacity.
    mult_cap="mult",  # Edge attribute with the lambda multiplier.
    lambdaRange=lambda_range,  # (lower, upper) bounds for the lambda parameter.
    roundNegativeCapacity=False  # True if negative arc capacities should be rounded to zero.
)

# breakpoints: list of upper bounds for the lambda intervals.
# cuts: A dictionary with for each node a list indicating whether
#       the node is in the source set of the minimum cut.
print(breakpoints)  # Output: [1., 2.]
print(cuts)  # Output: {0: [1, 1], 1: [0, 1], 2: [0, 0]}
#