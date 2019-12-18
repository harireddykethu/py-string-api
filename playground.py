word = 'education'

# Syntax:
# Single letter can be selected by [i] where i is the zero-based index
# Negative index such as string[-i] can be used, in which case, -1 stands for the last letter
# string[x:y] where x is the starting index and y is the ending index
# If x is absent, 0 or the start is presumed
# If y is absent, end is presumed
# x is inclusive while y is not-inclusive: mathematically, [x, y)
# Ideally, x < y
# If selection indexes [x:y] are out of the range, or illegal
# it results in either complete string or an empty string as the case may be.
# No error is thrown in such cases.
# But, single letter access exceeds the bound, IndexError will be thrown


# 5th letter (index is 4)
print(f'Fifth letter: {word[4]}')

# penultimate letter by negative index (index is -2)
print(f'Letter before the last letter: {word[-2]}')

# first 3 letters
print(f'First 3 letters: {word[0:3]}')

# end index goes out of bound
print(f'[:100]: {word[:100]}')

# beginning index is greater than ending index
print(f'[4:2]: {word[4:2]}')

# illegal indexes
print(f'[250:-100]: {word[250:-100]}')
