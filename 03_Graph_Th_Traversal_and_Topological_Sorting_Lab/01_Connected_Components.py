# # Depth-First Search (DFS)
# visited[0 … n-1] = false;
# for (v = 0 … n-1) dfs(v)
# dfs (node) {
#   if not visited[node] {
#     visited[node] = true;
#     for each child c of node
#       dfs(c);
#     print node;
#   }
# }
#
# # Breadth-First Search (BFS)
# bfs(node) {
#   queue <- node
#   visited[node] = true
#   while queue not empty
#     v <- queue
#     print v
#     for each child c of v
#       if not visited[c]
#         queue <- c
#         visited[c] = true
# }
#
#  # Iterative DFS and BFS
# bfs(node) {
#   queue <- node
#   visited[node] = true
#   while queue not empty
#     v <- queue
#     print 	v
#     for each child c of v
#       if not visited[c]
#         queue <- c
#         visited[c] = true
# }
# dfs(node) {
#   stack <- node
#   visited[node] = true
#   while stack not empty
#     v <- stack
#     print v
#     for each child c of v
#       if not visited[c]
#         stack <- c
#         visited[c] = true
# }
#
# # Graph Connected Components: Algorithm
# visited[] = false;
# foreach node from graph G {
#    if (not visited[node]) {
#       dfs(node);
#       countOfComponents++;
#    }
# }
#
# dfs(node) {
#   if (not visited[node]) {
#     visited[node] = true;
#     foreach c in node.children
#       dfs(c);
#   }
# }
#
# """ ------------------------------------------------ """
# # DFS in Action
# def dfs(node, graph, visited):
#     if node in visited:
#         return
#
#     visited.add(node)
#
#     for child in graph[node]:
#         dfs(child, graph, visited)
#
#     print(node, end=' ')
#
#
# graph = {
#     1: [19, 21, 14],
#     19: [7, 12, 31, 21],
#     7: [1],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [23, 6],
#     23: [21],
#     6: [],
# }
#
# visited = set()
#
# for node in graph:
#     dfs(node, graph, visited)
#
# """ ------------------------------------------------ """
#
# # DFS #2
# def dfs(node, graph, visited):
#     if visited[node]:
#         return
#
#     visited[node] = True
#     for child in graph[node]:
#         dfs(child, graph, visited)
#
#     print(node, end=' ')
#
#
# graph = [
#     [3, 6],
#     [3, 6, 4, 2, 5],
#     [1, 4, 5],
#     [5, 0, 1],
#     [1, 2, 6],
#     [2, 1, 3],
#     [0, 1, 4],
# ]
#
# visited = [False] * len(graph)
#
# for node in range(len(graph)):
#     dfs(node, graph, visited)
#
# """ ------------------------------------------------ """
# # BFS in Action
# from collections import deque
#
#
# def bfs(node, graph, visited):
#     if node in visited:
#         return
#
#     queue = deque([node])
#     visited.add(node)
#
#     while queue:
#         current_node = queue.popleft()
#         print(current_node, end=' ')
#
#         for child in graph[current_node]:
#             if child not in visited:
#                 visited.add(child)
#                 queue.append(child)
#
#
# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [23, 6],
#     6: [],
#     23: [21],
# }
#
# visited = set()
#
# for node in graph:
#     bfs(node, graph, visited)
#
# """ ------------------------------------------------ """
#
# Find Connected Components - DFS
#
# DFS Algorithm
def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


# Read input
nodes = int(input())
graph = []

for _ in range(nodes):
    children = [int(el) for el in input().split()]
    # not needed:
    # children = [] if line == '' else [int(el) for el in line.split()]
    graph.append(children)

# print(graph)

# DFS Algorithm - creating visited array + dfs function
visited = [False] * nodes

# Find all Components
for node in range(nodes):
    if visited[node]:
        continue

    component = []
    dfs(node, graph, visited, component)
    print(f'Connected component: {" ".join([str(el) for el in component])}')
