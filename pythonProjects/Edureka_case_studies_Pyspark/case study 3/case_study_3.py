import csv
import re
from Customer import Customer

class CustomerNotAllowedException(Exception):
    pass

def createOrder(title, firstName, lastName):
    with open('FairDealCustomerData.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        _lineCount = 0
        _title = ''
        _firstName = ''
        _lastName = ''
        for row in csv_reader:
            if _lineCount == 0:
                _string = row[1]
                _isBlackListed = int(row[2])
                if '.' in _string:
                    _title = (_string[slice(0, _string.find('.') + 1)]).lstrip()
                    _string = _string[_string.find('.') + 1:].lstrip()
                    _whiteSpaceCounter = 0
                    for index in _string:
                        if (index.isspace()) == True:
                            _whiteSpaceCounter += 1
                    if _whiteSpaceCounter >= 1:
                        _firstName = (_string[slice(0, _string.find(' '))])
                        _string = _string[_string.find(' '):].lstrip()
                    if _string != '':
                        _lastName = _string
                    if _string == '':
                        _lastName = ''
                    if ((title in _title) and (firstName in _firstName) and (lastName in _lastName)):
                        if _isBlackListed >= 1:
                            return 0
                        else:
                            return 1
                else:
                    print(False)
                    _whiteSpaceCounter = 0
                    for index in _string:
                        if (index.isspace()) == True:
                            _whiteSpaceCounter += 1
                    if _whiteSpaceCounter >= 1:
                        _firstName = (_string[slice(0, _string.find(' '))])
                        _string = _string[_string.find(' '):].lstrip()
                    if _string != '':
                        _lastName = _string

if __name__ == "__main__":
    try:
        customer = Customer()
        customer.setTitle("Mr.")
        customer.setFname("Owen")
        customer.setLname("Harris")
        _returnValue = createOrder(customer.getTitle(), customer.getFname(), customer.getLname())
        if _returnValue == 0:
            raise CustomerNotAllowedException
        elif _returnValue == 1:
            print(customer.getTitle() + ' ' + customer.getFname() + ' ' + customer.getLname(), "is not black listed")
        else:
            print(customer.getTitle() + ' ' + customer.getFname() + ' ' + customer.getLname(), "does not exists in inventory")
    except CustomerNotAllowedException:
        print(customer.getTitle() + ' ' + customer.getFname() + ' ' + customer.getLname(), "is black listed")