# You should input your number here
scoreit = int(input("Enter the score: "))

# These are the results depending on your score
if scoreit > 100:
    print("Invalid Input")
elif scoreit >= 90:
    print("Outstanding")
elif scoreit >= 80:
    print("Very Satisfactory")
elif scoreit >= 75:
    print("Satisfactory")
elif scoreit < 0:
    print("Invalid Input")
else:
    print("Needs Improvement")
# End of program
