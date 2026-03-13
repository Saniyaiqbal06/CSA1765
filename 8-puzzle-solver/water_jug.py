from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    """
    Solves the water jug problem and returns path of states.
    """
    # Queue stores (jug1, jug2, path_of_states)
    queue = deque([(0, 0, [(0, 0)])])
    visited = set([(0, 0)])
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        # Check if we reached the target
        if jug1 == target or jug2 == target:
            return path
        
        # Try all possible moves
        moves = []
        
        # Fill jug 1
        if jug1 < jug1_capacity:
            moves.append((jug1_capacity, jug2))
        
        # Fill jug 2
        if jug2 < jug2_capacity:
            moves.append((jug1, jug2_capacity))
        
        # Empty jug 1
        if jug1 > 0:
            moves.append((0, jug2))
        
        # Empty jug 2
        if jug2 > 0:
            moves.append((jug1, 0))
        
        # Pour jug 1 to jug 2
        if jug1 > 0 and jug2 < jug2_capacity:
            pour = min(jug1, jug2_capacity - jug2)
            moves.append((jug1 - pour, jug2 + pour))
        
        # Pour jug 2 to jug 1
        if jug2 > 0 and jug1 < jug1_capacity:
            pour = min(jug2, jug1_capacity - jug1)
            moves.append((jug1 + pour, jug2 - pour))
        
        # Add unvisited moves to queue
        for new_jug1, new_jug2 in moves:
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                new_path = path + [(new_jug1, new_jug2)]
                queue.append((new_jug1, new_jug2, new_path))
    
    return None

# Test the function
jug1, jug2, target = 4, 3, 2
print(f"Water Jug Problem: {jug1}L, {jug2}L, Target={target}L")
print("=" * 50)

path = water_jug_problem(jug1, jug2, target)

if path:
    print("\nPath of states:")
    for i, state in enumerate(path):
        jug1_val, jug2_val = state
        arrow = "→" if i < len(path)-1 else "  "
        if i == 0:
            print(f"  Start: ({jug1_val}, {jug2_val})")
        elif i == len(path)-1:
            print(f"  Goal:  ({jug1_val}, {jug2_val})")
        else:
            print(f"  Step {i}: ({jug1_val}, {jug2_val})")
    
    print(f"\nTotal steps: {len(path)-1}")
    
    # Show as a sequence
    print("\nSequence:", end=" ")
    for i, state in enumerate(path):
        if i < len(path)-1:
            print(f"{state} →", end=" ")
        else:
            print(state)
else:
    print("No solution found!")