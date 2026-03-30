from funciones import *
from Cositas import *
inventary=[]
Starting()
while True:

    clean_screen()
    W = "✨🌸 WELCOME 🌸✨ "
    print(Pink  + W.center(50, "=") + reset)
    print(Yellow + "What do you what to do today?" + reset)
    print(Pink  + "•1. Register new students.")
    print("•2. Check the student list.")
    print("•3. Search a student.")
    print("•4. Update a student's information.")
    print("•5. Delete a student.")
    print(Green + "•6. Exit." + reset)

    opcion = input(Cyan + "• Selecc an option \n " + reset)
    clean_screen()
    match opcion:
        case "1":
        
            ID = input(Pink  + "💫 Enter your ID \n 💫 " + reset)
            Name = ask_name()
            Age  = ask_age()
            Course = ask_course()
            State = student_state()
            create_student = register_new_student(ID,Name,Age,Course,State)
            inventary.append(create_student)
            print(Green + "✨ ¡student created successfully! ✨ " + reset)
            input(red + "Tap ENTER to continue "+ reset )
            clean_screen()
        case "2":

            check_list(inventary)
            input(red + "Tap ENTER to continue " + reset)
            clean_screen()
    

        case "3":
            search = input(Yellow + "Enter the name or id of the student \n" + reset)
            search_student(inventary,  search)
            input(red + "Tap ENTER to continue " + reset)
            clean_screen()


        case "4":
            input(Yellow + "Enter the student's name \n" + reset)
            ID = input(Pink  + "Enter your ID \n" + reset)
            Name = ask_name()
            Age  = ask_age()
            Course = ask_course()
            State = student_state()
            
            update_student(inventary,ID,Name,Age,Course,State)
            input(red + "Tap ENTER to continue " + reset)
            clean_screen()
            

        case "5":
            input(Yellow +  "Enter the name of the student you want to delete. \n" + reset)
            delete_student(inventary, ID)
            input(red + "Tap ENTER to continue " + reset)
            clean_screen()


        case "6":
            print(Green + "💖 Have a good day 💖 !" + reset)

        case _:
            print(red + "Sorry, try it again" + reset)
