#Surya Hardiansyah

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
print('Q1') 
class MyClass():
#    def __init__():
    def __init__(self):
        self.a = 10
        self.b = 20
#        self.x = a + b
        self.x = self.a + self.b # refer to the accessible a and b 
        # for my_instance
my_instance = MyClass()
my_instance.x
print(my_instance.x)

#2
print('\nQ2')
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        x = a + b
        self.x = x # can be accessed as an attribute of my_instance
my_instance = MyClass()
my_instance.x
print(my_instance.x)

#3
print('\nQ3')
class MyClass():
#    def __init__(a, b):
    def __init__(self, a, b): # include 'self' to allow instance methods
    # and variables to be accessible to 'my_instance'
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x
print(my_instance.x)

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
print('\nQ4')
#  + The instance should take two arguments when created; student name, 
#    and student year
#  + At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  + Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  + When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  + Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.
class HarristasCourses():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.enrolled_courses = []
        
    def enroll(self, course_name, course_number, course_days, course_times):
        # check for time overlap with already enrolled courses
        for course in self.enrolled_courses:
            if course_days == course['days'] and course_times == course['times']:
                print(f"Cannot enroll in {course_name} ({course_number}): time overlaps with another course.")
                return
        
        # if no overlap, enroll in the course
        course = {
            'name': course_name,
            'number': course_number,
            'days': course_days,
            'times': course_times
        }
        self.enrolled_courses.append(course)
        print(f"Enrolled in {course_name} ({course_number}).")

        
    def drop_course(self, course_number):
        # Remove course by its number
        for course in self.enrolled_courses:
            if course['number'] == course_number:
                self.enrolled_courses.remove(course)
                print(f"Dropped {course['name']} ({course_number}).")
                return
        print(f"Course {course_number} not found in enrolled courses.")

    def show(self):
        print(f"Name: {self.name}\nYear: {self.year}\nEnrolled Courses:")
        if not self.enrolled_courses:
            print(" None")
            return
        for course in self.enrolled_courses:
            print(f" - {course['name']} ({course['number']}): {course['days']} at {course['times']}")

            
# testing the class
student1 = HarristasCourses('Surya Hardiansyah', 2025)
student1.enroll('DAPFPP I - Python Programming', 'PPHA 30537 3', 'Tue Thu', '9:30am-10:50am')
student1.enroll('Introduction to GIS and Spatial Analysis', 'PPHA 38712 1', 'Tue Thu', '12:30pm-1:50pm')
student1.enroll('DAPFPP I - Python Programming', 'PPHA 30537 5', 'Tue Thu', '12:30pm-1:50pm')  # this will fail due to time overlap
student1.enroll('Survey Questionnaire Design', 'PPHA 41800 1', 'Wed', '4:30pm-7:20pm')
print('\n')
student1.show()

# dropping a course
print('\n')
student1.drop_course('PPHA 30537 3')
print('\n')
student1.show()

# showing unenrolled student
print('\n')
student2 = HarristasCourses('Jane Doe', 2025)
student2.show()