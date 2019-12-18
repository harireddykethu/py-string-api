# Reference:
# https://docs.python.org/3.8/library/stdtypes.html#str.startswith
# https://docs.python.org/3.8/library/stdtypes.html#str.endswith

print('Mumbai'.startswith('M'))

# check for start from a specific index
print('Bengaluru'.startswith('u', 6))

print('intuition'.endswith('tion'))
print('intuition'.endswith('tion', 5, 9))
