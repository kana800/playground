'''
This program can create recipes and the user can sort them out 'event' or 'ingredients'
'''



class Recipe:
    '''
    '''
    recipe = {}
    def __init__(self,name,category,ingredient_list):
        self.name = name
        self.category = category
        self.ingredient_list = ingredient_list
        self.recipe[name] = [category,ingredient_list]

    def __str__(self):
        string ="name = {}\n \tcategory = {}\n\tingredients = {}".format(self.name,self.category,self.ingredients)
        return string

    @property
    def ingredients(self):
        a = ""
        for i in self.ingredient_list:
            a += f"{i[0]} of {i[1]} ,"
        return a[:-1]

class Recipe_Manager:

    by_category = {}
    def __init__(self):
        self.by_category['dessert'] = []
        self.by_category['main dishes'] = []
        self.by_category['beef recipes'] = []

    def add_recipe(self,recipe):
        try:
            self.by_category[recipe.category].append(recipe)
        except KeyError:
            self.by_category[recipe.category] = [recipe]

    def categories(self,category):
        try:
            for r in self.by_category[category]:
                print(r)
        except:
            raise NotImplementedError

if __name__ == "__main__":

    # created some random recipes
    r1 = Recipe('pie','dessert',[[1,'pumpkin puree'],[250,'sugar'],[100,'cream']])
    r2 = Recipe('cake','dessert',[[1,'chocolate'],[250,'sugar'],[100,'cream']])
    r3 = Recipe('brownies','dessert',[[10,'oreos'],[250,'sugar'],[100,'cream']])

    # created a recipe manager
    r = Recipe_Manager()

    # adding recipes
    r.add_recipe(r1)
    r.add_recipe(r2)
    r.add_recipe(r3)

    # displaying the recipes by_category

    r.categories('dessert')
