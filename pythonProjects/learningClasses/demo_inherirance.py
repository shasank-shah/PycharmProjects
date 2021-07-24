# to get methods of other class into current class
# single level inheritance
class A:                        # super class
    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")

class B():                     # sub class
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

# multi level inheritance
class C(B):                     # mutilevel sub class
    def feature5(self):
        print("feature 5")

# multiple inheritance
class D(A, B):  # removing A super class from B class to obtain mutiple level inheritance
    def feature6(self):
        print("feature 5")

a1 = D()
a1.feature6()