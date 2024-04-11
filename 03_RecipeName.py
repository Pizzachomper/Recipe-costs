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

# Get ingredients, quantity, and units. Return as a list
def get_expenses(var_fixed):
    # Set up dictionaries and list

    ingredient_list = []
    quantity_list = []
    unit_list = []

    variable_dict = {
        "Ingredient": ingredient_list,
        "Quantity": quantity_list,
        "Units": unit_list
    }

    # loop to get component, quantity, item
    # Get expenses, return list which has the data frame and sub total
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()

        # Get name, quantity, and item
        ingredient_name = not_blank("What is the ingredient name? ",
                                "The ingredient name can't be blank.")
        if ingredient_name.lower() == "xxx":
            break

        quantity = num_check("Quantity: ",
                            "The amount must be a whole number more than zero", int)
        
        units = not_blank("What are the units for the item? ",
                        "The units can't be blank")
        
        # Add item, quantity and price to lists
        ingredient_list.append(ingredient_name)
        quantity_list.append(quantity)
        unit_list.append(units)

    expense_frame = pandas.DataFrame(variable_dict)

    return [expense_frame]

# Main routine

recipe_name = not_blank("Whats the name of your recipe? ", "The product name can't be blank.")
serving_amount = num_check("How many servings? ", "The amount must be a whole number more than zero", int)

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]

# Printing area
print()
print("Recipe Name:", recipe_name)
print("Servings:", serving_amount)
print()
print(variable_frame)
print()