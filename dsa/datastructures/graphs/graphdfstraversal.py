class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append(neighbor)

#Usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

print("DFS Traversal using Stack:")
dfs_stack(g.graph, 'A')
