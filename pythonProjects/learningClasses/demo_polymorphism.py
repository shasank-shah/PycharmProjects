# There are 4 different types of polymorphism
    # Duck Typing
    # Operator Overloading
    # Method Overloading
    # Method Overriding

# Duck Typing use case  -- To make sure that execute method is being used in class
class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

# Operator Overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return self.m1 + other.m1,  self.m2 + other.m2


s1 = Student(1, 2)
s2 = Student(3, 4)

s3 = s1 + s2

print(s3)
########################################################################################
'''
Python magic methods or special functions for operator overloading
Binary Operators:
Operator	Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
Unary Operators :
Operator	Magic Method
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
'''
########################################################################################

