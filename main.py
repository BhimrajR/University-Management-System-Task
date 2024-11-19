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

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        return sum(self.grades)/len(self.grades)
    
    def get_student_summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStudent ID: {self.student_id}\nCourse: {self.course}\nGrades:\n {"\n ".join([str(x) for x in self.grades])}\n"
    
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")

    def increase_salary(self, percentage):
        self.salary += self.salary * percentage / 100

    def get_professor_summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nStaff ID: {self.staff_id}\nDepartment: {self.department}\nSalary: {self.salary}\n"
    
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
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAdmin ID: {self.admin_id}\nOffice: {self.office}\nYears of Service: {self.years_of_service}\n"
    
student1 = Student("Adam", 19, "M", "23BJD", "Literature")
student2 = Student("Jessica", 21, "F", "39DOA", "Natural Sciences")

professor1 = Professor("Josh", 43, "M", "09MKL", "Literature", 80000)
professor2 = Professor("Mike", 37, "M", "68HDO", "Natural Sciences", 60000)

admin1 = Administrator("Ubel", 35, "F", "73KIS", "IT", 5)

print(student1.get_student_summary())
print(student2.get_student_summary())
print(professor1.get_professor_summary())
print(professor2.get_professor_summary())
print(admin1.get_admin_summary())

student1.add_grade(3)
student1.add_grade(6)
student1.add_grade(9)
print(student1.get_student_summary())
print(f"Average grade for {student1.name} is {student1.calculate_average_grade():.2f}")

student2.add_grade(5)
student2.add_grade(7)
student2.add_grade(8)
print(student2.get_student_summary())
print(f"Average grade for {student2.name} is {student2.calculate_average_grade():.2f}")

professor1.give_feedback(student1, "Work on questions similar to Question 5.")

professor2.increase_salary(10)
print(professor2.get_professor_summary())

admin1.increment_service_years()



print(student1.get_student_summary())
print(student2.get_student_summary())
print(professor1.get_professor_summary())
print(professor2.get_professor_summary())
print(admin1.get_admin_summary())