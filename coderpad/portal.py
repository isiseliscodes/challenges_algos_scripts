def compute_final_position(width, height, position, portalA, portalB, moves):
    """Calculates the final position of an avatar after a series of moves in a grid with portals.

    Args:
        width: The width of the grid.
        height: The height of the grid.
        position: The initial position of the avatar as [x, y].
        portalA: The location of portal A as [x, y].
        portalB: The location of portal B as [x, y].
        moves: A string of characters representing the avatar's movements (U, D, L, R).

    Returns:
        The final position of the avatar as [x, y].
    """

    x, y = position

    for move in moves:
        if move == "U" and y > 0:
            y -= 1
        elif move == "D" and y < height - 1:
            y += 1
        elif move == "L" and x > 0:
            x -= 1
        elif move == "R" and x < width - 1:
            x += 1

        # Check for portal teleportation
        if [x, y] == portalA:
            x, y = portalB
        elif [x, y] == portalB:
            x, y = portalA

        print([x, y])
    return [x, y]





# Test Cases with assert results
# test: bidirectional portals
# dont step outside the limits of the grid
test_cases = [
    {
        "width": 5,
        "height": 4,
        "position": [0, 3],
        "portalA": [4, 0],
        "portalB": [4, 1],
        "moves": "UUUUU",
        "expected": [0, 0]
    },
    {
        "width": 5,
        "height": 5,
        "position": [0, 0],
        "portalA": [1, 1],
        "portalB": [3, 3],
        "moves": "RRRUUDD",
        "expected": [3, 0]
    },
    {
        "width": 5,
        "height": 5,
        "position": [0, 0],
        "portalA": [1, 1],
        "portalB": [3, 3],
        "moves": "LLLL",
        "expected": [0, 0]
    },
    {
        "width": 5,
        "height": 5,
        "position": [0, 0],
        "portalA": [1, 1],
        "portalB": [3, 3],
        "moves": "UUUU",
        "expected": [0, 0]
    }
]

for test_case in test_cases:
    result = compute_final_position(
        test_case["width"],
        test_case["height"],
        test_case["position"],
        test_case["portalA"],
        test_case["portalB"],
        test_case["moves"]
    )
    expected = test_case["expected"]
    nums = test_case["moves"]
    print(f"Test case: {nums}, Expected: {expected}, Got: {result}")  
    assert result == expected, f"Failed for input: {nums}, expected: {expected}, got: {result}"

print("All test cases passed!")


