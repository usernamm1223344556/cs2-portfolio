def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def get_performance(average):
    if 85 <= average <= 100:
        return "Mastery"
    elif 70 <= average < 85:
        return "Developing"
    else:
        return "Needs Review"


def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3


score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)
perf_category = get_performance(average)
eligible_status = is_eligible(average, completed_tasks)

print("Average: " + "{:.2f}".format(average))
print("Performance: " + str(perf_category))
print("Eligible for Challenge: " + str(eligible_status))

1. The calculate_average() function returns a number (more specifically, a numerical average), the get_performance() gives you a string and the is_eligible() reutrns a Boolean (True or False).
2. It works like this. Once you call the average function to give you a number, the code turns that number into a usuable variable for the performance function to input.
3. If a student has a high average (e.g., 95) but fewer than three tasks, is_eligible() will return False. This happens because the function uses the and operator. Said operator strictly requires both conditions to be true, and since the task condition fails, the whole thing falls apart.
4. Using return allows other functions to use that as an input for use, unlike a print where it can't be used at all.
