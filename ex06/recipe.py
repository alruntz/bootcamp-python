m_cookbook = {
    'sandwich' : {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10,
        },
    'cake' : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : 60,
        },
    'salad' : {
        'ingredients' : ['avocado', 'arugula', 'tomatoes ', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : 15,
        }
    }

def print_recip(recipName):
    if recipName in m_cookbook.keys():
        print(m_cookbook[recipName])
        return True
    else:
        return False

def print_allRecipNames():
    for k in m_cookbook:
        print (k)

def remove_recip(recipName):
    if recipName in m_cookbook.keys():
        m_cookbook.pop(recipName, None)
        return True
    else:
        return False

def add_recip(recipName, ingredients, meal, prepTime):
    if recipName not in m_cookbook.keys():
        m_cookbook[recipName] = {
            'ingredients' : ingredients,
            'meal' : meal,
            'prep_time' : prepTime
            }
        return True
    else:
        return False

def main():

    run = True

    while (run is True):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")

        res = input()
    
        if res is '1':       
            recipName = input("Set name of recip\n")
            ingredients = input("Set ingredients (['a', 'b', 'c'])\n")
            meal = input("Set meal\n")
            prepTime = input("Set preparation time (minutes)\n")

            if (recipName is None or ingredients is None or meal is None or
               recipName is '' or ingredients is '' or meal is '' or prepTime is '' or
               prepTime.isdigit is False):
                print("Error !")
            else:
                try:
                    if add_recip(recipName, ingredients, meal, prepTime) is True:
                        print("Recip creation success")
                    else:
                        print("Error")
                except:
                    print("Error !")

        elif res is '2':
            recipName = input('Name of recip:\n')
            if remove_recip(recipName) is True:
                print("Success")
            else:
                print("Error")
    
        elif res is '3':
            recipName = input('Name of recip:\n')
            if print_recip(recipName) is None:
                print("Error")

        elif res is '4':
            print_allRecipNames()

        elif res is '5':
            run = False


if __name__ == "__main__":
    main()