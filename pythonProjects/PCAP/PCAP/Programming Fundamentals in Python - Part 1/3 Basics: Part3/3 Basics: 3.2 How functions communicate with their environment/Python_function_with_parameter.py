def message(no):
    print("Enter any value", no)


no = 1234
# shadowing
message('!@#$%^&*()_+-=')
print(no)


# positional parameters
def introduction(firstname, lastname):
    print("Hello, my name is", firstname, lastname)


introduction("James", "Bond")
introduction("Luke", "Skywalker")


# keyword argument passing
def introduction(firstname, lastname):
    print("Hello, my name is", firstname, lastname)


introduction(firstname="James", lastname="Bond")
introduction(lastname="Skywalker", firstname="Luke")


# mixing of positional and keyword parameters
def sum(a, b, c):
    print("sum is: ", a + b + c)


sum(3, c=1, b=2)


def introduction(firstname="John", lastname="Smith"):
    print("Hello my name is: ", firstname, lastname)


introduction(lastname="Hopkins")
