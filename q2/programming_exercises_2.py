school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]
# these are the list of items
print("School item at index 0:", school_items[0])
print("School item at index 1:", school_items[1])
print("School item at index 2:", school_items[2])
print("School item at index 3:", school_items[3])
print("School item at index 4:", school_items[4])

listofdestinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]
# the list of destinations as presented
print("All of the destinations:")
for place in listofdestinations:
    print(place)
# prints the list
print(listofdestinations[1:4])

search = input("Enter a destination to search: ")
print("Found!" if search in listofdestinations else "Not found.")
# either it's found or not
listofdestinations[2] = "Iloilo"
print(listofdestinations)
