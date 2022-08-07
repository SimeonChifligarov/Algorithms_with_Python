# from collections import deque
#
# nodes = int(input())
# pairs = int(input())
#
# graph = []
# [graph.append([]) for _ in range(nodes + 1)]
#
# for _ in range(nodes):
#     node_str, children_str = input().split(':')
#     node = int(node_str)
#     children = [int(el) for el in children_str.split()]
#     # children = [int(el) for el in children_str.split()] if children_str else []
#     graph[node] = children
#
# # print(graph)
#
# for _ in range(pairs):
#     source, destination = [int(el) for el in input().split('-')]
#
#     queue = deque([source])
#     visited = [False] * len(graph)
#     visited[source] = True
#
#     parent = [None] * len(graph)
#
#     while queue:
#         node = queue.popleft()
#         if node == destination:
#             break
#         for child in graph[node]:
#             if visited[child]:
#                 continue
#             queue.append(child)
#             visited[child] = True
#             parent[child] = node
#
#     path = deque()
#     node = destination
#     while node is not None:
#         path.appendleft(node)
#         node = parent[node]
#
#     # print(*path)
#
#     print(f'{{{source}, {destination}}} -> {len(path) - 1 if not (len(path) - 1) == 0 else -1}')
#
#     # # Solution 2
#     # # line 37
#     # if parent[destination] is None:
#     #     print(f'{{{source}, {destination}}} -> -1')
#     #     continue
#     #
#     # node = destination
#     # size = 0
#     # while node is not None:
#     #     node = parent[node]
#     #     size += 1
#     #
#     # print(f'{{{source}, {destination}}} -> {size - 1}')

# Solution 3
from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    # visited = [False] * len(graph)
    # visited[source] = True
    visited = {source}

    # parent = [None] * len(graph)
    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            #     if visited[child]:
            #         continue
            if child in visited:
                continue
            queue.append(child)
            # visited[child] = True
            visited.add(child)
            parent[child] = node

    return parent


def find_path(parent, destination):
    path = deque()
    node = destination
    # while node is not None:
    while node in parent:
        path.appendleft(node)
        node = parent[node]

    return path


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(el) for el in children_str.split()]
    # children = [int(el) for el in children_str.split()] if children_str else []
    graph[node] = children

# print(graph)


for _ in range(pairs):
    source, destination = [int(el) for el in input().split('-')]

    parent = find_shortest_path(graph, source, destination)
    current_path = find_path(parent, destination)

    # print(*path)

    # print(f'{{{source}, {destination}}} -> {len(current_path) - 1 if not (len(current_path) - 1) == 0 else -1}')

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    print(f'{{{source}, {destination}}} -> {len(current_path) - 1 if not (len(current_path) - 1) == 0 else -1}')
