# Clean Decision Code Makeover: Student Score Checker
**Name:** Benedict Kyler P. Bigtas
**Section:** 8 - Dahlia
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.
---
# Part 1 - Analyze the Logic
## Input
What information does the program need?
> It needs to get a number between 1 to 100 and shouldn't exceed that limit.

## Valid Range
**Minimum valid score:**
> The minimum valid score is 0.
**Maximum valid score:**
> The maximum valid score is 100.

## Possible Outputs
List all possible outputs of the program.
1. "Outstanding" (if number is between 90-100)
2. "Very Satisfactory" (if number is between 80-89)
3. "Satisfactory" (if number is between 75-79)
4. "Needs Improvement" (if number is below 75)
5. "Invalid Input" (if number is more than 100 or below than zero)

## Boundary Condition
What condition will you use to determine whether the score is valid?
> I will use an "if" statement, "elif" statements, and an "else" function.

## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
> It will classify it if it follows the guidlines like, for example, if the number is more than or equal to 90, it should display "Oustanding".
---
# Part 2 - Flowchart
Insert your flowchart below.
![Score Checker Flowchart](./q1/score_checker_flowchart.png)
---

# Part 3 - Pseudocode
Create a pseudocode showing the logic of your program.

##Sample Pseudocode
START
INPUT score
IF score < 0 OR score > 100 THEN
DISPLAY "Invalid score."
ELSE IF score >= 90 THEN
DISPLAY "Outstanding"
....
END

---
# Part 4 - Clean Code Implementation
## Source code
Insert your source code.
![Score Checker Source Code](./q1/score_checker.py)

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | | | |
| 2 | 0 | Minimum boundary | | | |
| 3 | 74 | Below Satisfactory boundary | | | |
| 4 | 75 | Satisfactory boundary | | | |
| 5 | 80 | Very Satisfactory boundary | | | |
| 6 | 90 | Outstanding boundary | | | |
| 7 | 100 | Maximum boundary | | | |
| 8 | 101 | Above maximum | | | |

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> Write your answers here
### 2. Why did you also test -1 and 101?
> Write your answers here
### 3. Which test helped you understand boundary conditions the most?
> Write your answers here
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> Write your answers here

---

# Reflection
### 1. How did selection structures make the program more useful?
> Write your answers here
### 2. How did proper comments and readable formatting improve your program?
> Write your answers here
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> Write your answers here
