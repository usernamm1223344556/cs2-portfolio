# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Benedict Kyler P.Bigtas
**Section:** 8 - Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | Text(String) | Presence | "" (blank string) | Cannot be empty. | "Name should not be blank." |
| Age | Whole Number (Integer) | Data Type & Range | "abc", 10, 89 | Must be an integer between 12 and 19. | "Age must be an integer." or "Age must be a number between 11 to 18." |
| Grade Level | Whole Number (Integer) | Data Type & Range | "twelve", 6, 19 | Must be an integer between 7 and 12. | "Grade must be an integer." or "- Grade must be 7 to 12." |
| Email Address | Text(String) | Format | "mariamaria" | Must contain both an '@" symbol and a "." character. | "Email format is wrong." |
| Registration Code | Text(String) | Substring Match | "CS2026" | Must be exactly 6 characters long. | "Code must be 6 characters." |
---
## Validation Questions
### 1. Why should the student name not be blank?
> If the input is blank, it can't be checked and be considered identifiable to the system.
### 2. Why should age be checked for both data type and range?
> It can help specify a certain type of input and what is the range.
### 3. Why should grade level only accept specific values?
> Because that shows the actual high school structure and that means it has a limit.
### 4. What format requirements did you use for the email address?
> The input must contain at least one "@" symbol and at least one "." character to ensure it resembles an email address layout.
### 5. What length requirement did you use for the registration code?
> The registration code must be exactly 6 characters long.
---
# Part B - Program Design
## Pseudocode
START

    INPUT name
    INPUT age
    INPUT grade
    INPUT email
    INPUT code

    SET error = False

    IF name is empty THEN
        PRINT "Blank names are invalid"
        SET error = True
    ENDIF

    IF age is less than 11 OR age is greater than 18 THEN
        PRINT "Age must be between 11 to 18"
        SET error = True
    ENDIF

    IF grade is less than 7 OR grade is greater than 12 THEN
        PRINT "Grade level must be between 7 and 12"
        SET error = True
    ENDIF

    IF email is invalid THEN
        PRINT "Invalid email address format"
        SET error = True
    ENDIF

    IF length of code is less than 6 OR length of code is greater than 6 THEN
        PRINT "Registration code must be exactly 6 characters"
        SET error = True
    ENDIF

    IF error is False THEN
        PRINT "REGISTRATION ACCEPTED"
        PRINT name, age, grade, email, code
    ELSE
        PRINT "REGISTRATION NOT ACCEPTED"
    ENDIF

END
```

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
nametime = input("Please enter your full name: ")
ageing = input("Please enter your age: ")
grader = input("Please enter your grade: ")
emailmo = input("Please enter an email: ")
regiscode = input("Please enter your registration code: ")

has_errors = False
print("\n" + "-" * 30)

if nametime == "":
    print("Name should not be blank.")
    has_errors = True

if not ageing.isdigit():
    print("Age must be an integer.")
    has_errors = True
elif int(ageing) < 11 or int(ageing) > 18:
    print("Age must be a number between 11 to 18.")
    has_errors = True

if not grader.isdigit():
    print("Grade must be an integer.")
    has_errors = True
elif int(grader) < 7 or int(grader) > 12:
    print("Grade must be 7 to 12.")
    has_errors = True

if "@" not in emailmo or "." not in emailmo:
    print("Email format is wrong.")
    has_errors = True

if len(regiscode) != 6:
    print("Code must be 6 characters.")
    has_errors = True

print("-" * 30)
if has_errors == False:
    print("REGISTRATION ACCEPTED")
    print("-" * 30)
    print(f"Student: {nametime}")
    print(f"Age: {ageing}")
    print(f"Grade Level: {grader}")
    print(f"Email: {emailmo}")
    print(f"Registration Code: {regiscode}")
else:
    print("REGISTRATION NOT ACCEPTED")

```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> The validation was used on the Student Name input so that the user does not make the input blank, preventing blank records.
### Data Type Validation
Explain where you used data type validation.
> It was used on the Age and Grade Level inputs to confirm the user typed actual whole numbers instead of text.
### Range Validation
Explain where you used range validation.
> It was used on the Age input to ensure the number falls between 12 and 19, and on the Grade Level input makes sure it falls between 7 and 12.
### Acceptable Value Validation
Explain where you used acceptable value validation.
> It was used alongside range validation on the Grade Level so that it only allows grade numbers in the high school system (7, 8, 9, 10, 11, and 12).
### Pattern Validation
Explain the simple pattern rule you used.
> It was used on the Email Address input by checking that the text includes both an "@" symbol and a "." symbol.
### Length Validation
Explain the length rule you used.
> It was used on the Registration Code input to verify that the string length is exactly 6 characters.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | Benedict Kyler P. Bigtas, 13, 8, bigtas@benedict.com, IJJ493 | Benedict Kyler P. Bigtas, 13, 8, bigtas@benedict.com, IJJ493 | PASS |
| 2 | Blank student name | Presence | Name should not be blank. | Name should not be blank. | PASS |
| 3 | Age = `fourteen` | Data type | Age must be an integer. | Age must be an integer. | PASS |
| 4 | Age = `11` | Minimum boundary | "The message will be accepted." | "The message will be accepted." | PASS |
| 5 | Age = `18` | Maximum boundary | "The message will be accepted." | "The message will be accepted." | PASS |
| 6 | Age = `10` | Range | Age must be a number between 11 to 18. | Age must be a number between 11 to 18. | PASS |
| 7 | Grade Level = `13` | Acceptable value | Grade must be 7 to 12. | Grade must be 7 to 12. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Email format is wrong. | Email format is wrong. | PASS |
| 9 | Registration Code = `ABC` | Length | Code must be 6 characters. | Code must be 6 characters. | PASS |
| 10 | Registration Code = `CS2026` | Valid length | "The message will be accepted." | "The message will be accepted." | PASS |
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
---

[← Back to Main Portfolio](../README.md)
