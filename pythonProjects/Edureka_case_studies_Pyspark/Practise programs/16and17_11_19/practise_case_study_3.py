_title = ''
_firstName = ''
_lastName = ''
_string = "Mr. Shasank Shah jr".split(' ')
for index in sorted(range(len(_string)), reverse=True):
    if _string[index] == '':
        del _string[index]
print(_string)
_maxListLength = (len(_string)-1)
for index in range(len(_string)):
    if (('.') in _string[index]):
        if index == _maxListLength:
            _title = _string[index]
            break
        else:
            print("title")
            _title = _string[index]
    elif ((('.') not in _string[index]) and (index < _maxListLength)):
        #if index < _maxListLength:
            print("here", _string[index])
            _firstName = _string[index]
    elif ((('.') not in _string[index])):
        if index == _maxListLength:
            print("here", _string[index])
            _lastName = _string[index]
'''
        if index == _maxListLength:
            print("sdasdas", _string[index])
            _firstName = _string[index]
            break
'''
print(_title+' '+_firstName+' '+_lastName)
'''    
    elif ((('.') not in _string[index])):
        if index == _maxListLength:
            print("first name")
            _firstName = _string[index]
            break
        else:
            _firstName = _firstName.join(_string[index])
'''

'''
    elif ((('.') not in _string[index]) and (index == 0)):
        _firstName = _string[index]
'''