print('aBcD'.capitalize())
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')
print('epsilon'.endswith('on'))
print('zeta'.find('ta'))
print('zeta'.find('att'))
print('zete'.find('e', 2)) # prints 3 as 2nd 'e' is after 2nd index position

print('abcd123'.isalnum())
print('abcd'.isalnum())
print('123'.isalnum())
print(''.isalnum())
print(''.isalnum())
print('abcd 123'.isalnum()) #False

print('Mu40'.isalpha()) #checking only for letters ---> False
print('Mu'.isalpha()) #checking only for letters ---> True

print('2018'.isdigit()) #checking only for digits ---> True

print('n u 123'.islower())

print('  '.isspace()) # True
print(' \n '.isspace()) # True

print('X1'.isupper())

print(','.join(['omicron', 'pi', 'rho'])) # The join method requires a list

print('SiGmA=60'.lower())
print('SiGmA=60'.upper())

print('[' + ' tau '.lstrip() + ']')

print('www.cisco.com'.lstrip('w.')) # It will strip complete www. from basestring

print('this is it'.replace('is', 'are'))
print('this is it'.replace('is', 'are', 1)) # It will replace if the integer(third argument) is > 1

print('tau tau tau'.rfind('ta'))
print('tau tau tau'.rfind('ta', 9))
print('tau tau tau'.rfind('ta', 3, 9))

print('[' + ' upsilon '.rstrip() + ']')
print('www.cisco.com'.rstrip('m'))

print('phi chi\npsi'.split())

print('omega'.startswith('meg'))

print('[' + ' some string '.strip() + ']')

print('One thing I know, that I know nothing'.swapcase())

print('One thing I know, that I know nothing'.title())
