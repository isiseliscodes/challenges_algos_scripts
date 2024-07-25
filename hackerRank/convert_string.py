
def convert(string):
    ints, floats = string.split('.') if '.' in string else (string, "")
    number = 0

    for i, c in enumerate(reversed(ints)):
        number += int(c) * 10 ** i  

    for i, c in enumerate(floats):
        number += int(c) * 10 ** -(i + 1)  

    return number

result = convert("13.87")
print(result)  # Output: 13.87 (as a float)


array = ["abc", "bce", "dce", "acb"]
sets = [set(word) for word in array]
common_letters = set.intersection(*sets)  # Unpack the list of sets
print("Letters present in all elements:", common_letters)  




def char_to_digit(char):
  return ord(char) - ord('0')

print(char_to_digit('5'))  # Output: 5
print(char_to_digit('8'))  # Output: 8