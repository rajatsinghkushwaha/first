stu_record={}

def finder():
    name=input("Please enter student name: ")
    if(name.capitalize() in stu_record)==True:
        print("{} has been registered with marks: ".format(name.capitalize()),stu_record[name.capitalize()])
        asking()
    else:
        print("Student with name {} doesn't exists".format(name.capitalize()))
        asking()

def modifier():
    name=input("Please enter the name of the student you want to modify: ")
    if(name.capitalize() in stu_record)==True:
        new_name=input("Re_enter the new name: ")
        new_marks=float(input("Re_enter new marks: "))
        if(new_marks>100):
            print("Marks cannot be greater than 100")
            modifier()
        del(stu_record[name.capitalize()])
        stu_record[new_name.capitalize()]=new_marks
        print("{} has been modified successfully".format(new_name.capitalize()))
        asking()
    else:
        print("Student with name {} doesn't exists".format(name.capitalize()))
        asking()

def new_record():
    name=input("Please enter new student name: ")
    if(name.capitalize() in stu_record)==True:
        print("{} has been already registered with marks: ".format(name.capitalize()),stu_record[name.capitalize()])
        asking()
    marks=float(input("Please enter marks: "))
    if(marks>100):
        print("Marks cannot be greater than 100")
        new_record()
    stu_record[name.capitalize()]=marks
    print("{} has been entered successfully".format(name.capitalize()))
    asking()

def remover():
    name=input("Please enter the name of student you want to delete: ")
    if(name.capitalize() in stu_record)==True:
        del(stu_record[name.capitalize()])
        print("{} has been removed successfully".format(name.capitalize()))
        asking()
    else:
        print("Student with name {} doesn't exists".format(name.capitalize()))
        asking()

def asking():
    a=input("Press n to enter new student:\nPress f to find student record:\nPress m to modify student record:\nPress d to delete student record:\npress r to see all students:\nPress q to quit: " )
    if(a.lower()=='q'):
        exit()
    elif(a.lower()=='f'):
        finder()
    elif(a.lower()=='m'):
        modifier()
    elif(a.lower()=='n'):
        new_record()
    elif(a.lower()=='d'):
        remover()
    elif(a.lower()=='r'):
        print(stu_record)
        asking()
    else:
        print("Please enter a valid input")
        asking()

asking()



