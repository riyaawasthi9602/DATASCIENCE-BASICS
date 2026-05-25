from abc import ABC, abstractmethod


# Abstract Base Class
class Coffee(ABC):

    @abstractmethod
    def recipe(self):
        pass

    @abstractmethod
    def art(self):
        pass


# Latte Class
class Latte(Coffee):

    def recipe(self):
        print("\nRecipe : Milk + Espresso + Foam")

    def art(self):
        print(r"""
############################
###### LATTE ☕ ########
############################
 ( (
  ) )
 ........
 | |]
 \   /
  `---'
""")


# Mocha Class
class Mocha(Coffee):

    def recipe(self):
        print("\nRecipe : Chocolate + Milk + Espresso")

    def art(self):
        print(r"""
############################
###### MOCHA ☕ ########
############################
 {~~~~}
 |    |
 |    |
 |____|
""")


# Mazza Class
class Mazza(Coffee):

    def recipe(self):
        print("\nRecipe : Cold Coffee + Chocolate + Ice")

    def art(self):
        print(r"""
############################
###### MAZZA 🥤 ########
############################
  ______
 |      |
 |MAZZA |
 |______|
""")


# Coffee Machine Class
class CoffeeMachine:

    def serve(self, coffee):
        coffee.art()
        coffee.recipe()
        print("\nYour drink is ready!\n")


# Main Program
machine = CoffeeMachine()

while True:

    print("====== COFFEE MACHINE ======")
    print("1 -> Latte")
    print("2 -> Mocha")
    print("3 -> Mazza")
    print("4 -> Exit")

    choice = input("Enter your choice : ").strip()

    if choice == "1":
        machine.serve(Latte())

    elif choice == "2":
        machine.serve(Mocha())

    elif choice == "3":
        machine.serve(Mazza())

    elif choice == "4":
        print("\nCoffee Machine Closed")
        break

    else:
        print("\nPlease enter a valid choice (1-4)\n")