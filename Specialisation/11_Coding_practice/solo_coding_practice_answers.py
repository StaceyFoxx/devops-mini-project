"""
Approach

Create an empty dictionary to store {juice_name: order_count}.
Loop through every order.
Add or update each juice’s count.
Keep track of which juice currently has the highest count.
Print the result with the juice name and total orders
"""

def best_selling_juice(orders):
    # dictionary to store each juice and its sales count
    sales = {}
    top_juice = ''
    sales[top_juice] = 0  # base value so comparisons don't fail

    # loop through all juice orders
    for drink in orders:
        # if this is the first time we see the juice, add it to dictionary
        if drink not in sales:
            sales[drink] = 0
        # increment its count
        sales[drink] += 1

        # check if this drink has now overtaken the top seller
        if sales[drink] > sales[top_juice]:
            top_juice = drink

    return f"🥤 The most popular juice is {top_juice} with {sales[top_juice]} orders!"


# TEST CASE
orders = [
    "Mango", "Apple", "Mango", "Berry", "Apple", "Apple",
    "Berry", "Mango", "Mango", "Berry"
]

print(best_selling_juice(orders))
