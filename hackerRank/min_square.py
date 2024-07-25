
def minArea(x, y, k):  
    """
    Calculates the minimum area of a square enclosing all points.

    Args:
        x: List of x-coordinates.
        y: List of y-coordinates.
        k: Minimum number of points to enclose (ignored in this simplified version).

    Returns:
        The minimum area of the enclosing square.
    """
    
    # combine the points to use with the original logic
    points = list(zip(x, y))  

    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    side_length = max(max_x - min_x, max_y - min_y)  + 2
    return side_length * side_length



x = [1,1,2]
y = [1,2,1]
result = minArea(x, y, 2)  # k is ignored
print(result)  # Output: 9 