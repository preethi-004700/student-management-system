import json

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("No Records Found")
    else:
        print("\nStudent Records:")
        for student in students:
            print(student)

def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
