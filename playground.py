sentence = 'The name that can be named is not the eternal name'

# Syntax: https://docs.python.org/3.8/library/stdtypes.html#str.replace

new_sentence = sentence.replace('name', 'NAME')

new_sentence_with_limit = sentence.replace('name', 'NAME', 1)

print(f'After complete replacement: {new_sentence}')
print(f'After 1 replacement: {new_sentence_with_limit}')
