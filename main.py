# Note: You must download the colorama module before you can run

from colorama import Fore, init

init()


class Course:
    id = 1

    def __init__(self, course_name, course_level):
        self.c_name = course_name
        self.c_level = course_level
        self.c_id = Course.id
        Course.id += 1


class Student:
    id = 1

    def __init__(self, student_name, studnet_level, student_courses=[]):
        self.s_name = student_name
        self.s_level = studnet_level
        self.s_courses = student_courses
        self.s_id = Student.id
        Student.id += 1

    def add_course_to_std(self, add_course_level):
        if self.s_level == add_course_level:
            return True
        else:
            return False

    def display_student_details(self):
        if self.s_courses == []:
            print(Fore.YELLOW + f'Student ID: {self.s_id} , Name: {self.s_name} , Level: {self.s_level}')
        else:
            print(Fore.YELLOW + f'Student ID: {self.s_id} , Name: {self.s_name} , Level: {self.s_level} , Student courses: {self.s_courses}')


students_list = []
courses_list = []

while True:
    print(Fore.BLUE + '''
Student Course Management System Menu:
1. Add New Student
2. Remove Student
3. Edit Student
4. Display all students
5. Create new Course
6. Add Course to student
7. Display all Courses
8. Exit ''' + Fore.RESET)

    choice = int(input('Enter your choice: '))
    # 1. Add New Student
    if choice == 1:
        new_s_name = input(' * Enter the student name: ')
        new_s_level = input(' * Enter the student level (A/B/C): ')
        while True:
            new_s_level = new_s_level.upper()
            if new_s_level not in ['A', 'B', 'C']:
                new_s_level = input('Invalid input ! , Please enter the student level again (A/B/C):')
            else:
                print(Fore.GREEN + 'student saved successfully')
                break
        obj_std = Student(new_s_name, new_s_level, [])
        students_list.append(obj_std)

    # 2. Remove Student
    elif choice == 2:
        id_to_remove = int(input(" * Enter student ID to remove: "))
        for i in students_list:
            if i.s_id != id_to_remove and i is students_list[-1]:
                print(Fore.RED + f'\t\t\t\t Student {id_to_remove} not found in the system .')
            elif i.s_id == id_to_remove:
                students_list.remove(i)
                print(Fore.GREEN + f'Student {i.s_name} has been removed from the system.')
                break


    # 3. Edit Student
    elif choice == 3:
        id_to_edit = int(input(' * Enter student ID to edit: '))
        for i in students_list:
            if i.s_id != id_to_edit and i is students_list[-1]:
                print(Fore.RED + f'\t\t\t\t Student {id_to_edit} not found in the system .')
                break
            elif i.s_id == id_to_edit:
                edit_name = input(" - Enter new name: ")
                edit_level = input(" - Enter new level: ")
                edit_level = edit_level.upper()
                i.s_name = edit_name
                i.s_level = edit_level
                print(Fore.GREEN + f"Student {i.s_id} details update successfully.")


    # 4. Display all students
    elif choice == 4:
        for i in students_list:
            i.display_student_details()

    # 5. Create new Course
    elif choice == 5:
        new_c_name = input(' * Enter the course name: ')
        new_c_level = input(' * Enter the student level (A/B/C): ')
        while True:
            new_c_level = new_c_level.upper()
            if new_c_level not in ['A', 'B', 'C']:
                new_c_level = input('Invalid input ! , Please enter the course level again (A/B/C):')
            else:
                print(Fore.GREEN + 'Course created successfully.')
                break
        obj_cour = Course(new_c_name, new_c_level)
        courses_list.append(obj_cour)

    # 6. Add Course to student
    elif choice == 6:
        add_s_id = int(input(" * Enter student ID: "))
        for i in students_list:
            if i.s_id != add_s_id and i is students_list[-1]:
                print(Fore.RED + f'\t\t\t\t Student {add_s_id} not found in the system .')
                break
            elif i.s_id == add_s_id:
                add_c_id = int(input(" * Enter course ID: "))
                count = 1
                for cour in courses_list:
                    if cour.c_id == add_c_id and i.add_course_to_std(cour.c_level) is True:

                        i.s_courses.append(cour.c_name)
                        print(Fore.GREEN + f'The {cour.c_name} course was added to the student {i.s_name}')
                        break
                    elif cour.c_id == add_c_id and cour.c_level != i.s_level:
                        print(Fore.RED + '\t\t\t\t The course level does not match student level.')
                        break

                    elif cour.c_id != add_c_id and cour is courses_list[-1]:
                        print(Fore.RED + f'\t\t\t\t course {add_c_id} not found in the system .')
                break

    # 7. Display all Courses
    elif choice == 7:
        if courses_list == []:
            print(Fore.RED + "\t\t\t\tNo courses have been added yet")
        else:
            for i in courses_list:
                print(Fore.YELLOW + f'course ID: {i.c_id} , Name: {i.c_name} , Level: {i.c_level}')

    # 8. Exit
    elif choice == 8:
        print(Fore.GREEN + "\t\t\t\t\t\t Exiting program , GSG  wishes you a good day .")
        break

    # anthor choice
    else:
        print(Fore.RED + '\t\t\t\t Invalid input , Try again !')
