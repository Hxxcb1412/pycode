class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def search_student_by_grade(self, grade):
        result = []
        for student in self.students:
            if student.grade == grade:
                result.append(student)
        return result

    def print_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

# 创建学生管理系统对象
sms = StudentManagementSystem()

# 添加学生
student1 = Student("John", 18, 12)
sms.add_student(student1)

student2 = Student("Mary", 17, 11)
sms.add_student(student2)

student3 = Student("Tom", 16, 10)
sms.add_student(student3)

# 打印全部学生
sms.print_all_students()

# 按姓名搜索学生
search_name = "Mary"
result = sms.search_student_by_name(search_name)
if result:
    print(f"Found student: Name: {result.name}, Age: {result.age}, Grade: {result.grade}")
else:
    print(f"Student with name '{search_name}' not found.")

# 按年级搜索学生
search_grade = 12
result = sms.search_student_by_grade(search_grade)
if result:
    print(f"Found {len(result)} students with grade {search_grade}:")
    for student in result:
        print(f"Name: {student.name}, Age: {student.age}")
else:
    print(f"No students found with grade {search_grade}.")

# 删除学生
sms.remove_student(student2)

# 再次打印全部学生
sms.print_all_students()