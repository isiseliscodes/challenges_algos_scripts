def get_even_numbers(numbers):

    even_numbers = (x for x in numbers if x % 2 == 0)
    return even_numbers

print(list(get_even_numbers(range(10))))