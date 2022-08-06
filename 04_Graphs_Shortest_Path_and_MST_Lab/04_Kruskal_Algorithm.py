# # Kruskal's Algorithm – Pseudo Code
# # Time complexity: O(|E| * log* |E|)
# foreach v ∈ graph edges
#   parent[v] = v
# foreach edge {u, v} ordered by weight(u, v)
#   rootU = findRoot(u)
#   rootV = findRoot(v)
#   if rootU ≠ rootV
#     print edge {u, v}
#     parent[rootU] = rootV
# findRoot(node)
#   while (parent[node] ≠ node)
#     node = parent[node]
#   return node
#
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __repr__(self):
        return f'{self.first} - {self.second}'


def find_root(parent, node):
    while not node == parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(el) for el in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node + 1)]
forest = []

for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if not first_node_root == second_node_root:
        parent[first_node_root] = second_node_root
        # also possible:
        # parent[second_node_root] = first_node_root
        forest.append(edge)

[print(edge) for edge in forest]
