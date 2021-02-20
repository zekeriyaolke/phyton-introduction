class RecipeItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Recipe:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def cook(self):
        recipeItems = [f"{i.name}({i.quantity})" for i in self.items]
        print(f"{self.name} pişiyor\n Kullanılan malzemeler:{recipeItems} \n")


class Hamburger(Recipe):
    def __init__(self):
        super(Hamburger, self).__init__("Hamburger", [RecipeItem("Kıyma", 150),
                                                      RecipeItem("Soğan", 10),
                                                      RecipeItem("Ekmek", 1),
                                                      RecipeItem("Turşu", 10)])

    def cook(self):
        super(Hamburger, self).cook()


class Pizza(Recipe):
    def __init__(self):
        super(Pizza, self).__init__("Pizza", [RecipeItem("Salam", 50),
                                              RecipeItem("Sosis", 50),
                                              RecipeItem("Mantar", 25),
                                              RecipeItem("Biber", 25),
                                              RecipeItem("Hamur", 100)])

    def cook(self):
        super(Pizza, self).cook()


class Kebap(Recipe):
    def __init__(self):
        super(Kebap, self).__init__("Kebap", [RecipeItem("Kıyma", 150),
                                              RecipeItem("Biber", 25),
                                              RecipeItem("Soğan", 50),
                                              RecipeItem("Domates", 50),
                                              RecipeItem("Marul", 25),
                                              RecipeItem("Biber", 25),
                                              RecipeItem("Pide", 1)])

    def cook(self):
        super(Kebap, self).cook()


hamburger = Hamburger()
hamburger.cook()

pizza = Pizza()
pizza.cook()

kebap = Kebap()
kebap.cook()
