nametime = input("Please enter your full name: ")
age_input = input("Please enter your age: ")
grade_input = input("Please enter your grade: ")
emailmo = input("Please enter an email: ")
regiscode = input("Please enter your registration code: ")

has_errors = False
print("\n" + "-" * 30)

if nametime == "":
    print("Name should not be blank.")
    has_errors = True

if not age_input.isdigit():
    print("Age must be an integer.")
    has_errors = True
elif int(age_input) < 11 or int(age_input) > 18:
    print("Age must be a number between 11 to 18.")
    has_errors = True

if not grade_input.isdigit():
    print("Grade must be an integer.")
    has_errors = True
elif int(grade_input) < 7 or int(grade_input) > 12:
    print("Grade must be 7 to 12.")
    has_errors = True

if "@" not in emailmo or "." not in emailmo:
    print("Email format is wrong.")
    has_errors = True

if len(regiscode) < 6 or len(regiscode) > 6:
    print("Code must be 6 characters.")
    has_errors = True

print("-" * 30)
if has_errors == False:
    print("REGISTRATION ACCEPTED")
    print("-" * 30)
    print(f"Student: {nametime}")
    print(f"Age: {age_input}")
    print(f"Grade Level: {grade_input}")
    print(f"Email: {emailmo}")
    print(f"Registration Code: {regiscode}")
else:
    print("REGISTRATION NOT ACCEPTED")
