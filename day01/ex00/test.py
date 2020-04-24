from book import Book
from recipe import Recipe


r = Recipe(
        name='Ice cream',
        cooking_lvl=2,
        cooking_time=30,
        ingredients=['milk', "chocolate"],
        recipe_type="dessert",
        description="description here"
        )
b = Book(
        name="Book"
        )
print("Add recipe:" + str(r))
b.add_recipe(r)
print("Get recipe by name 'Cake':")
b.get_recipe_by_name("Cake")
print("Get recipe by name 'Ice cream':")
b.get_recipe_by_name("Ice cream")
print("Get recipe by type 'dessert':")
b.get_recipe_by_type("dessert")
print("Get recipe by type 'starter':")
b.get_recipe_by_type("starter")
