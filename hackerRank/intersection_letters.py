array = ["abc", "bce", "dce", "acb"]
sets = [set(word) for word in array]
print(sets)
common_letters = set.intersection(*sets)  # Unpack the list of sets
print("Letters present in all elements:", common_letters)  