# Student class

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = ""
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:   
            self.courses.append(course)
            print(f"{course} course added successfully for {self.first_name.capitalize()}")
        else:
            print(f"{self.first_name.capitalize()} is already enrolled in {course} course")
    

courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
jay = Student("Thevenel", "Joazard", courses_1)
jay.add_course('java')
jay.add_course('rails')

print(jay.first_name, jay.last_name, jay.courses)