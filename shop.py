# importing necessary libraries
from dataclasses import dataclass, field
from typing import List
import csv
import math

# defining dataclasses for elements required in the shop
@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass
class ProductStock:
    product: Product
    quantity: int

@dataclass
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shoppingList: List[ProductStock] = field(default_factory=list)

# global variables
c = Customer()
s = Shop()

# function to print product
def printProduct(p):
    print("---------------")
    print(f"PRODUCT NAME: {p.name}\nPRODUCT PRICE: €{p.price:.2f}")
    print("- - - - - - - - -")

# reading in csv file
def createAndStockShop():
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            # print(ps)
    return s

def readCustomer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name)
            ps = ProductStock(p, quantity)
            c.shoppingList.append(ps)
        return c 

# function to print shop stock
def printShop(s):
    print("\n//////////")
    print("Stock list")
    print("//////////")
    print(f"Shop has a float of €{s.cash:.2f}")
    for item in s.stock:
        iq = int(item.quantity)
        printProduct(item.product)
        print(f"The shop has {iq} in stock")
        print("---------------")

def checkProductStock(n,q):
    for item in s.stock:
        if n == item.product.name:
            if q <= item.quantity:
                return q
            elif q > item.quantity:
                q = int(item.quantity)
                print(f"We don't have that many in stock. We only have {q}")
                return q
        else:
            print(f"Sorry, we don't stock {n}!")

def createCustomer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name)
            ps = ProductStock(p, quantity)
            c.shoppingList.append(ps)
        return c

# Live mode
def liveMode():
    budget = float(input("What is your budget? \n"))
    totalBill = 0
    print("\n//////////////////////")
    print("Welcome to the C shop LIVE SHOPPING MODE!")
    print("//////////////////////\n")
    while True:
        print(f"Your current budget is €{budget:.2f}.\n\nPlease select what you would like to buy from the list below:\n")
        for prod in s.stock:
            print(f"{s.stock.index(prod) + 1} - {prod.product.name} @ €{prod.product.price:.2f} each")
        print("**98** - finish shopping and print total bill")
        print("**99** - Exit Live Mode\n")
        choice = int(input("Please make your selection: "))
        if choice == 99:
            print("\n--------------------\n")
            print("Come again soon and have a nice day!\n")
            print("--------------------\n")
            break
        elif choice <= len(s.stock) and budget > 0:
            choice = choice - 1
            choiceName = s.stock[choice].product.name
            choicePrice = s.stock[choice].product.price
            choiceDetails = s.stock[choice].product
            quant = int(input(f"How many {choiceName} would you like to purchase? "))
            QB = checkProductStock(choiceName, quant)
            totalCost = QB * choicePrice
            # receipt = []
            # receipt.append(choiceName)
            if budget < totalCost:
                QB = budget / choicePrice
                QB1 = math.floor(QB)
                totalCost = QB1 * choicePrice
                print("You don't have the budget to complete that transaction.")
                continue
            budget -= totalCost
            totalBill += totalCost
            s.cash += totalBill
            printProduct(choiceDetails)

            print(f"QUANTITY REQUIRED: {quant}")
            print(f"QUANTITY PURCHASED: {QB}")
            print(f"TOTAL ITEM COST: €{totalCost:.2f}")
            print(f"ADJUSTED BUDGET: €{budget:.2f}")
            print(f"(ADJUSTED SHOP FLOAT: €{s.cash:.2f}")
            print(f"- - - - - - - - - - - - - -\n")
            print(f"TOTAL BILL SO FAR: €{totalBill:.2f}")   
        elif choice == 98:
            print("\n--------------------\n")
            # for i in receipt:
            #     print(i)
            # print(*receipt, sep = "\n")
            print(f"Your total bill is €{totalBill:.2f}\n")
            print("Thank you for your custom. Please come again soon!\n")
            print("--------------------\n")
            break
        elif choice < 1:
            print("Invalid number please try again: ")
        else:
            choice = input("Invalid number please try again: ")
    mainMenu()

def printCustomer(c,s):
    print("////////////////////////")
    print(f"{c.name}'s shopping list")
    print("////////////////////////\n")
    print(f"Budget: €{c.budget:.2f}")
    totalBill = 0
    for item in c.shoppingList:
        for prod in s.stock:
            if item.product.name == prod.product.name:
                shopPrice = prod.product.price
                shopQuant = int(prod.quantity)
                item.quantity = int(item.quantity)
        if item.quantity >= shopQuant:
            print("\nSorry! Can't fulfill order on this item due to insufficient stock.")
            quit()
        else:
            cost = item.quantity * shopPrice
            totalBill += cost
            c.budget -= cost
            s.cash += cost
            print("---------------")
            print(f"PRODUCT NAME: {item.product.name}")
            print(f"PRODUCT PRICE: €{shopPrice:.2f}")
            print(f"QUANTITY REQUIRED: {item.quantity}")
            # else:
            print("- - - - - - - - ")
            print(f"QUANTITY PURCHASED: {item.quantity}")
            print(f"TOTAL ITEM COST:: €{cost:.2f}")
            print("- - - - - - - - ")
            print(f"ADJUSTED BUDGET: €{c.budget:.2f}")
            print(f"(ADJUSTED SHOP FLOAT: €{s.cash:.2f})")
            print("---------------")
            print(f"TOTAL BILL SO FAR: €{totalBill:.2f}")
            print("---------------")
            shopQuant -= item.quantity
        
    print(f"TOTAL BILL: €{totalBill:.2f}\n** Thank you for your custom **\n")

    return c

def mainMenu():
    print("\n/////////////////////")
    print("WELCOME TO THE C SHOP")
    print("/////////////////////\n")
    print("Please select from the following: \n")
    print("1 - Show shop's current stock and float")
    print("2 - Shop with Caoimhin's shopping list")
    print("3 - Shop with PJs's shopping list")
    print("4 - Shop with JimBob's shopping list")
    print("5 - Shop in Live Mode")
    print("0 - Exit")
    # for i in c.shoppingList:
        # print(i)
        # print(f"{s.stock.index(prod) + 1} - {prod.product.name} @ €{prod.product.price:.2f} each")



def shopMenu(s):
    # s = createAndStockShop()
    # c = Customer()
    mainMenu()

    while True:
        choice = input("Please make a selection: ")

        if (choice == "1"):
            printShop(s)
            mainMenu()

        elif (choice == "2"):
            customer1 = createCustomer("customer1.csv")
            printCustomer(customer1,s)
            mainMenu()

        elif (choice == "3"):
            customer2 = createCustomer("customer2.csv")
            printCustomer(customer2,s)
            mainMenu()

        elif (choice == "4"):
            customer3 = createCustomer("customer3.csv")
            printCustomer(customer3,s)
            mainMenu()

        elif (choice == "5"):
            print("\n////////////////////////////////")
            print("You are now entering our LIVE SHOPPING MODE!")
            print("////////////////////////////////")
            liveMode()
            # mainMenu()

        elif (choice == "0"):
            print(f"Bye {c.name}! Thank's for your custom! Come again soon!")
            exit()

        else:
            print("Incorrect Selection - please try again")
            mainMenu()

def main():
    newShop = createAndStockShop()
    # print(newShop)
    shopMenu(newShop)

if __name__ == "__main__":
    main()
