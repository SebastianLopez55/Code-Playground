"""
+---------------------+
|     CoffeeMachine   |
+---------------------+
| - water_level: int  |
| - coffee_beans: int |
| - milk: int         |
| - cups: int         |
+---------------------+
| + add_water(amount: int): void        |
| + add_coffee_beans(amount: int): void |
| + add_milk(amount: int): void         |
| + add_cups(cups: int): void           |
| + check_ingredients(): str            |
| + brew_coffee(type: CoffeeType): str  |
+---------------------+

+---------------------+
|    CoffeeType       |
+---------------------+
| + ESPRESSO: str     |
| + LATTE: str        |
+---------------------+

"""


class CoffeeType:
    ESPRESSO = "Espresso"
    LATTE = "Latte"


class CoffeeMachine:
    def __init__(self):
        self.water_level = 0
        self.coffee_beans = 0
        self.milk = 0
        self.cups = 0

    def add_water(self, amount):
        self.water_level += amount
        print(f"Added {amount}ml of water.")

    def add_coffee_beans(self, amount):
        self.coffee_beans += amount
        print(f"Added {amount}g of coffee beans.")

    def add_milk(self, amount):
        self.milk += amount
        print(f"Added {amount}ml of milk.")

    def add_cups(self, cups):
        self.cups += cups
        print(f"Added {cups} cups.")

    def check_ingredients(self):
        return (
            f"Water Level: {self.water_level}ml, "
            f"Coffee Beans: {self.coffee_beans}g, "
            f"Milk: {self.milk}ml, "
            f"Cups: {self.cups}"
        )

    def brew_coffee(self, coffee_type):
        if coffee_type == CoffeeType.ESPRESSO:
            if self.water_level >= 50 and self.coffee_beans >= 18 and self.cups >= 1:
                self.water_level -= 50
                self.coffee_beans -= 18
                self.cups -= 1
                print(f"Brewing {coffee_type} ...")
                return "Serving Espresso"
            else:
                print("Not enough ingredients for Espresso")
                print(self.check_ingredients())

        elif coffee_type == CoffeeType.LATTE:
            if (
                self.water_level >= 200
                and self.coffee_beans >= 18
                and self.milk >= 150
                and self.cups >= 1
            ):
                self.water_level -= 200
                self.coffee_beans -= 18
                self.milk -= 150
                self.cups -= 1
                print(f"Brewing {coffee_type} ...")
                return "Serving Latte"
            else:
                print("Not enough ingredients for Latte")
                print(self.check_ingredients())


# Example usage:
coffee_machine = CoffeeMachine()
coffee_machine.add_water(1000)
coffee_machine.add_coffee_beans(100)
coffee_machine.add_milk(500)
coffee_machine.add_cups(10)

print(coffee_machine.check_ingredients())
print(coffee_machine.brew_coffee(CoffeeType.ESPRESSO))  # Serving Espresso
print(coffee_machine.check_ingredients())
print(coffee_machine.brew_coffee(CoffeeType.LATTE))  # Serving Latte
print(coffee_machine.check_ingredients())
