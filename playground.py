# Reference:
# https://docs.python.org/3.8/library/stdtypes.html#str.strip
# https://docs.python.org/3.8/library/stdtypes.html#str.lstrip
# https://docs.python.org/3.8/library/stdtypes.html#str.rstrip

# default is whitespace
print(f'strip left and right:{"     word     ".strip()}.')
print(f'left strip:{"     word     ".lstrip()}.')
print(f'right strip:{"     word     ".rstrip()}.')

# stripping specific characters
print(f'stripping *: {"*********intuition*********".strip("*")}')
