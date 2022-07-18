print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
)

# initialize empty meal dictionary

# start loop here until user enters quit

# create a variable to store the user's order
order = input("> ")

# print the order in some fancy way we're still figuring out
num_items = 1  # TODO: properly tally items that have been ordered
report = f"** {num_items} order of {order} have been added to your meal **"

print(report)
# end loop
