from model.ClassRoom import ClassRoom
from model.Studen import Student

oop = ClassRoom("OOP")
oop.add_student(Student(1, "Alice", 20, "A001"))
oop.add_student(Student(2, "Bob", 22, "B002"))
print(len(oop))
oop.add_student(Student(3, "Charlie", 21, "C003"))
print(len(oop))

for i in range(len(oop)):
    print(oop[i])