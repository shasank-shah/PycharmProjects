from math import pi, radians, degrees, sin, cos, tan

ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi/2.)
print(sin(ar) / cos(ar) == tan(ar))
#print(asin(sin(ar)) == ar)

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

from random import random, seed, randrange, randint

seed(0)
for i in range(5):
    print(random())
    
print(randrange(1), end = ' ')
print(randrange(0, 1), end = ' ')
print(randrange(0, 1, 1), end = ' ')
print(randint(0, 0), end = ' ')
print("\n")

for i in range(10):
    print(randint(1, 10), end = ', ')

print("\n")
from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))
print(sample(lst, 12)) # it does not throw any error even though the elements_to_choose is greater than list elements

