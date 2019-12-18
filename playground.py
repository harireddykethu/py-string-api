# Strings are immutable

name = 'Manohar'


alias_name = name  # alias_name is now name

alias_name = 'Anand'  # doesn't change name

print(f'name: {name}, alias_name: {alias_name}')
