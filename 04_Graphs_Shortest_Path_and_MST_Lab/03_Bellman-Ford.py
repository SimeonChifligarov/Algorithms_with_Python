# # Bellman-Ford Algorithm
# for v in G
#    d[v] = infinity
#    prev[v] = null
# d[source] = 0
# for vertex in G.vertices – 1
#   for edge in edges
#     if (d[edge.from] != infinity and
#         d[edge.from] + edge.weight < d[edge.to])
#       update d[edge.to]
# // Run the algorithm second time if you can
# // update any distance there is a negative cycle
#
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(el) for el in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True

    if not updated:
        break

# print(distance)

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path)
    print(distance[target])
