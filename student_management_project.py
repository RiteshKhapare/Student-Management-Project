class student():
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Roll: {self.roll}  '\
               f'Name: {self.name}  '\
               f'Marks:{self.marks} '
               


students_list = []

def add_student():
    roll = int(input("Enter roll number of student:::"))
    name = input("Enter name here:::")
    marks = float(input("Enter marks here:::"))
    stu = student(roll, name, marks)
    students_list.append(stu)
    print('***One record added***')
               

def show_student():
    for student in students_list:
        print(student)
    
def choices(student_change):
    ch = int(input('What do you want to update\n' \
                   '1. Name\n' \
                   '2. Marks\n'
                   ))

    match ch:
        case 1:
            newname = input("Enter new name")
            student_change.name = newname

        case 2:
            newmarks = float(input("Enter marks here:::"))
            student_change.marks = newmarks

def update_student_info():
    roll = int(input('Enter roll number here:::'))
    student_change = False
    for student in students_list:
        if student.roll == roll:
            student_change = student
            break
    if student_change:
        choices(student_change)

    else:
        print("no such roll found X")



def delete_student_info():
    roll = int(input("Enter Roll number here:::"))
    student_change = False
    for student in students_list:
        if student.roll ==roll:
            student_change = student
            break
    if student_change:
        students_list.remove(student_change)
    else:
        print("no such roll number found X")
        
while True:
    ch = int(input("Enter choice here \n"\
                   '1.Add student\n'\
                   '2.Show student info \n' \
                   '3.Update student info\n' \
                   '4.Delete student info\n' \
                   '5.Exit\n'))

    match ch:
        case 1:
            add_student()
        case 2:
            show_student()
        case 3:
            update_student_info()
        case 4:
            delete_student_info()
        case 5:
            print("Exit")
            break
        case _:
            print("Enter valid number X")
