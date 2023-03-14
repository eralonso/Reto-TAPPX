def isinteger(num):
    if (num[0] == '+' or num[0] == '-'):
        return num[1::].isdigit()
    else:
        return num.isdigit()

def print_recipe(cookbook):
    name = input("Please enter a recipe name to get its details:\n>>  ")
    if ((tuple(cookbook.keys())).count(name) == 0):
        print("This recipe is not in cookbook")
    else:
        recipe = cookbook[name]
        print(f"\nRecipe for {name}:")
        print(f"  Ingredients list: [{str(recipe['ingredients'])[1:-1:]}]")
        print(f"  To be eaten for {recipe['meal']}.")
        print(f"  Takes {recipe['prep_time']} minutes of cooking.")
    return

def print_cookbook(cookbook):
    print(str({*cookbook.keys()})[1:-1:].replace('\'', ''))
    return

def delete_recipe(cookbook):
    recipe = input("Please enter a recipe name to delete:\n>>  ")
    if (recipe in cookbook.keys() == False):
        print("This recipe is not in cookbook")
    else:
        del cookbook[recipe]
    return

def add_recipe(
            cookbook, name,
            ingredients, meal,
            time):
    cookbook[name] = {
                        "ingredients":ingredients,
                        "meal":meal,
                        "prep_time":time
                     }
    return

def op_add_recipe(cookbook):
    name = input("Enter a name:\n>> ")
    while (isinteger(name) == True or list(cookbook.keys()).count(name) != 0):
        if (list(cookbook.keys()).count(name) != 0):
            print("This recipe is in cookbook")
        else:
            print("This name of recipe is invalid")
        name = input("Please enter a valid name:\n>> ")
    ingredients = set()
    ingredient = "Prueba"
    while (ingredient != ""):
        ingredient = input("Enter ingredients:\n>> ")
        while (ingredient != "" and isinteger(ingredient) == True):
            print("This ingredient is invalid")
            ingredient = input("Please enter a valid ingredient:\n>> ")
        ingredients.add(ingredient)
    meal = input("Enter a meal type:\n>> ")
    while (isinteger(meal) == True):
        print("This meal type is invalid")
        meal = input("Please enter a valid meal type:\n>> ")
    time = input("Enter a preparation time:\n>> ")
    while (time.isdigit() == False):
        time = input("The time only accept integers value\nPlease enter a valid preparation time\n>>  ")
    add_recipe(cookbook, name, ingredients, meal, time)

def init_cookbook(cookbook):
    add_recipe(cookbook, "bocadillo", {"jamon", "pan", "queso", "tomate"}, "almuerzo", 10)
    add_recipe(cookbook, "tarta", {"harina", "azucar", "huevos"}, "postre", 60)
    add_recipe(cookbook, "ensalada de aguacate", {"rucula", "tomates", "espinacas"}, "almuerzo", 15)
    return

def print_options():
    print("List of available option:")
    print("  1: Add a recipe\n  2: Delete a recipe\n  3: Print a recipe\n  4: Print the cookbook\n  5: Quit")

cookbook = dict()
init_cookbook(cookbook)
print("Welcome to the Python Cookbook !")
print_options()
options = (1, 2, 3, 4, 5)
finish = False
while (finish == False):
    option = input("\nPlease select an option:\n>>  ")
    print("")
    if (option.isdigit() == False or options.count(int(option)) == 0):
        print("Sorry, this option does not exist.")
        print_options()
        continue
    option = int(option)
    if (option == 1):
        op_add_recipe(cookbook)
    elif (option == 2):
        delete_recipe(cookbook)
    elif (option == 3):
        print_recipe(cookbook)
    elif (option == 4):
        print_cookbook(cookbook)
    elif (option == 5):
        print("Cookbook closed. Goodbye !")
        finish = True
      
exit(0)
