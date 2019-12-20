sentence = 'The name that can be named is not the eternal name'

# Syntax: https://docs.python.org/3.8/library/stdtypes.html#str.find

first_index = sentence.find('name')

# index of n in the first occurrance of name in the sentence
print(f'First index of name: {first_index}')
# index is -1 for no match
print(f'First index of no match: {sentence.find("tao")}')

# index within bounds. -1 for not finding
print(f'Index within bounds: {sentence.find("the", 0, 30)}')

# escape characters: https://docs.python.org/2.0/ref/strings.html


# Additional API (from right side): https://docs.python.org/3.8/library/stdtypes.html#str.rfind
