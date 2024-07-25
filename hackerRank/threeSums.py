
def threeSum(nums):
    result = []
    nums.sort()  # Sorting helps with efficient traversal

    for i in range(len(nums) - 2):  # We'll need at least 3 elements for a triplet
        # Avoid duplicate triplets for the same first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue 

        left, right = i + 1, len(nums) - 1  # Two pointers for the remaining elements

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1  # Increase the sum by moving the left pointer
            elif total > 0:
                right -= 1  # Decrease the sum by moving the right pointer
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Move both pointers to avoid duplicates
                while left < right and nums[left] == nums[left + 1]: 
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
output = threeSum(nums)
print(output)  # Output: [[-1, -1, 2], [-1, 0, 1]]