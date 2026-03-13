from typing import List, Tuple, Set
from collections import deque

class SmartVacuumCleaner:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.position = (0, 0)
        
    def initialize_room(self, dirt_pattern: List[List[int]]):
        """Initialize the room with a specific dirt pattern"""
        self.grid = [row[:] for row in dirt_pattern]
        
        print("Before cleaning the room I detect all of these random dirt")
        print(self.grid)
        print()
        
    def find_dirty_cells(self) -> List[Tuple[int, int]]:
        """Find all dirty cells in the room"""
        dirty = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    dirty.append((i, j))
        return dirty
    
    def find_path(self, start: Tuple[int, int], target: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Find shortest path from start to target using BFS"""
        if start == target:
            return [start]
        
        queue = deque([(start, [start])])
        visited = {start}
        
        while queue:
            (x, y), path = queue.popleft()
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                new_pos = (new_x, new_y)
                
                if (0 <= new_x < self.rows and 0 <= new_y < self.cols and 
                    new_pos not in visited):
                    if new_pos == target:
                        return path + [new_pos]
                    visited.add(new_pos)
                    queue.append((new_pos, path + [new_pos]))
        
        return [start]  # Return just start if no path found
    
    def clean_room(self):
        """Clean the room by finding and cleaning all dirty cells"""
        dirty_cells = self.find_dirty_cells()
        
        if not dirty_cells:
            print("Room is already clean!")
            return
        
        print("Starting cleaning process...")
        print()
        
        # Clean each dirty cell
        for target in dirty_cells:
            # Find path to the dirty cell
            path = self.find_path(self.position, target)
            
            # Follow the path
            for next_pos in path[1:]:  # Skip the current position
                self.position = next_pos
                x, y = next_pos
                print(f"Vacuum in this location now, {x} {y}")
                
                # Clean if dirty
                if self.grid[x][y] == 1:
                    self.grid[x][y] = 0
                    print(f"cleaned {x} {y}")
                print()
    
    def is_room_clean(self) -> bool:
        """Check if all cells are clean"""
        return all(cell == 0 for row in self.grid for cell in row)
    
    def print_final_message(self):
        """Print the final status message"""
        print("Room is clean now, Thanks for using : A.SAFARI CLEANER")
        
        # Ensure all rows have the same length for display
        display_grid = []
        for row in self.grid:
            while len(row) < 4:
                row.append(0)
            display_grid.append(row)
        
        print(display_grid)

def main():
    # Create vacuum cleaner
    vacuum = SmartVacuumCleaner(4, 4)
    
    # Define the dirt pattern from your example
    dirt_pattern = [
        [1, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    # Initialize the room
    vacuum.initialize_room(dirt_pattern)
    
    # Clean the room
    vacuum.clean_room()
    
    # Show final status
    vacuum.print_final_message()

if __name__ == "__main__":
    main()