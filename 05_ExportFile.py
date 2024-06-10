import pandas

# Frames and content for export
recipe_name_dict = {
    "Item": ["Yeast", "Flour", "Olive oil", "Tomato paste", "Cheese", "Peperoni", "Chicken", "Capsicun"],
    "Quantity": [2.25, 1.5, 1, 1, 5, 0.25, 0.75, 0.5,],
    "Units": ["Teaspoons", "Cups", "Tablespoons", "Tablespoons", "Ounces", "Cups", "Cups", "Cups"],
    "Price": [4.90, 2.4, 9.45, 1.6, 8.5, 3.8, 8.8, 3.5],
    "Quantity per packet / box": [34, 18, 33.82, 12, 13, 0.5, 4, 1.5]

}

variable_frame = pandas.DataFrame(recipe_name_dict)

# Change frames to string
variable_txt = pandas.DataFrame.to_string(variable_frame)

# Headings to write
recipe_name = "Chicken Pizza"
recipe_name_string = "Recipe name: Chicken Pizza\nServings: 8"
total_price = "Total variable cost of items: $42.95\nCosts based on quantity of items used: $8.92\nCosts per serve: $1.12"

# Makes list of everything needed
to_write = [recipe_name_string, variable_txt, total_price]

# Write to file
# Create file to hold data
file_name = F"{recipe_name}.txt"
text_file = open(file_name, "w+")

# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close file
text_file.close()

# Printing
for item in to_write:
    print(item)
    print()