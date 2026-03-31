#We import the functions
import time
from Cositas import * 
import os
#We define the functions
def Starting():
    
    print(Cyan + "Staring ..." + reset)
    time.sleep(1)

    print(Pink + "3..." + reset)
    time.sleep(1)
    print(Pink  + "2..." + reset)
    time.sleep(1)
    print(Pink  + "1..." + reset)
    time.sleep(1)

def clean_screen():
    os.system('clear')


def register_new_student(ID, Name,Age,Course,State):
    dictionary = {"id": ID,
                "name": Name,
                "age": Age,
                "course": Course,
                "state": State}
    return dictionary


def ask_name():
    while True:
        student_name= input(Cyan + "🎀 Write the student's name \n 🎀 " + reset)
        if not student_name.isalpha():
            print("Please. Enter only letters")
            continue
        return student_name
        
def ask_age():
    while True:
        student_age = int(input(Pink + "☁️ Enter your age \n ☁️ " + reset))
        if student_age <= 0:
            print("Error, enter a valid age")
            continue
        return student_age

def ask_course():
    student_course = input(Cyan + "💻  Enter your course \n 💻 " + reset)
    return student_course


def student_state():
    
    while True:
        student_state = input(Pink + "🔃 Enter your state (active/inactive) \n 🔃 " + reset)
    
        if student_state == "active":
            return "active"
        elif  student_state == "inactive":
            return "inactive"
        else:
            print("Error")
            break

def check_list(inventary):
    if len(inventary) == 0:
        print("¡Ups!, Empy inventory")
    for student in inventary:
        print(f"ID: {student ['id']}, Name: {student['name']}, Age: {student['age']}, Course:{student['course']}, State: {student['state']} ")
    
def search_student(inventary, search):


    for student in inventary:
        if search.lower() in student["name"].lower() or search == student["id"]:
            print("student find")
            print(f"ID: {student ['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course:{student['course']}")
            print(f"State: {student['state']}")

            return inventary

    if not inventary:
        print("Sorry,there is no student with that ID or name")

def update_student(inventory,ID,Name,Age,Course,State):
    for student in inventory:
        if student in ["id"] == ID:
            student["name"] = Name,
            student["age"] = Age,
            student["course"] = Course,
            student["state"] =  State
            return inventory
        print(Green + "✨ ¡student update successfully! ✨ " + reset)
        if not inventory:
            print("Sorry, we can't find a student with that name")
    
        
        
    

def delete_student(inventary, ID):
    for student in inventary:
        if student["id"] == ID:
            inventary.remove(student)
            print(Green + f"student {student["name"]} successfully eliminated" + reset)
            return inventary
        else:
            print(red + "We couldn't find any students with that ID" + reset )
            return inventary
        


