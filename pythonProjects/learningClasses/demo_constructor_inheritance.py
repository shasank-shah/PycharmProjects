# constructor inside a class
# MRO - Method Resolution Order - While calling constructor or method during multiple inheritance, it would start from leaft to right
#                                   for example it would call first A class in (A, B).
class A:
    def __init__(self):
        print("Inside A class init method")
    def feature1(self):
        print("feature 1 - class A")

    def feature2(self):
        print("feature 2")

class B():                     # sub class
    def __init__(self):
        #super().__init__()      # calling constructor of A
        print("Inside B class init method")

    def feature1(self):
        print("feature 1 - class B")

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Inside C class init method")

    def feat(self):
        super().feature2()      # calling method from super class

a1 = C()
a1.feat()