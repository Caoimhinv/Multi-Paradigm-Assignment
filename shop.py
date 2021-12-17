# importing necessary libraries
from dataclasses import dataclass, field
from typing import List
import csv

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

def checkProductStock(n, order):
    for item in s.stock:
        name = item.product.name
        if (name, n) == 0:
            if item.quantity >= order:
                item.quantity = item.quantity - order
            else:
                order = item.quantity
                item.quantity = 0
        # print(order)
        # print(type(order))
        return order

def findProductPrice(s,c):
    for item in c.shoppingList:
        for prod in s.stock:
            if item.product.name==prod.product.name:
                item.product.price==prod.product.price

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

# Live mode??????
# def liveMode():
    # pass

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
    print("/////////////////////")
    print("Please select from the following: ")
    print("1 - Show shop's current stock and float")
    print("2 - Shop with Caoimhin's shopping list")
    print("3 - Shop with PJs's shopping list")
    print("4 - Shop with JimBob's shopping list")
    print("5 - Shop in Live Mode")
    print("0 - Exit")



def shopMenu(s):
    s = createAndStockShop()
    c = Customer()
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
            # liveMode()
            mainMenu()

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
