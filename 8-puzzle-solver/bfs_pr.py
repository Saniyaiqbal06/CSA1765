from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph (Adjacency List using numbers)
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

# Function call
bfs(graph, 0)