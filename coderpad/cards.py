def max_score(cards):
    n = len(cards)
    dp = [[0] * n for _ in range(n)]  # Table to store optimal scores

    for length in range(2, n + 1, 2):  # Calculate scores for even lengths
        for start in range(n - length + 1):
            end = start + length - 1  # Ending index for the subarray
            if length == 2:
                dp[start][end] = max(cards[start], cards[end])
            else:
                take_left = cards[start] + min(dp[start + 2][end], dp[start + 1][end - 1])
                take_right = cards[end] + min(dp[start + 1][end - 1], dp[start][end - 2])
                dp[start][end] = max(take_left, take_right)

    return dp[0][n - 1]

# Test cases
test_cases = [
    ([1, 9, 10, 5, 6, 4], 18),
    ([59,324,915,608,779,958,814,387,454,505], 3072)
]

for nums, expected in test_cases:
    result = max_score(nums)
    print(f"Test case: {nums}, Expected: {expected}, Got: {result}")  
    assert result == expected, f"Failed for input: {nums}, expected: {expected}, got: {result}"

print("All test cases passed!")

#Time Complexity: O(n^2), optimized compared to a naive recursive solution.
#Space Complexity: O(n^2) due to the DP table.