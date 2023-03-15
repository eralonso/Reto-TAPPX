class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self._name = name
        self._cooking_lvl = cooking_lvl
        self._cooking_time = cooking_time
        self._ingredients = ingredients
        self._description = description
        self._recipe_type = recipe_type
    
    @property
    def name(self):
        return (self._name)

    @name.setter
    def name(self, name):
        if (isinstance(name, str) == False or str == ""):
            print("Error: The name must be string and not empty")
            exit(1)
        else:
            self._name = name

    @property
    def cooking_lvl(self):
        return (self._cooking_lvl)

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if (isinstance(cooking_lvl, int) == False):
            print("Error: The cooking level must be int")
            exit(1)
        if (cooking_lvl not in range(1, 6)):
            print("Error: The cooking level not is in range 1 - 5")
            exit(1)
        else:
            self._cooking_lvl = cooking_lvl

    @property
    def cooking_time(self):
        return (self._cooking_time)

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if (isinstance(cooking_time, int) == False):
            print("Error: The cooking time must be int")
            exit(1)
        else:
            self._cooking_time = cooking_time

    @property
    def ingredients(self):
        return (self._ingredients)

    @ingredients.setter
    def ingredients(self, ingredients):
        if (isinstance(ingredients, list) == False or len(ingredients) == 0):
            print("Error: The ingredients must be list and not empty")
            exit(1)
        for ing in ingredients:
            if (isinstance(ing, str) == False or ing == ""):
                print("Error: The ingredients name must be string and not empty")
                exit(1)
        else:
            self._ingredients = ingredients

    @property
    def description(self):
        return (self._description)

    @description.setter
    def description(self, description):
        if (isinstance(description, str) == False):
            print("Error: The description must be string")
            exit(1)
        else:
            self._description = description

    @property
    def recipe_type(self):
        return (self._recipe_type)

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        types = ("starter", "lunch", "dessert")
        if (isinstance(recipe_type, str) == False):
            print("Error: The recipe type must be string and not empty")
            exit(1)
        if (types.count(recipe_type) == 0):
            print(f"Error: The recipe type must be {types}")
            exit(1)
        else:
            self._recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt += f"Name: {self.name}"
        txt += f"\nCooking level: {self.cooking_lvl}"
        txt += f"\nCooking time: {self.cooking_time}"
        txt += f"\nIngredients: {self.ingredients}"
        if (self.description != ""):
            txt += f"\nDescription: {self.description}"
        txt += f"\nRecipe type: {self.recipe_type}"
        return (txt)


