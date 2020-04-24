def error(x):
    raise ValueError(x)


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = self.h_name(name)
        self.cooking_lvl = self.h_ckglvl(cooking_lvl)
        self.cooking_time = self.h_ckgtime(cooking_time)
        self.ingredients = self.h_ingredients(ingredients)
        self.recipe_type = self.h_rcptype(recipe_type)
        if description:
            self.description = self.h_description(description)

    def __str__(self):
        x = "\n" + self.h_name(self.name).upper()
        x += "\nLevel: " + str(self.h_ckglvl(self.cooking_lvl)) + "\n"
        x += "Time: " + str(self.h_ckgtime(self.cooking_time)) + "\n"
        y = ""
        i = 0
        while(i < len(self.h_ingredients(self.ingredients))):
            y += '{}, '.format(self.ingredients[i])
            i += 1
        x += "Ingredients: " + y + "\n"
        x += "Type: " + self.h_rcptype(self.recipe_type) + "\n"
        if self.description:
            x += "Description: " + self.h_description(self.description) + "\n"
        return x

    def h_name(self, name):
        if not isinstance(name, str):
            error("You\'re missing recipe\'s name")
        self.name = name
        return(self.name)

    def h_ckglvl(self, cooking_lvl):
        if not isinstance(cooking_lvl, int):
            error("Cooking level must be an integer")
        elif not cooking_lvl >= 1 and cooking_lvl <= 5:
            error("Cooking level must be between 1 and 5")
        return(cooking_lvl)

    def h_ckgtime(self, cooking_time):
        if not isinstance(cooking_time, int):
            error("Cooking time must be an integer")
        elif not cooking_time >= 0:
            error("Cooking time must be positive")
        return(cooking_time)

    def h_ingredients(self, ingredients):
        if not ingredients:
            error("Ingredients can't be empty")
        while("" in ingredients):
            ingredients.remove("")
        if not ingredients:
            error("Ingredients can't be empty")
        for i in ingredients:
            if not isinstance(i, str):
                x = i + "is not a String"
                error(x)
        return(ingredients)

    def h_description(self, description):
        if not isinstance(description, str):
            error("Description must be a str")
        return(description)

    def h_rcptype(self, recipe_type):
        if not isinstance(recipe_type, str):
            error("Recipe type must be a str")
        elif not(recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            error("Recipe type must be starter, lunch or dessert")
        return(recipe_type)
