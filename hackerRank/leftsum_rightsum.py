numbers = [ 1,2,3,4,5]
for i in range(len(numbers)):
    # Calc the sum of elements on the left (excluding the current element)
    left_sum = sum(numbers[:i])
    # Calc the sum of elements on the right (excluding the current element)
    right_sum = sum(numbers[i+1:])

print(left_sum, right_sum)


num = 12345
print(num % 10)


import math
num_digits = int(math.log10(num)) + 1
first_digit = num // 10**(num_digits - 1)
print(first_digit)