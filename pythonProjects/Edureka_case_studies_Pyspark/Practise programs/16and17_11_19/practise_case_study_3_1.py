import re

_title = ''
_firstName = ''
_lastName = ''
_string = "    Mr. Shasank Shah jr   ".strip()
if '.' in _string:
    print(True)
    _title = (_string[slice(0, _string.find('.')+1)])
    _string = _string[_string.find('.')+1:].lstrip()
    print(_title)
    print(_string)
    _whiteSpaceCounter = 0
    for index in _string:
        if (index.isspace()) == True:
            print("here")
            _whiteSpaceCounter += 1
    print(_whiteSpaceCounter)
    if _whiteSpaceCounter >= 1:
        _firstName = (_string[slice(0, _string.find(' '))])
        _string = _string[_string.find(' '):].lstrip()
    print(_firstName)
    print(_string)
    if _string != '':
        _lastName = _string

    print("The title is: ", _title, " and the first name is: ", _firstName, " and the last name is: ", _lastName, "asdadad")
    print(_title+' '+_firstName+' '+_lastName)
    #_firstName = _string.lstrip()
    #print(_title+' '+_firstName)
else:
    _whiteSpaceCounter = 0
    for index in _string:
        if (index.isspace()) == True:
            print("here")
            _whiteSpaceCounter += 1
    print(_whiteSpaceCounter)
    if _whiteSpaceCounter >= 1:
        _firstName = (_string[slice(0, _string.find(' '))])
        _string = _string[_string.find(' '):].lstrip()
    print(_firstName)
    print(_string)
    if _string != '':
        _lastName = _string

    print("The title is: ", _title, " and the first name is: ", _firstName, " and the last name is: ", _lastName, "asdadad")
    print(_firstName+' '+_lastName)