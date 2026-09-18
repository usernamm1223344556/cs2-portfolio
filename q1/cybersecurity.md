# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Benedict Kyler P. Bigtas
**Section:** 8 - Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and  appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number: 3**
**Case Title: Suspicious Download**
> A pop-up says the student's device is infected and tells them to download an unknown security application.
---
### 1. What cybersecurity threat is shown?
> The pop-up stating that their computer is infected and they should download an application is a way of tricking the user to download the virus (disguised as the aforementioned application).
### 2. What warning signs make the situation suspicious?
> The glaring issue is the application. The pop-up is telling the user to download a "security app" that they're not familiar with. Not to mention computers never actually tell you to download an unknown application since they already have a built-in antivirus, making the pop-up even more suspicious.
### 3. What may be affected?
Check or describe all that apply:
- Data (check)
- Account (check)
- Application
- Device (check)
- Network
- Financial information (check)
> If the user downloaded the application, it could hack your computer instead. It could steal your account information, your financial info, and other private information.
### 4. What information could be exposed or misused?
> They should not download the application and, instead, close it immediately by clicking the X button. If there is no X button, try to close it with Alt + F4 or use Task Manager.
### 5. What should the user do to reduce the risk?
> Use the anti-virus to check if any virus seeped in and block any pop-ups that could appear on the computer.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | They will require you to give your name to get to know you. |
| Section | Collect | It will make it easier to figure out where you are if needed. |
| Club Choice | Collect | This helps gather info and your preferences. |
| School Email | Collect | It's a helpful way of messaging you but it's also limited to your school account. |
| Attendance Status | Collect | They should do that in order to figure out if you're present. |
| Password | Do Not Collect | This is obviously not necessary in the context on a club registration. |
| OTP | Do Not Collect | This is also not necessary in the context of the registration. |
| Home Address | Do Not Collect | They could track your real house and where you actually live. |
| Parent Bank Account | Do Not Collect | This is not even necessary. |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> It makes sure they're getting the information limited to the school and not beyond that.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Full Name | Blank or missing name | (blank) | Must not be empty | Student name is required. |
| Section | Sampaguita, Ilang-Ilang, Rosal, Dahlia | Invalid or unrecognized section | Ruby | Must be one of the four accepted sections | Please choose a valid section. |
| Club Choice | Robotics, Science, Mathematics, Programming | Student selects a club that is not offered | Social Media | Must be one of the four accepted clubs | Please choose a valid club. |
| School Email | School email containing @ | Incorrect email format | studentpshsedu.ph | Must contain @ | Invalid school email address. |
| Attendance Status | Present, Absent, Late | Invalid attendance status | Excused | Must be Present, Absent, or Late | Please choose a valid attendance status. |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> It should accept full names, accepted sections, their club choice, school email, and their attendance. 
### 2. What should your program reject?
> It should reject blank names, invalid sections, invalid clubs, emails with @ or ., and invalid attendance statuses.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> These help reject invalid inputs and makes sure it follows what the program wants.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
# nameofstudent = input("Enter student name: ")
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
```
---
## Security Practices Applied
### Required Input
> Blank input is handled by checking if the student name is empty. If it is blank, the program displays an error message and does not accept the registration.

### Allowed Values
> Section, Club Choice, and Attendance Status only accept certain values. Section accepts Sampaguita, Ilang-Ilang, Rosal, and Dahlia. Club Choice accepts Robotics, Science, Mathematics, and Programming. Attendance Status accepts Present, Absent, and Late.

### Format Check
> The school email is checked to make sure it contains the @ or . symbol. If it does not contain @ or ., the program considers the email invalid.

### Error Messages
> Clear error messages help users understand what information is incorrect and how they can fix it. This makes the program easier to use and prevents confusion.

### Data Minimization
> I decided not to ask for sensitive information such as passwords, home addresses, phone numbers, or personal identification numbers because they are not necessary for the student registration. This helps protect the student's privacy.
---
# Part E - Testing and Reflection
## Testing
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name | Student name is required. / REGISTRATION NOT ACCEPTED | Student name is required. / REGISTRATION NOT ACCEPTED | PASS |
| 3 | Invalid section | Please choose a valid section. / REGISTRATION NOT ACCEPTED | Please choose a valid section. / REGISTRATION NOT ACCEPTED | PASS |
| 4 | Invalid club choice | Please choose a valid club. / REGISTRATION NOT ACCEPTED | Please choose a valid club. / REGISTRATION NOT ACCEPTED | PASS |
| 5 | Email missing `@` | Invalid school email address. / REGISTRATION NOT ACCEPTED | Invalid school email address. / REGISTRATION NOT ACCEPTED | PASS |
| 6 | Email missing `.` | Invalid school email address. / REGISTRATION NOT ACCEPTED | Invalid school email address. / REGISTRATION NOT ACCEPTED | PASS |
| 7 | Invalid attendance status | Please choose a valid attendance status. / REGISTRATION NOT ACCEPTED | Please choose a valid attendance status. / REGISTRATION NOT ACCEPTED | PASS |
| 8 | Different valid inputs | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> One example of this is phishing. Phishing uses fake messages or websites to trick users into giving away personal information, passwords, or other sensitive data.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Users can reduce the risk by checking the sender, avoiding suspicious links or attachments, and not sharing personal information through untrusted messages or websites.
### 3. How can validation rules improve the security of user input?
> Validation rules help prevent incorrect or unexpected data from being entered into a program. They can reduce risks by limiting input to the required format and allowed values.
### 4. Why should a program avoid collecting unnecessary personal information?
> A program should avoid collecting unnecessary personal information because it protects users' privacy and reduces the amount of sensitive data that could be exposed if the system is compromised.
### 5. How did SG7's input validation concepts become security practices in SG8?
> These input validation concept help accept values that are accepted and reject values 
---
# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
