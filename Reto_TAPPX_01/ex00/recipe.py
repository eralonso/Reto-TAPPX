class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        types = ("entrante", "comida", "postre")
        if (isinstance(name, str) == False or str == ""):
            print("Error: The name must be string and not empty")
            exit(1)
        if (isinstance(cooking_lvl, int) == False):
            print("Error: The cooking_level must be int")
            exit(1)
        if (isinstance(cooking_time, int) == False):
            print("Error: The cooking_time must be int")
            exit(1)
        if (isinstance(ingredients, list) == False or len(ingredients) == 0):
            print("Error: The ingredients must be list and not empty")
            exit(1)
        if (isinstance(description, str) == False):
            print("Error: The description must be string and not empty")
            exit(1)
        if (isinstance(recipe_type, str) == False):
            print("Error: The recipe type must be string and not empty")
            exit(1)
        if (cooking_lvl not in range(1, 6)):
            print("Error: The cooking level not is in range 1 - 5")
            exit(1)
        if (recipe_type not in types):
            print(f"Error: The recipe type must be {types}")
            exit(1)
        for ing in ingredients:
            if (isinstance(ing, str) == False or ing == ""):
                print("Error: The ingredients name must be string and not empty")
                exit(1)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        txt = ""
        txt += f"\nName: {self.name}"
        txt += f"\nCooking level: {self.cooking_lvl}"
        txt += f"\nCooking time: {self.cooking_time}"
        txt += f"\nIngredients: {self.ingredients}"
        if (self.description != ""):
            txt += f"\nDescription: {self.description}"
        txt += f"\nRecipe type: {self.recipe_type}"
        return (txt)

