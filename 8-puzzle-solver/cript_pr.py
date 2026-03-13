from itertools import permutations

def solve_cryptarithmetic(puzzle):
    """
    Solves the cryptarithmetic puzzle.
    puzzle: a string containing the puzzle in the form of "WORD + WORD = RESULT"
    Returns a dictionary mapping letters to digits, or None if no solution is found.
    """
    # Parse the puzzle
    parts = puzzle.split()
    word1 = parts[0]
    word2 = parts[2]
    result = parts[4]
    words = [word1, word2, result]
    
    # Get all unique letters
    letters = set(''.join(words))
    if len(letters) > 10:
        return None  # More than 10 letters, no solution is possible
    
    # Try all possible digit assignments
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Check for leading zeros
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
            continue
        
        # Convert words to numbers
        num1 = sum(mapping[c] * (10 ** i) for i, c in enumerate(word1[::-1]))
        num2 = sum(mapping[c] * (10 ** i) for i, c in enumerate(word2[::-1]))
        num_result = sum(mapping[c] * (10 ** i) for i, c in enumerate(result[::-1]))
        
        # Check if the equation holds
        if num1 + num2 == num_result:
            return mapping
    
    return None

# Example usage
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)
if mapping:
    print(mapping)
    # Create translation table for the puzzle string
    translation = str.maketrans({k: str(v) for k, v in mapping.items()})
    print(puzzle.translate(translation))
else:
    print('No solution found.')