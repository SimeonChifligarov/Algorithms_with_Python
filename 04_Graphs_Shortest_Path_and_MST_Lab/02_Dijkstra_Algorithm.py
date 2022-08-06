# # Steps in Dijkstra's algorithm:
# Initially calculate all direct distances d[] from S
# Enqueue that start node S
# While (queue not empty)
#   Dequeue the nearest vertex B
#   Enqueue all unvisited child nodes of B
#   For each edge {B → A}, improve d[A] through B:
#     d[S → A] = min(d[S → A], d[S → B] + weight[B → A])
#
# # Dijkstra's Algorithm – Pseudo Code
# d[0…n-1] = INFINITY; d[startNode] = 0
# Q = priority queue holding nodes ordered by distance d[]
# startNode add to Q
# while (Q is not empty)
#   minNode = dequeue the smallest node from Q
#   if (d[minNode] == INFINITY) break;
#   foreach (child c of minNode)
#     if (c is unvisited) c add to Q
#     newDistance = d[minNode] + distance {minNode → c}
#     if (newDistance < d[c])
#       d[c] = newDistance;
#       reorder Q;
# }
#
from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f'{self.source} -> {self.destination}, weight: {self.weight}'


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(el) for el in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

# print(graph)

start = int(input())
target = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

# print(distance)

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(distance[target])
    print(*path)
