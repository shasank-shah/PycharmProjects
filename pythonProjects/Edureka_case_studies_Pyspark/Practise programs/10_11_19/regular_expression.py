import re

print(re.sub(r'[ad]', '$', 'abcdce abcdef abcdef'))
print(re.sub(r'abc', '*', 'abcdef abcdef'))