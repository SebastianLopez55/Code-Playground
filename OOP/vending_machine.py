# Imagine how a vending machine works. You put money in, you punch in a code, an item is dispensed.
# I want you to model a vending machine as a class. To get you started, I will give you a few method signatures:


# let vm = new VendingMachine(....);
# vm.addMoney(1);
# vm.buyItem('A5');


class VendingMachine:

    def __init__(self):
        self.vending_items = {}
        self.balance = 0.0  # Current money in the machine

    def add_money(self, amount):
        if amount < 1:
            print("Can't add negative funds.")
        else:
            self.balance += amount
            print(f"${amount} added. Total money: ${self.balance}")

    def buy_item(self, code):
        if code not in self.vending_items:
            print(f"Item {code} not found.")
            return
        item = self.vending_items[code]
        if self.balance < item["price"]:
            print(
                f"Not enough money. Item price: ${item['price']}. Current balance: ${round(self.balance, 3)}"
            )
        else:
            self.balance -= item["price"]
            item["quantity"] -= 1
            print(
                f"Item {item['name']} dispensed. Remaining quantity: {item['quantity']}. Change: ${self.balance}"
            )
            if item["quantity"] == 0:
                del self.vending_items[code]

    def add_item(self, code, name, price, quantity):
        if code in self.vending_items:
            self.vending_items[code]["quantity"] += quantity
        else:
            self.vending_items[code] = {
                "name": name,
                "price": price,
                "quantity": quantity,
            }
        print(
            f"Item {name} added with code {code}, price ${price}, quantity {quantity}."
        )


vm = VendingMachine()
vm.add_item("A5", "Hershey's", 2.2, 10)
vm.add_money(6)
vm.buy_item("A5")
vm.buy_item("A5")
vm.buy_item("A5")
