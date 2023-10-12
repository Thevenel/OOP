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

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{course} course removed successfully")
        else:
            print(f"{course} not found")

    def __len__(self):
        return len(self.courses)
    
    def __repr__(self) -> str:
        return f"Student('{self.first_name}', '{self.last_name}', {self.courses})"

    def __str__(self):
        return f"First Name: \t{self.first_name}\
        \nLast Name: \t{self.last_name}\
        \nCourses : \t{' - '.join(map(str.capitalize, self.courses))}"

courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
jay = Student("Thevenel", "Joazard", courses_1)


print(jay)