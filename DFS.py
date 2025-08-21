# Recursive DFS Implementation
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal (Recursive):", end=" ")
dfs_recursive(graph, 'A')
print()
# Iterative DFS Implementation
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    print("DFS Traversal (Iterative):", end=" ")
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  # reverse to maintain order
    print()

# Run Iterative DFS
dfs_iterative(graph, 'A')
