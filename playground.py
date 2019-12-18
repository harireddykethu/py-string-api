
# https://docs.python.org/3.8/library/stdtypes.html#str.isalnum

numbers = '1234567'
alphabets = 'ABCDEF'

print(f'contains only numbers: {numbers.isdigit()}')
print(f'contains only alphabets: {alphabets.isalpha()}')

ascii_string = 'Greeting'
unicode_string = 'ಶುಭಾಶಯಗಳು'

print(f'ASCII: {ascii_string.isascii()}')
print(f'Is unicode ASCII: {unicode_string.isascii()}')

decimal_number = '314159265359'
print(f'Decimal number as decimal: {decimal_number.isdecimal()}')
print(f'Decimal number as digit: {decimal_number.isdigit()}')

# all decimals are digits but not all digits are decimals
exotic_numbers = '➊⓽➂'
print(f'Exotic number as decimal: {exotic_numbers.isdecimal()}')
print(f'Exotic number as digit: {exotic_numbers.isdigit()}')

print(f'my_variable is a valid identifier: {"my_variable".isidentifier()}')
print(f'Is %my_variable a valid identifier?: {"%my_variable".isidentifier()}')

print(f'Can I mark whitespace? {"                ".isspace()}')
