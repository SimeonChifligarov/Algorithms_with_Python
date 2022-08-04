# # Source Removal Algorithm
# L <- empty list that will hold the sorted elements (output)
# S <- set of all nodes with no incoming edges
# while S is non-empty do
#     remove some node n from S
#     append n to L
#     for each node m with an edge e: { n through m }
#         remove edge e from the graph
#         if m has no other incoming edges then
#             insert m into S
# if graph is empty
#    return L (a topologically sorted order)
# else
#    return "Error: graph has at least one cycle"
#
# """ ------------------------------------------------ """
# # Topological Sorting: DFS Algorithm
# sortedNodes = { }   // linked list to hold the result
# visitedNodes = { }  // set of already visited nodes
# foreach node in graphNodes
#     topSortDFS(node)
# topSortDFS(node)
#     if node ∉ visitedNodes
#         visitedNodes ← node
#         for each child c of node
#             TopSortDFS(c)
#         insert node upfront in the sortedNodes
#
# # TopSort: DFS Algorithm + Cycle Detection
# sortedNodes = { }   // linked list to hold the result
# visitedNodes = { }  // set of already visited nodes
# cycleNodes = { }    // set of nodes in the current DFS cycle
# foreach node in graphNodes
#     topSortDFS(node)
# topSortDFS(node)
#     if node ϵ cycleNodes
#         return "Error: cycle detected"
#     if node ∉ visitedNodes
#         visitedNodes <- node
#         cycleNodes <- node
#         for each child c of node
#             topSortDFS(c)
#         remove node from cycleNodes
#         insert node upfront in the sortedNodes
#
# """ ------------------------------------------------ """
#
# Source Removal Topological Sorting
#
# Compute Predecessors
# def get_predecessors_count(graph):
#     result = {}
#
#     for node, children in graph.items():
#         if node not in result:
#             result[node] = 0
#         for child in children:
#             if child not in result:
#                 result[child] = 1
#             else:
#                 result[child] += 1
#
#     return result
#
#
# # Remove Independent Nodes
# def top_sort(graph, predecessors_count):
#     result = []
#
#     while predecessors_count:
#         predecessors_count = get_predecessors_count(graph)
#         node = find_node_without_predecessors(predecessors_count)
#         if node is None:
#             break
#
#         for child in graph[node]:
#             predecessors_count[child] -= 1
#
#         result.append(node)
#         predecessors_count.pop(node)
#
#     return result
#
#
# def find_node_without_predecessors(predecessors_count):
#     for node, count in predecessors_count.items():
#         if count == 0:
#             return node
#     return None
#
#
# nodes = int(input())
#
# graph = {}
#
# for _ in range(nodes):
#     line_tokens = input().split('->')
#     node = line_tokens[0].strip()
#     children = line_tokens[1].strip().split(', ') if line_tokens[1] else []
#     graph[node] = children
#
# predecessors_count = get_predecessors_count(graph)
# sorted_nodes = top_sort(graph, predecessors_count)
#
# if predecessors_count:
#     print('Invalid topological sorting')
# else:
#     print(f'Topological sorting: {", ".join(sorted_nodes)}')

# """ ------------------------------------------------ """
def find_dependencies(graph):
    result = {}

    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node

    return None


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_tokens = input().split('->')
    node = line_tokens[0].strip()
    children = line_tokens[1].strip().split(', ') if line_tokens[1] else []
    graph[node] = children

# print(graph)

dependencies_by_node = find_dependencies(graph)

# print(dependencies_by_node)

has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break

    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

# print(sorted_nodes)

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f'Topological sorting: {", ".join(sorted_nodes)}')

# """ ------------------------------------------------ """
# from collections import deque
#
#
# def dfs(node, graph, visited, cycles, sorted_nodes):
#     if node in cycles:
#         raise Exception('Cycle has been detected. Invalid topological sorting!')
#
#     if node in visited:
#         return
#
#     visited.add(node)
#     cycles.add(node)
#     for child in graph[node]:
#         dfs(child, graph, visited, cycles, sorted_nodes)
#
#     cycles.remove(node)
#     sorted_nodes.appendleft(node)
#
#
# nodes = int(input())
#
# graph = {}
#
# for _ in range(nodes):
#     line_tokens = input().split('->')
#     node = line_tokens[0].strip()
#     children = line_tokens[1].strip().split(', ') if line_tokens[1] else []
#     graph[node] = children
#
# visited = set()
# cycles = set()
# sorted_nodes = deque()
#
# for node in graph:
#     dfs(node, graph, visited, cycles, sorted_nodes)
#
# print(*sorted_nodes, sep=' ')
