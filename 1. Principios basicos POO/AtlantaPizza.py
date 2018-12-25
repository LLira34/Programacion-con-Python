# AtlantaPizza.py - a simple pizza cost calculator
# Ask the person how many pizzas they want, get number with function eval()

number_of_pizzas = eval(input("How many pizzas do you want? "))

# Ask for menu cost of each pizza
cost_per_pizza = eval(input("How much does each pizza cost? "))

# Calculate the total cost of pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizza

# Calculate the sale tax owed, at 8% of subtotal 
tax_rate = 0.08
sales_tax = subtotal * tax_rate

# Add the sales tax to subtotal for the final total.
total = subtotal + sales_tax

# Show the user the total amount due, including tax
print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sales tax.")
