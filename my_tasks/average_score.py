# https://www.cyberforum.ru/python-tasks/thread2875740.html

class Student():

    def __init__(self):
        string = input().split()
        self.name = string[0] + ' ' + string[1]
        self.maths = int(string[2])
        self.physics = int(string[3])
        self.informatics = int(string[4])


class Group():

    def __init__(self):
        self.all_student = []

    def add_student(self):
        self.all_student.append(Student())

    def avg_maths(self):
        return sum(student.maths for student in self.all_student) / len(self.all_student)

    def avg_physics(self):
        return sum(student.physics for student in self.all_student) / len(self.all_student)

    def avg_informatics(self):
        return sum(student.informatics for student in self.all_student) / len(self.all_student)


group = Group()
for _ in range(int(input())):
    group.add_student()

print(f'{group.avg_maths():.6f} {group.avg_physics():.6f} {group.avg_informatics():.6f}')
