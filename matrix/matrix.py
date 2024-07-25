def has_hole(matrix, row, col, visited):
  """
  This function checks if a cell is part of a hole (contiguous region of 0s) in the matrix.
  Args:
      matrix: The 2D binary matrix.
      row: The row index of the current cell.
      col: The column index of the current cell.
      visited: A set to keep track of visited cells.
  Returns:
      True if the cell is part of a hole, False otherwise.
  """
  rows, cols = len(matrix), len(matrix[0])

  # Check if out of bounds or already visited
  if (row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited):
    return False

  # Check if current cell is 0 (part of a hole)
  if matrix[row][col] == "0":
    visited.add((row, col))

    # Recursively explore adjacent cells (up, down, left, right)
    has_hole(matrix, row + 1, col, visited)
    has_hole(matrix, row - 1, col, visited)
    has_hole(matrix, row, col + 1, visited)
    has_hole(matrix, row, col - 1, visited)
    return True

  return False

def count_holes(matrix):
  """
  This function counts the number of holes in the binary matrix.
  Args:
      matrix: The 2D binary matrix.
  Returns:
      The number of holes in the matrix.
  """
  if not matrix:  # Handle empty matrix
    return 0

  rows = len(matrix) 
  cols = len(matrix[0])

  visited = set()  # Set to store visited cells
  hole_count = 0

  # Iterate through each cell in the matrix
  for row in range(rows):
    for col in range(cols):
      if matrix[row][col] == "0" and (row, col) not in visited:
        # If unvisited 0 cell, explore the hole and increment count
        has_hole(matrix, row, col, visited)
        hole_count += 1

  return hole_count

# Example usage (replace with your actual matrix)
matrix = ["01111","01101","00011","11110"]

number_of_holes = count_holes(matrix)
print(f"The number of holes in the matrix is: {number_of_holes}")
