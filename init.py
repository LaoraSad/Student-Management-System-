from funtion import generic_input

student: dict[str, dict[str, int, str, bool]] = {}

print("---Student Management System with Data Persistence---")

finish: bool = True
while finish:
    try:
        print("*"*40)
        print(" 📋  MENU  📋")
        print("*"*40)
        print("1.Register new student")
        print("2.Check the student list")
        print("3.Find a student")
        print("4.Update a student's information")
        print("5.Delete students.")
        print("6.exit")

        choose: str = input("Select an option: ").strip()

        match choose:
            case "1":
                student_id: str = str(1 if len(student) < 1 else len(student) + 1)

                cedula: int  = int(generic_input("Please enter your cedula: ", False, int))
                name:str = generic_input("Please enter your name: ", False, str)
                last_name:str = generic_input("Please enter your last name: ", False, str)
                age: int = int(generic_input("Please enter your age: ", False, int))
                program: str = generic_input("Please enter your program: ", False, str)
                status: bool = generic_input("Please enter your status[active/inactive]: ", False, str)

                student[student_id] = {"cedula": cedula, "name": name, "last_name": last_name, "age": age, "program": program, "status": status}
                print("-"*40)
                print("student created successfully")
                print("-"*40)
                correc = False

            
            case "2":
                if len(student) <= 0:
                    print("You don't have any registered students yet.")
                else:
                    for key, dato in student.items():
                        print("-"*40)
                        print(f"{key} name: {dato["name"]} last name: {dato["last_name"]} age: {dato["age"]} program: {dato["program"]} status: {dato["status"]}")
                        print("-"*40)
    
            case "3":
                find: int = int(input("Enter the cedula of the student you want to find: "))

                if len(student) <= 0:
                    print("You don't have any registered students yet.")
                    continue
                
                for key, dato in student.items():
                    if dato["cedula"] == find:
                        print(f"{key} name: {dato["name"]} last name: {dato["last_name"]} age: {dato["age"]} program: {dato["program"]} status: {dato["status"]}")
                        break
                    print("Stundent not found")
            
            case "4":
                option: bool = False
                while not option:
                
                    if len(student) <= 0:
                        print("-"*40)
                        print("You don't have any registered students yet.")
                        print("-"*40)
                        option = True
                        continue
                    
                    for key, dato in student.items():
                        print("-"*40)
                        print(f"ID: {key} name: {dato["name"]} last name: {dato["last_name"]} age: {dato["age"]} program: {dato["program"]} status: {dato["status"]}")
                        print("-"*40)
                        option = True
                
                    choose: str = input("Which students do you want to modify? Please enter the ID: ")

                    is_exist: bool = student.get(choose, False)

                    if is_exist:
                        editing: bool = True
                        while editing:
                            try:
                                print("-"*40)
                                print("What do you want to edit about the student?\n")
                                print("\n1.name\n 2.last name\n 3.age\n 4.program\n 5.status\n 6.all the data\n 7.exit\n")
                                print("-"*40)

                                value_edit: str = input("choose an option: ").strip()

                                match value_edit:

                                    case "1":
                                        new_name: str = input("enter the new name: ").strip()
                                        student[choose]["name"] = new_name
                                        print("-"*40)
                                        print("New name added")
                                        print("-"*40)
                                    
                                    case "2":
                                        new_last_name: str = input("enter the new last name: ").strip()
                                        student[choose]["last_name"] = new_last_name
                                        print("-"*40)
                                        print("New last name added")
                                        print("-"*40)
                                    
                                    case "3":
                                        new_age: int = int(input("enter the new age: ").strip())
                                        student[choose]["age"] = new_age
                                        print("-"*40)
                                        print("New age added")
                                        print("-"*40)
                                    
                                    case "4":
                                        new_program: str = input("enter the new program: ").strip()
                                        student[choose]["program"] = new_program
                                        print("-"*40)
                                        print("New program added")
                                        print("-"*40)
                                    
                                    case "5":
                                        new_status: str = input("enter the new status: ").strip()
                                        student[choose]["status"] = new_status
                                        print("-"*40)
                                        print("New status added")
                                        print("-"*40)

                                    case "6":

                                        new_name: str = input("enter the new name: ").strip()
                                        student[choose]["name"] = new_name

                                        new_last_name: str = input("enter the new last name: ").strip()
                                        student[choose]["last_name"] = new_last_name
                        
                                        new_age: int = int(input("enter the new age: ").strip())
                                        student[choose]["age"] = new_age

                                        new_program: str = input("enter the new program: ").strip()
                                        student[choose]["program"] = new_program

                                        new_status: str = input("enter the new status: ").strip()
                                        student[choose]["status"] = new_status

                                        print("-"*40)
                                        print("All student data was updated")
                                        print("-"*40)

                                    case "7":
                                        editing = False
                                        print("-"*40)
                                        print("The data was saved correctly")
                                        print("-"*40)
                                        
                                        

                                    case _:
                                        print("-"*40)
                                        print("Please select the menu options")
                                        print("-"*40)

                            except ValueError:
                                print("⚠️  An invalid option was selected, please try again")
        
            case "5":
                if len(student) <= 0:
                            print("-"*40)
                            print("You don't have any registered students yet.")
                            print("-"*40)
                            option = True
                            continue
                        
                for key, dato in student.items():
                    print("*"*40)
                    print(f"ID: {key} name: {dato["name"]} last name: {dato["last_name"]} age: {dato["age"]} program: {dato["program"]} status: {dato["status"]}")
                    print("-"*40)

                choose_delete: str = input("Which student do you wish to remove? Enter their ID: ").strip()
                delete = student.get(choose_delete, "not fount")
                del(student[choose_delete])
                print("-"*40)
                print("Student delete")
                print("-"*40)
                
            case "6":
                finish = False
                print("see you later")
            case _:
                print(" ⚠️  Option not available, please try again")


    except ValueError:
        print(" 🔄  Please choose a valid option")

