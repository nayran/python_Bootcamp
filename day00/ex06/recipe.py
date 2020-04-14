sandwich = {
        'ingredients': 'ham, bread, cheese, tomatoes',
        'meal': 'lunch',
        'prep_time': 10,
        }
cake = {
        'ingredients': 'flour, sugar, eggs',
        'meal': 'dessert',
        'prep_time': 60,
        }
salad = {
        'ingredients': 'avocado, arugula, tomatoes, spinach',
        'meal': 'lunch',
        'prep_time': 15,
        }
cookbook = {
        'sandwich': sandwich,
        'cake': cake,
        'salad': salad,
        }


def recipe_print(recipe_name):
    if cookbook.get(recipe_name) is None:
        print("This isn't a recipe")
    else:
        print("\n" + recipe_name.upper())
        print("Ingredients: " + cookbook[recipe_name]['ingredients'])
        print("It's a " + cookbook[recipe_name]['meal'])
        print("Prep time: %s minutes" % cookbook[recipe_name]['prep_time'])


def recipe_add(recipe_name, ingredients, meal, prep_time):
    x = {recipe_name: {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time}}
    cookbook.update(x)


def recipe_rm(recipe_name):
    cookbook.pop(recipe_name)


def cookbook_print():
    x = [*cookbook]
    i = 0
    while (i < len(cookbook.keys())):
        model = '{}'.format(x[i])
        print(model)
        i += 1


opcao = 0
while (opcao != '5'):
    print("1 - Print recipe")
    print("2 - Add recipe")
    print("3 - Delete recipe")
    print("4 - Print cookbook")
    print("5 - Quit")
    opcao = input()
    if(opcao == '1'):
        recipe_name = input("Recipe name: ")
        recipe_print(recipe_name)
        input("Enter to continue")
        print("\n")
    elif(opcao == '2'):
        recipe_name = input("Recipe name: ")
        ingredients = input("Ingredients: ")
        meal = input("Meal: ")
        prep_time = input("Preparation time: ")
        recipe_add(recipe_name, ingredients, meal, prep_time)
        input("Enter to continue")
        print("\n")
    elif(opcao == '3'):
        recipe_name = input("Recipe name: ")
        recipe_rm(recipe_name)
        input("Enter to continue")
        print("\n")
    elif(opcao == '4'):
        cookbook_print()
        input("Enter to continue")
        print("\n")
