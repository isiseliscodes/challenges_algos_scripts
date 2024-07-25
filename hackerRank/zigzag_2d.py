
array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def print_zigzag(matrix):
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            print(*row)  # Unpack the row for direct printing
        else:
            print(*reversed(row)) # Unpack the reversed row for direct printing

print_zigzag(array)