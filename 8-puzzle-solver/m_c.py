from typing import List, Tuple
from collections import deque

def is_valid_state(state: Tuple[int, int, int, int, int, int]) -> bool:
    """
    Check if a state is valid according to the problem constraints.
    """
    m1, c1, b, m2, c2, d = state  # Fixed: Added d parameter
    
    # Check for negative values
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    
    # Check if missionaries are outnumbered by cannibals on either side
    # Only check if there are missionaries on that side (m1 > 0 or m2 > 0)
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False
    
    return True

def get_successors(state: Tuple[int, int, int, int, int, int]) -> List[Tuple[int, int, int, int, int, int]]:
    """
    Generate all possible valid states that can be reached from a given state.
    """
    m1, c1, b, m2, c2, d = state
    successors = []
    
    if b == 1:  # boat is on the left side
        # Try all possible combinations of moving missionaries and cannibals
        for i in range(min(m1, 2) + 1):  # i = missionaries to move (0-2, but not more than available)
            for j in range(min(c1, 2) + 1):  # j = cannibals to move (0-2, but not more than available)
                if 1 <= i + j <= 2:  # boat capacity: at least 1, at most 2 people
                    new_state = (m1 - i, c1 - j, 0, m2 + i, c2 + j, 0)  # Changed d to 0
                    if is_valid_state(new_state):
                        successors.append(new_state)
    else:  # boat is on the right side
        # Try all possible combinations of moving missionaries and cannibals
        for i in range(min(m2, 2) + 1):  # i = missionaries to move (0-2)
            for j in range(min(c2, 2) + 1):  # j = cannibals to move (0-2)
                if 1 <= i + j <= 2:  # boat capacity: at least 1, at most 2 people
                    new_state = (m1 + i, c1 + j, 1, m2 - i, c2 - j, 1)  # Changed d to 1
                    if is_valid_state(new_state):
                        successors.append(new_state)
    
    return successors

def breadth_first_search() -> List[Tuple[int, int, int, int, int, int]]:
    """
    Find the solution using a breadth-first search algorithm.
    """
    initial_state = (3, 3, 1, 0, 0, 1)  # (m_left, c_left, boat_left, m_right, c_right, boat_side_flag)
    goal_state = (0, 0, 0, 3, 3, 0)
    
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        state, path = queue.popleft()
        
        # If we've reached the goal state
        if state == goal_state:
            return path + [state]
        
        # Skip if already visited
        if state in visited:
            continue
            
        visited.add(state)
        
        # Explore successors
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [state]))
    
    return []  # No solution found

def print_solution(solution: List[Tuple[int, int, int, int, int, int]]) -> None:
    """
    Print the solution in a readable format.
    """
    if not solution:
        print("No solution found!")
        return
    
    print("\nSolution found!")
    print("=" * 50)
    print(f"{'Step':<6} {'Left':<15} {'Boat':<10} {'Right':<15}")
    print("-" * 50)
    
    for i, state in enumerate(solution):
        m1, c1, b, m2, c2, d = state
        boat_pos = "Left" if b == 1 else "Right"
        print(f"{i:<6} {f'M:{m1} C:{c1}':<15} {boat_pos:<10} {f'M:{m2} C:{c2}':<15}")

if __name__ == '__main__':
    solution = breadth_first_search()
    print_solution(solution)