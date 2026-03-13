from queue import PriorityQueue

# Goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            if tile != 0:
                x, y = (tile - 1) // 3, (tile - 1) % 3
                distance += abs(x - i) + abs(y - j)
    return distance

# Generate possible moves
def successors(state):
    successors = []
    i = state.index(0)
    
    # Move left
    if i % 3 != 0:
        new_state = list(state)
        new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
        successors.append(tuple(new_state))
    
    # Move right
    if i % 3 != 2:
        new_state = list(state)
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        successors.append(tuple(new_state))
    
    # Move up
    if i > 2:
        new_state = list(state)
        new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
        successors.append(tuple(new_state))
    
    # Move down
    if i < 6:
        new_state = list(state)
        new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
        successors.append(tuple(new_state))
    
    return successors

# Solve using A* algorithm
def solve(initial_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), 0, initial_state))
    explored = set()
    g_values = {initial_state: 0}
    counter = 1
    
    while not frontier.empty():
        _, _, state = frontier.get()
        
        if state == goal_state:
            return True, g_values[state], len(explored)
        
        if state in explored:
            continue
            
        explored.add(state)
        
        for successor in successors(state):
            if successor not in explored:
                new_g = g_values[state] + 1
                if successor not in g_values or new_g < g_values[successor]:
                    g_values[successor] = new_g
                    priority = new_g + heuristic(successor)
                    frontier.put((priority, counter, successor))
                    counter += 1
    
    return False, 0, len(explored)

# Print puzzle in simple format
def print_puzzle(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        print(f"| {state[i]} | {state[i+1]} | {state[i+2]} |")
        print("+---+---+---+")

# MAIN PROGRAM
print("=" * 50)
print("8-PUZZLE SOLVER - FINAL VERSION")
print("=" * 50)

# Test with a solvable puzzle
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

print("\nINITIAL STATE:")
print_puzzle(initial_state)

print("\nGOAL STATE:")
print_puzzle(goal_state)

print("\n" + "=" * 50)
print("SOLVING...")
print("=" * 50)

solvable, steps, nodes = solve(initial_state)

if solvable:
    print("\n✅ SUCCESS: The puzzle IS solvable!")
    print(f"📊 Minimum moves needed: {steps}")
    print(f"📊 Nodes explored: {nodes}")
else:
    print("\n❌ FAILED: The puzzle is NOT solvable.")
    print(f"📊 Nodes explored: {nodes}")

print("\n" + "=" * 50)

# Bonus: Try another solvable puzzle
print("\nTESTING ANOTHER PUZZLE:")
another_puzzle = (1, 2, 3, 4, 0, 5, 7, 8, 6)
print("\nInitial State:")
print_puzzle(another_puzzle)

solvable2, steps2, nodes2 = solve(another_puzzle)
if solvable2:
    print(f"\n✅ This puzzle IS solvable in {steps2} moves!")
else:
    print("\n❌ This puzzle is NOT solvable.")