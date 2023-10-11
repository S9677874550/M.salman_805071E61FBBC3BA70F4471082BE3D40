class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)


students = [
    Student('EREN YEAGER', '001', 8.5),
    Student('ZORO', '007', 6.7),
    Student('GOJO SATORU', '002', 8.6),
    Student('MADARA UCHIHA', '005', 9.9),
    Student('SAITAMA', '006', 9.6),
    Student('GOKU', '003', 9.7),
    Student('LIGHT YAGAMI', '004', 5.7),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, Cgpa: {}".format(student.name, student.roll_number, student.cgpa))
