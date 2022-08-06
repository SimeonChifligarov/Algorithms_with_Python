# # BFS Shortest Path
# bfs(G, start, end)
#     visited[start] = true
#     queue.enqueue(start)
#     while (!queue.isEmpty())
#           v = queue.dequeue()
#           if v is end
#           return v
#           for all edges from v to w in G.adjacentEdges(v) do
#              if w is not labeled as discovered then
#                  label w as discovered
#                  w.parent = v
#                  queue.enqueue(w)
#
# # Solution 1
# from collections import deque
#
# nodes = int(input())
# edges = int(input())
#
# graph = []
# [graph.append([]) for _ in range(nodes + 1)]
#
# for _ in range(edges):
#     # source -> destination => directed graph
#     source, destination = [int(el) for el in input().split()]
#     graph[source].append(destination)
#
# start_node = int(input())
# destination_node = int(input())
#
# visited = [False] * (nodes + 1)
# parent = [None] * (nodes + 1)
#
# visited[start_node] = True
# queue = deque([start_node])
#
# while queue:
#     node = queue.popleft()
#     if node == destination_node:
#         break
#     for child in graph[node]:
#         if visited[child]:
#             continue
#         visited[child] = True
#         queue.append(child)
#         parent[child] = node
#
# path = deque()
# node = destination_node
# while node is not None:
#     path.appendleft(node)
#     node = parent[node]
#
# print(f'Shortest path length is: {len(path) - 1}')
# print(*path)

# Solution 2
from collections import deque


def find_parent_by_node(graph, start_node, destination_node):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == destination_node:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def reconstruct_path(parent, destination_node):
    path = deque()
    node = destination_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    # source -> destination => directed graph
    source, destination = [int(el) for el in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

parent = find_parent_by_node(graph, start_node, destination_node)
path = reconstruct_path(parent, destination_node)

print(f'Shortest path length is: {len(path) - 1}')
print(*path)
