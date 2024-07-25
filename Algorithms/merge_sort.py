
def merge_sort(nums:list[int]) -> list[int]:
    # It is a recursive funtion so we need to give it an exit point
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2    #Find  the middle index
    left = nums[:mid]      #Find the left array
    right = nums[mid:]     #Find the right array

    left = merge_sort(left)     #recursevely sort left array
    right = merge_sort(right)    #recursevely sort right array


    #merge
    i , j , k = 0 , 0 , 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:   #compare elements from left and right sublist
            nums[k] = left[i]   # chose the smaller element and place it in the original list
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left or right sublists
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums




nums:list[int] = [3,5,7,1,2,4,6,8,9]
print(merge_sort(nums))
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9]