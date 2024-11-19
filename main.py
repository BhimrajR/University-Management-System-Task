import os
import platform

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
        self.mentor = None

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def get_mentor(self):
        return "No mentor assigned" if self.mentor == None else self.mentor.name
    
    def get_student_summary(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Student ID: {self.student_id}\n"
            f"Course: {self.course}\n"
            "Grades:\n" +
            "\n".join([str(x) for x in self.grades]) +
            "\n"
        )    
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
        self.students = []

    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")

    def increase_salary(self, percentage):
        self.salary += self.salary * percentage / 100
        
    def mentor_student(self, student):
        if student.mentor is not None:
            student.mentor.remove_student(student)
        student.mentor = self
        self.add_student(student)
        print(f"Professor {self.name} is now mentoring Student {student.name} on {student.course}")

    def add_student(self, student):
        if student.name not in self.students:
            self.students.append(student.name)

    def remove_student(self, student):
        if student.name in self.students:
            self.students.remove(student.name)

    def get_mentored_students(self):
        return self.students

    def get_professor_summary(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Staff ID: {self.staff_id}\n"
            f"Department: {self.department}\n"
            f"Salary: {self.salary}\n"
        )
    
class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Admin ID: {self.admin_id}\n"
            f"Office: {self.office}\n"
            f"Years of Service: {self.years_of_service}\n"
        )
   
clear_command = "cls" if platform.system() == "Windows" else "clear"

def clear_console():
    os.system(clear_command)
    
clear_console()

student1 = Student("Adam", 19, "M", "23BJD", "Literature")
student2 = Student("Jessica", 21, "F", "39DOA", "Natural Sciences")

professor1 = Professor("Mr Josh", 43, "M", "09MKL", "Literature", 80000)
professor2 = Professor("Mr Mike", 37, "M", "68HDO", "Natural Sciences", 60000)

admin1 = Administrator("Miss Ubel", 35, "F", "73KIS", "IT", 5)

print(student1.get_student_summary())
print(student2.get_student_summary())
print(professor1.get_professor_summary())
print(professor2.get_professor_summary())
print(admin1.get_admin_summary())

input("Press Enter to continue...")
clear_console()

student1.add_grade(3)
student1.add_grade(6)
student1.add_grade(9)
print(f"Average grade for {student1.name} is {student1.calculate_average_grade():.2f}")

student2.add_grade(5)
student2.add_grade(7)
student2.add_grade(8)
print(f"Average grade for {student2.name} is {student2.calculate_average_grade():.2f}")

input("Press Enter to continue...")
clear_console()

professor1.give_feedback(student1, "Excellent work on the assignment.")
professor2.increase_salary(10)
admin1.increment_service_years()

print(student1.get_student_summary())
print(student2.get_student_summary())
print(professor1.get_professor_summary())
print(professor2.get_professor_summary())
print(admin1.get_admin_summary())

input("Press Enter to continue...")
clear_console()

professor1.mentor_student(student1)
professor1.mentor_student(student2)
print(f"The mentored students of {professor1.name} are " + ', '.join(professor1.get_mentored_students()))

print(f"The mentor of {student1.name} is {student1.get_mentor()}")
print(f"The mentor of {student2.name} is {student2.get_mentor()}")

professor2.mentor_student(student2)
print(f"The mentored students of {professor2.name} are " + ', '.join(professor2.get_mentored_students()))
print(f"The mentored students of {professor1.name} are " + ', '.join(professor1.get_mentored_students()))
print(f"The mentor of {student1.name} is {student1.get_mentor()}")
print(f"The mentor of {student2.name} is {student2.get_mentor()}")