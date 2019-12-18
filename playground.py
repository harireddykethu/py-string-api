sentence = 'The quick brown fox jumps over the lazy dog'

# string.split() by default splits the string at spaces
# original string remains as such
# result of split is a list of substrings
# split character will be discarded

words = sentence.split()

print(f'Words: {words}')
print(f'Type of words: {type(words)}')

underscore_separated_tokens = 'ABC_123456_MX415_%_4587+/_09$#@'

tokens = underscore_separated_tokens.split('_')
print(f'Tokens: {tokens}')

# if maxsplit is specified, the split is limited to maxsplit
long_string = 'this is a really long sentence here'
limited_words = long_string.split(maxsplit=2)
print(f'Only 2 words: {limited_words}')
