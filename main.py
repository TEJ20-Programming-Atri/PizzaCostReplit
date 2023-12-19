"""
Pizza Cost
Made by Atri
"""

print("Welcome to Atri's Pizzeria!")
# Constants
RENT_COST = 1.00
LABOUR_COST = 0.75
MATERIAL_COST = 0.50
HST = 0.13

# function that makes sure input is a positive number
def valid_input(prompt:str):
  while True:
    try:
      res = float(input(prompt))
      if res >= 0:
        return res
      else:
        print("Value must be a positive number")
    except ValueError:
      print("Value must be a positive number")

# Asks the user for the diameter of the pizza in inches
pizza_diameter = valid_input("Enter the diameter of the pizza in inches: ")

# Calculates the cost of the pizza

# Calculate the subtotal
subtotal = RENT_COST + LABOUR_COST + (MATERIAL_COST * pizza_diameter)

# Calculate the tax
tax = subtotal * HST

# Calculate the total cost
total = subtotal + tax

# Display Total cost to the user
print(f"the total cost of the pizza is ${total:.2f}")