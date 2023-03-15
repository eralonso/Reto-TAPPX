from datetime import datetime
from recipe import Recipe

class Book:

    def __init__(self, name, recipes_list = None):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = recipes_list
    
    @property
    def name(self):
       return (self._name)

    @name.setter
    def name(self, name):
        if (isinstance(name, str) == False):
            print("AssertionError: Name of book must be string")
            exit(1)
        else:
            self._name = name

    @property
    def recipes_list(self):
        return (self._recipes_list)

    @recipes_list.setter
    def recipes_list(self, recipes_list):
        if (recipes_list is None):
            self._recipes_list = dict().fromkeys(("starter", "lunch", "dessert"))
        else:
            r_list = dict().fromkeys(("starter", "lunch", "dessert"))
            r_keys = tuple(r_list.keys())
            if (isinstance(recipes_list, dict) == False):
                print("AssertionError: Recipes list must be a dictionnary")
                exit(1)
            if (recipes_list.keys() != r_list.keys()):
                print(f"AssertionError: Dictionary must only have 3 keys: \"{r_keys[0]}\", \"{r_keys[1]}\" and \"{r_keys[2]}\"")
                exit(1)
            else:
                self._recipes_list = recipes_list

    @property
    def last_update(self):
        return (self._last_update)

    @last_update.setter
    def last_update(self, last_update):
        if (isinstance(last_update, datetime) == False):
            print("AssesrtionError: Last update must be a datetime type")
            exit(1)
        else:
            self._last_update = last_update

    @property
    def creation_date(self):
        return (self._creation_date)

    @last_update.setter
    def creation_date(self, creation_date):
        if (isinstance(creation_date, datetime) == False):
            print("AssesrtionError: Last update must be a datetime type")
            exit(1)
        else:
            self._creation_date = creation_date

    def get_recipe_by_name(self, name):
        r_types = ("starter", "lunch", "dessert")
        if (tuple(self.recipes_list.values()).count(name)):
            print("AssertionError: The name of recipe is not in recipes list")
            exit(1)
        if (self.recipes_list is None):
            self._recipes_list = dict().fromkeys(("starter", "lunch", "dessert"))
        for r_type in self.recipes_list.keys():
            if (self.recipes_list[r_type] is None):
                continue
            for r_name in self.recipes_list[r_type]:
                if (r_name.name == name):
                    if (r_name.recipe_type not in r_types):
                        print("AssertionError: Recipe type is not valid")
                        exit(1)
                    print(str(r_name))
                    return (r_name)

    def get_recipes_by_types(self, recipe_type):
        r_types = ("starter", "lunch", "dessert")
        if (recipe_type not in r_types):
            print("AssertionError: Recipe type is not valid")
            exit(1)
        return (self.recipes_list[recipe_type])

    def add_recipe(self, recipe):
        r_types = ("starter", "lunch", "dessert")
        if (isinstance(recipe, Recipe) == False):
            print("AssertionError: Argument must be a \"Recipe\"")
            exit(1)
        if (recipe.recipe_type not in r_types):
            print("AssertionError: Recipe type is not valid")
            exit(1)
        if (self.recipes_list is None):
            self._recipes_list = dict().fromkeys(("starter", "lunch", "dessert"))
        if (self.recipes_list[recipe.recipe_type] is None):
            self.recipes_list[recipe.recipe_type] = list()
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

