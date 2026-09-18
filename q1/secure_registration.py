nameofstudent = input("Enter student name: ")
sectioned = input("Enter section: ")
clubb = input("Enter club choice: ")
schoolsemail = input("Enter school email: ")
attendance = input("Enter attendance status: ")

error = False

if nameofstudent == "":
    print("Student name is required.")
    error = True

if sectioned not in ["Sampaguita", "Ilang-Ilang", "Rosal", "Dahlia"]:
    print("Please choose a valid section.")
    error = True

if clubb not in ["Robotics", "Science", "Mathematics", "Programming"]:
    print("Please choose a valid club.")
    error = True

if "@" not in schoolsemail or "." not in schoolsemail:
    print("Invalid school email address.")
    error = True

if attendance not in ["Present", "Absent", "Late"]:
    print("Please choose a valid attendance status.")
    error = True

if error == False:
    print("REGISTRATION ACCEPTED")
    print("Student Name:", nameofstudent)
    print("Section:", sectioned)
    print("Club:", clubb)
    print("School Email:", schoolsemail)
    print("Attendance:", attendance)
else:
    print("REGISTRATION NOT ACCEPTED")
