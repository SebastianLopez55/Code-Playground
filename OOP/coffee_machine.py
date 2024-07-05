"""
+---------------------+
|     CoffeeMachine   |
+---------------------+
| - waterLevel: int   |
| - coffeeBeans: int  |
| - milk: int         |
| - cups: int         |
+---------------------+
| + addWater(amount: int): void       |
| + addCoffeeBeans(amount: int): void |
| + addMilk(amount: int): void        |
| + addCups(amount: int): void        |
| + checkIngredients(): str           |
| + brewCoffee(type: CoffeeType): str |
+---------------------+

+---------------------+
|    CoffeeType       |
+---------------------+
| + ESPRESSO          |
| + LATTE             |
| + CAPPUCCINO        |
| + BLACK             |
+---------------------+

"""


class CoffeeType:
    ESPRESSO = "Espresso"


class CoffeeMachine:
    def __init__(self, water_level, coffee_beans, milk, cups):
        self.water_level = water_level
        self.coffee_beans = coffee_beans
        self.milk = milk
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount
        print(f"Added {amount}ml of water.")

    def add_coffee_beans(self, amount):
        self.coffee_beans += amount
        print(f"Added {amount}g of coffee beans.")

    def add_milk(self, amount):
        self.milk += amount
        print(f"Added {amount}ml of milk.")

    def add_cups(self):
        pass

    def check_ingredients(self):
        pass

    def brew_coffee(self):
        pass
