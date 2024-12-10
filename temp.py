def traverse_all_diagonals(matrix, row, col):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Four diagonal directions
    diagonal_paths = {d: [] for d in directions}  # Store elements along each diagonal
    
    for dr, dc in directions:
        r, c = row + dr, col + dc  # Start from the next element in the direction
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):  # Check bounds
            diagonal_paths[(dr, dc)].append(matrix[r][c])  # Add first valid diagonal element
    
    return diagonal_paths

# Example usage
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

row, col = 2, 2  # Starting from the element '11' at (2, 2)
diagonal_elements = traverse_all_diagonals(matrix, row, col)

# Print diagonals
for direction, elements in diagonal_elements.items():
    print(f"Diagonal in direction {direction}: {elements}")
