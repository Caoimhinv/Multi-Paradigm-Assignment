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

# function to print product  
def printProduct(p):
    print("---------------\n")
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: €{p.price}')
    print("- - - - - - - - -\n")

def createAndStockShop():
    s = Shop()
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            print(ps)
    return s

def printShop(s):
    print("//////////\n")
    print("Stock list\n")
    print("//////////\n")
    print(f'Shop has a float of €{s.cash}')
    for item in s.stock:
        printProduct(item.product)
        print(f'The shop has {item.quantity} in stock')
    
def checkProductStock():
    pass

def findProductPrice():
    pass

def createCustomer(file_path):
    c = Customer()
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
def liveMode():
    pass

def printCustomer(c):
    print("////////////////////////\n")
    print(f"{c.name}'s shopping list\n")
    print("////////////////////////\n")
    print(f"Budget: €{c.budget}")
    
    for item in c.shopping_list:
        printProduct(item.product)
        
        print(f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price
        print(f'The cost to {c.name} will be €{cost}')

def mainMenu():
    print("/////////////////////")
    print("WELCOME TO THE C SHOP")
    print("/////////////////////")
	print("Please select from the following:")
	print("1 - Show shop's current stock and float") 
	print("2 - Shop with Caoimhin's shopping list") 
    print("3 - Shop with PJs's shopping list")
    print("4 - Shop with JimBob's shopping list") 
	print("5 - Shop in Live Mode")
	print("0 - Exit")

def mainMenu2(s):
    mainMenu()
    while True:
        choice = input("Please make a selection: ")

        if (choice == "1"):
            printShop(s)
            mainMenu()

        elif (choice == "2"):
            customer1 = createCustomer("customer1.csv")
            mainMenu()

        elif (choice == "3"):
            customer2 = createCustomer("customer2.csv")
            mainMenu()

        elif (choice == "4"):
            customer3 = createCustomer("customer3.csv")
            mainMenu()

        elif (choice == "5"):
            print("\n////////////////////////////////")
			print("\nYou are now entering our LIVE SHOPPING MODE!\n")
            print("////////////////////////////////\n")
            liveMode()
            mainMenu()

        elif (choice == "0"):           
			print(f"Bye {customer.name}! Thank's for your custom!\nCome again soon!")
            break

        else:
            print("Incorrect Selection - please try again")
            mainMenu()

# s = createAndStockShop()
# printShop(s)

# c = createCustomer("customer.csv")
# printCustomer(c)
def main():
    newShop = createAndStockShop()
    print(newShop)
    mainMenu2(newShop)

if __name__ == "__main__":
    main()
