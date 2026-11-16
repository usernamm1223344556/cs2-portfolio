for number in range(2, 21, 2):
    print(number)
    # the final result should only include the multiples of 2 between said numbers
--------------------------------------------
count = 10
while count >= 1:
    print(count)
    count -= 1
# this should do a countdown from 10 to 1
print("Time is up!")
--------------------------------------------
for number in range(1, 16):
    if number % 3 == 0:
        continue
    print(number)
    # used modulo for this
--------------------------------------------
def show_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
userentry = int(input("Enter a number: "))
show_table(userentry)
# this should show the times table from x1 to x10 of your chosen number
