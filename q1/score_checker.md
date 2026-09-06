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
| 80-89 | Very Satisfactory |
| 75-79 | Satisfactory |
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

BEGIN
    INPUT scoreit

    IF scoreit > 100 THEN
        DISPLAY "Invalid Input"
    ELSE IF scoreit >= 90 THEN
        DISPLAY "Outstanding"
    ELSE IF scoreit >= 80 THEN
        DISPLAY "Very Satisfactory"
    ELSE IF scoreit >= 75 THEN
        DISPLAY "Satisfactory"
    ELSE IF scoreit < 0 THEN
        DISPLAY "Needs Improvement"
    END IF
END

---
# Part 4 - Clean Code Implementation
## Source code
![Score Checker Source Code](./q1/score_checker.py)

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum |Invalid Input |Invalid Input |It Works|
| 2 | 0 | Minimum boundary |Needs Improvement |Needs Improvement |It Works|
| 3 | 74 | Below Satisfactory boundary |Needs Improvement |Needs Improvement |It Works|
| 4 | 75 | Satisfactory boundary |Satisfactory |Satisfactory|It Works|
| 5 | 80 | Very Satisfactory boundary |Very Satisfactory |Very Satisfactory|It Works|
| 6 | 90 | Outstanding boundary |Outstanding|Outstanding|It Works|
| 7 | 100 | Maximum boundary |Outstanding|Outstanding|It Works|
| 8 | 101 | Above maximum |Invalid Input |Invalid Input |It Works|

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> These values are the most important than other values since they show the limit that the code can input and make an output.
### 2. Why did you also test -1 and 101?
> In this case, these values show what happens when you try to exceed the limits of the code.
### 3. Which test helped you understand boundary conditions the most?
> It was the part where I tried putting values beyond/below the limits of the boundaries.
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> There were no cases of any of my tests failing.

---

# Reflection
### 1. How did selection structures make the program more useful?
> Selection structures help branch out into different outcomes depending on the input. It allows the user to be able to do such things without using repeated amounts of coding lines.
### 2. How did proper comments and readable formatting improve your program?
> Proper comments and clean formatting make your program readable, maintainable, and easy to debug. Comments help explain the code easly without looking at the code and figuring it out by themselves while proper formatting makes it much more simple and able to be read without difficulties.
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> Write your answers here
