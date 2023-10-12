# Student class

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = ""
        else:
            self.courses = courses

courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
jay = Student("Thevenel", "Joazard")

print(jay.first_name, jay.last_name, jay.courses)