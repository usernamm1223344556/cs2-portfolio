itemprice = float(input("Enter the price of your object: "))
itemquantity = int(input("Enter the quantity of your object: "))
paymentmo = float(input("Give us your money please: "))

calculate_total = itemprice * itemquantity

if itemprice < 0 or itemquantity < 0 or paymentmo < 0:
    print("No negatives.")
elif paymentmo < calculate_total:
    print("Please give us more money!")
else:
    calculate_change = paymentmo - calculate_total
    print("Your total bill is:", calculate_total)
    print("Your change is:", calculate_change)

1. Each function handles a specific step in the code. The "calculation_total" function gets the cost of a ccertain item and the amount of items purchased, multiplies them together, and computes the final amount the customer needs to pay. On the other hand, the "calculation_change" function gets the total cost and the amount of cash handed over by the customer, which then subtracts the total from the cash, and determines exactly how much money needs to be returned to them.
2. The difference between parameters and arguments is like the difference between a blueprint and the actual building material. Parameters like price and quantity are just placeholder names written into the function to show what kind of info said function expects to receive. Arguments, on the other hand, are the actual, real-world data values (such as 4.99 or 3) that you feed into the function when you run your code.
3. The returned total is put in a variable so it can be passed along to other parts of the program. When the total calculation function is done, it sends the final amount back to the main script, where it is usually stored in a dedicated variable (e.g. customerTotal). This variable acts like a bridge, allowing the program to reuse that exact result later on—most notably by passing it as a starting ingredient into the change calculation function.
4. Separating total calculation from change calculation is highly useful because it makes your code flexible, organized, and easy to fix. By breaking them apart, you can reuse the total calculation function on its own for situations where change isn't needed, such as online shopping carts or credit card payments. This separation also follows the core programming rule of "Single Responsibility," meaning each function does exactly one job, which makes it much easier to pinpoint and fix bugs if your math ever comes out wrong.
