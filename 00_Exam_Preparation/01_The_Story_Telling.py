from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)

    # print(node)
    # result.append(node)
    result.appendleft(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break

    node, children_str = [el.strip() for el in line.split('->')]
    children = children_str.split()
    graph[node] = children
    # args = [el.strip() for el in line.split('->')]
    # node = args[0]
    # if len(args) == 1:
    #     graph[node] = []
    # else:
    #     graph[node] = args[1].split()

# print(graph)

visited = set()

# result = []
result = deque()
for node in graph:
    dfs(node, graph, visited, result)

# print(*result[::-1])
print(*result)
