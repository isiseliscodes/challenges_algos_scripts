
def insertion_sort(nums:list[int]) -> list[int]:

    for i in range(1, len(nums)):
        j= i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


nums:list[int] = [3,5,7,1,2,4,6,8,9]
print(insertion_sort(nums))
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9]