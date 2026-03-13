def solve_queens(n):
    board = [-1] * n
    result = []
    
    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or \
               abs(row - i) == abs(col - board[i]):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            result.append(list(board))
            return
        
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    backtrack(0)
    return result

# Solve 8-Queens
solutions = solve_queens(8)
print(f"Total solutions found: {len(solutions)}")
print("\n" + "="*50)

# Display first 3 solutions
for sol_num, solution in enumerate(solutions[:3], 1):
    print(f"\nSolution {sol_num}:")
    print("  " + "-" * 17)
    for row in range(8):
        line = " |"
        for col in range(8):
            if solution[row] == col:
                line += " Q |"
            else:
                line += " - |"
        print(line)
        print("  " + "-" * 17)