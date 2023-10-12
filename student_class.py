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

    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip()) # we use Class name to access a static method
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in: # compare the student object with the line in the file
                    return True
            return False
                

    def add_to_file(self, filename):
        pass

    ## When a method has no relation with the classes method, you declare it as @staticmethod
    @staticmethod 
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details
    
    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)
    
    def __repr__(self) -> str:
        return f"Student('{self.first_name}', '{self.last_name}', {self.courses})"

    def __str__(self):
        return f"First Name: \t{self.first_name}\
        \nLast Name: \t{self.last_name}\
        \nCourses : \t{' - '.join(map(str.capitalize, self.courses))}"

# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
file_name = 'data.txt'
jay = Student("thevenel","joazard",['python','ruby','javascript'])
print(jay.find_in_file(file_name))


# print(jay)

# terlly,sylvain:python,ruby,javascript
# john,doe:python,ruby,javascript