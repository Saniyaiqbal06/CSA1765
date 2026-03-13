import heapq

def astar(start, goal, neighbors_fn, heuristic_fn):
    """
    Find the shortest path from start to goal using A* algorithm.
    
    Arguments:
    start: the starting node
    goal: the goal node
    neighbors_fn: a function that takes a node and returns its neighbors
    heuristic_fn: a function that takes a node and returns the estimated
                  distance to the goal node
    
    Returns:
    A tuple containing the path from start to goal and its cost
    """
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            break
            
        for neighbor in neighbors_fn(current):
            # Assuming uniform cost of 1 per step (change if needed)
            new_cost = cost_so_far[current] + 1
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    # Check if goal was reached
    if goal not in came_from:
        return None, float('inf')  # No path found
    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()  # Reverse to get path from start to goal
    
    return path, cost_so_far[goal]

# Example 1: Grid-based pathfinding
def grid_neighbors(node):
    """Example neighbors function for a 4-directional grid."""
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def grid_heuristic(node, goal):
    """Manhattan distance heuristic for grid."""
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Example 2: Graph-based pathfinding
def graph_neighbors(node):
    """Example neighbors function for a graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    return graph.get(node, [])

def graph_heuristic(node, goal):
    """Simple heuristic for graph (0 = uninformed, can use domain knowledge)."""
    # This is a simple heuristic - in practice, you might use straight-line distance
    # or other domain-specific estimates
    heuristic = {
        ('A', 'F'): 2,  # Estimated distance from A to F
        ('B', 'F'): 1,
        ('C', 'F'): 1,
        ('D', 'F'): 2,
        ('E', 'F'): 1,
        ('F', 'F'): 0
    }
    return heuristic.get((node, goal), 0)

if __name__ == "__main__":
    print("=" * 50)
    print("EXAMPLE 1: Grid Pathfinding")
    print("=" * 50)
    
    start = (0, 0)
    goal = (3, 4)
    
    path, cost = astar(start, goal, grid_neighbors, grid_heuristic)
    
    if path:
        print(f"Path from {start} to {goal}: {path}")
        print(f"Path cost: {cost}")
        
        # Visualize the path (small grid)
        print("\nPath visualization:")
        grid = [['.' for _ in range(5)] for _ in range(5)]
        for x, y in path:
            if 0 <= x < 5 and 0 <= y < 5:
                grid[x][y] = '*'
        grid[start[0]][start[1]] = 'S'
        grid[goal[0]][goal[1]] = 'G'
        
        for row in grid:
            print(' '.join(row))
    else:
        print(f"No path found from {start} to {goal}")
    
    print("\n" + "=" * 50)
    print("EXAMPLE 2: Graph Pathfinding")
    print("=" * 50)
    
    start_graph = 'A'
    goal_graph = 'F'
    
    path_graph, cost_graph = astar(start_graph, goal_graph, 
                                   graph_neighbors, graph_heuristic)
    
    if path_graph:
        print(f"Path from {start_graph} to {goal_graph}: {' -> '.join(path_graph)}")
        print(f"Path cost: {cost_graph}")
    else:
        print(f"No path found from {start_graph} to {goal_graph}")
    
    print("\n" + "=" * 50)
    print("EXAMPLE 3: Unreachable Goal")
    print("=" * 50)
    
    # Create a graph with unreachable node
    def disconnected_neighbors(node):
        graph = {
            'A': ['B'],
            'B': ['A'],
            'C': []  # C is isolated
        }
        return graph.get(node, [])
    
    path_unreachable, cost_unreachable = astar('A', 'C', 
                                               disconnected_neighbors, 
                                               lambda n, g: 0)
    
    if path_unreachable:
        print(f"Path found: {path_unreachable}")
    else:
        print(f"No path from A to C (correctly detected)")