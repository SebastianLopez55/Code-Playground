"""
Implement parent class Vehicle and use Polymorphism.
"""


class Vehicle:
    def __init__(self):
        pass

    def make_noise(self, power):

        for _ in range(power):
            print("Vroom...")


class Car(Vehicle):
    def __init__(self):
        pass

    """
    In Python, method overriding works differently compared to Java.
    In Python, when you override a method in a subclass, it completely
    replaces the method in the parent class. This means that if the method
    signatures don't match exactly, you cannot call the parent class
    method using the same method name with a different number of arguments.

    However, you can explicitly call the parent class method using super().
    Here is an example of how you can achieve this:
    """

    def make_noise(self, power, cylinder_diameter=None):
        if cylinder_diameter is None:
            super().make_noise(power)
        else:
            print(
                f"This is the Car noise with power {power} and diameter {cylinder_diameter} Vrooooo"
            )


print()
vehicle1 = Vehicle()
vehicle1.make_noise(2)

print()
car1 = Car()
car1.make_noise(3)

print()
car1.make_noise(3, 2)
