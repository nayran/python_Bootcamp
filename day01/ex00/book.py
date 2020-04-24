import datetime
from recipe import Recipe


def error(x):
    raise ValueError(x)


class Book:
    def __init__(self, name):
        if not (name or isinstance(name, str)):
            error("Book must have a name")
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {
                "starter": [],
                "lunch": [],
                "dessert": []
                }

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            error("Not a Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()

    def get_recipe_by_name(self, name):
        x = 0
        for i in self.recipes_list["starter"]:
            if self.recipes_list["starter"][x].name == name:
                print(str(i))
                return
            x += 1
        x = 0
        for i in self.recipes_list["lunch"]:
            if self.recipes_list["lunch"][x].name == name:
                print(str(i))
                return
        x = 0
        for i in self.recipes_list["dessert"]:
            if self.recipes_list["dessert"][x].name == name:
                print(str(i))
                return

    def get_recipe_by_type(self, recipe_type):
        for i in self.recipes_list[recipe_type]:
            print(i.name)
