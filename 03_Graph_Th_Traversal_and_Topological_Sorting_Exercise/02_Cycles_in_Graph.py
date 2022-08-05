class AcyclicException(Exception):
    pass


def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise AcyclicException

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break

    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

# print(graph)

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except AcyclicException:
    print('Acyclic: No')
