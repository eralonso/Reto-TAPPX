from recipe import Recipe
from book import Book

r = Recipe("Patata", 1, 15, ["a"], "", "entrante")
b = Book("Libro")
r.recipe_type = "starter"
b.add_recipe(r)
b.get_recipe_by_name("Patata")
