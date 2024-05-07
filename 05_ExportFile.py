import pandas

# Frames and content for export
recipe_name_dict = {
    "Item": ["Eggs", "Flour", "Sugar", "Cinnamon"],
    "Quantity": [4, 200, 30, 15],
    "Units": ["", "grams", "grams", "grams"],
    "Price": [13.50, 5, 7.5, 12],
    "Quantity per packet / box": [6, 1000, 1500, 100]

}

variable_frame = pandas.DataFrame(recipe_name_dict)

# Change frames to string
variable_txt = pandas.DataFrame.to_string(variable_frame)

recipe_name = "Pancakes"
recipe_name_string = "Recipe name: Pancakes\nServings: 4"
total_price = "Total variable cost of items: $38\nCosts based on quantity of items used: $11.40\nCosts per serve: $2.85"

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