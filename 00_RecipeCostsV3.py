import pandas

# Functions go here
# Checks user has entered yes or no to a given question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter either yes or no")

# Checks users enter an integer to a given question
def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print("Please enter an integer")
            print()

# Checks that user response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        # If response is blank output error
        if response == "":
            print(error)
            continue

        
        return response

# Currency formatting function
def currency(x):
    return f"${x:.2f}"

# Get the ingredient name, quantity, units, price, and quantity per packet. Return as a list for easy printing
def get_expenses(var_fixed):
    
    # Set up dictionaries and lists for all items
    ingredient_list = []
    quantity_list = []
    unit_list = []
    price_list = []
    quantity_pp_list = []
    quantity_costs_list = []

    ingredient_dict = {
        "Ingredient": ingredient_list,
        "Quantity": quantity_list,
        "Units": unit_list,
        "Price": price_list,
        "Quantity per packet / box": quantity_pp_list,
        "Cost based on quantity of items used": quantity_costs_list
    }

    # loop to get the ingredient name, quantity, units, price, and quantity per packet from the user
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()

        # Get the ingredient name, quantity, units, price, and quantity per packet from the user
        ingredient_name = not_blank("What is the ingredient name? ","The ingredient name can't be blank.")
        
        # If user enters exit code end loop
        if ingredient_name.lower() == "xxx":
            break

        quantity = num_check("Quantity: ", "The amount must be a number more than zero", float)

        units = input("What are the units for the item? ")
        
        price = num_check("Price for the store item? (Next question will ask the quantity included in this packet): $",
                            "The amount must be a number more than zero", float)
        
        quantity_pp = num_check("What was the Quantity included in the packet / box: ",
                            "The amount must be a number more than zero", float)
        
        # Find the price based on the amount of quantity used in the packet
        quantity_costs = (price / quantity_pp) * quantity
            
        # Add ingredient name, quantity, units, price, and quantity per packet into lists, and quantity costs to list
        ingredient_list.append(ingredient_name)
        quantity_list.append(quantity)
        unit_list.append(units)
        price_list.append(price)
        quantity_pp_list.append(quantity_pp)
        quantity_costs_list.append(quantity_costs)

    # Use pandas to create table
    expense_frame = pandas.DataFrame(ingredient_dict)

    # Find total costs
    total_costs = expense_frame['Price'].sum()

    # Find total costs based of quantity of items used
    total_quantity_costs = expense_frame['Cost based on quantity of items used'].sum()

    # Figures out the costs for each serving
    serving_costs = total_quantity_costs / serving_amount  

    # Currency Formatting
    add_dollars = ['Price']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    add_dollars_quantity = ['Cost based on quantity of items used']
    for item in add_dollars_quantity:
        expense_frame[item] = expense_frame[item].apply(currency)

    # Returns all the costs
    return [expense_frame, total_costs, total_quantity_costs, serving_costs]


# Main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ").lower()

# If user wants instructions, print out instructions
if want_instructions == "yes" or want_instructions == "y":
    print()
    print("--- Instructions ---")
    print()
    print("This program will figure out the total cost of store ingredients, total cost of quantity used in the recipe, cost per serving")
    print("It will also create a table of all the data used")
    print("Enter the recipe's name, serving amounts, ingredients, quantity, quantity that was included in the packet / box, units, and price")
    print("Enter XXX to exit loops")
    print()

# Ask user for the name of their recipe and the amount of servings that they will be using
recipe_name = not_blank("Whats the name of your recipe? ", "The product name can't be blank. ")
serving_amount = num_check("How many servings? ", "The amount must be a whole number more than zero", int)

# Get information from get expenses function
variable_expenses = get_expenses("variable")
expense_frame = variable_expenses[0]
total_costs = variable_expenses[1]
total_quantity_costs = variable_expenses[2]
serving_costs = variable_expenses[3]
print()

# Turn variable items into strings to print out in the file
recipe_name_string = F"Recipe Name: {recipe_name}\nServings: {serving_amount}"
panda_frame_string = F"*** Recipe Table ***\n{expense_frame}"
cost_string = F"Total costs of items: ${total_costs:.2f}\nCosts based on quantity of items used: ${total_quantity_costs:.2f}\nCost per serving (based on quantity of items used): ${serving_costs:.2f}"

# Printing area
print()
print(recipe_name_string)
print()
print(panda_frame_string)
print()
print(cost_string)
print()

# Write to file
to_write = [recipe_name_string, panda_frame_string, cost_string]

# Create file to hold data
file_name = F"{recipe_name}.txt"
text_file = open(file_name, "w+")

# Add all strings to the text file
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close file
text_file.close()