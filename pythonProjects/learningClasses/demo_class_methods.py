# methods
    # Instance method   -- works with instance variables
        # Accessor method   -- Accessing values
        # Mutator method    -- modifying values
    # Class method  -- works with class variables
    # Static method -- just do something

class Student:

    school = "IISC"     # Class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):   # Accessor/getter is just used for getting values and values will not change
        return self.m1

    def set_m1(self, value):    # Mutator/setter may modify value
        self.m1 = value

    @classmethod    # to work with class variables
    def school_info(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class with a static method")

s1 = Student(1, 2, 3)
s2 = Student(4, 5, 6)

print(s1.avg())
print(s2.avg())

print(s1.school_info())
print(s2.school_info())

Student.info()