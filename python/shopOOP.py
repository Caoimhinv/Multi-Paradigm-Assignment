import csv
import math

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'---------------\nPRODUCT NAME: {self.name}\nPRODUCT PRICE: €{self.price:.2f}\n- - - - - - - -'

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name
    
    def itemPrice(self):
        return self.product.price
        
    def cost(self):
        return self.itemPrice() * self.quantity
        
    def __repr__(self):
        return f"{self.product}\nQUANTITY REQUIRED: {int(self.quantity)}\n"

class Customer:

    def __init__(self, path):
        self.shoppingList = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shoppingList.append(ps) 
                
    def printCustomer(self):
        stock = shop.stock
        for i in stock:
            shop_item_name = i.product.name
            if shop_item_name == self.shoppingList: 
                return i
        
    def __repr__(self):
        print('')
        formatFloat = "{:.2f}".format(self.budget)
        str = f"\n////////////////////////\n{self.name}'s shopping list\n////////////////////////\n\n"
        str += f"BUDGET: €{formatFloat}"
        totalBill = 0
        for item in self.shoppingList:
            for prod in shop.stock:
                if item.product.name == prod.name():
                    choiceName = item.product.name
                    item.product.price = prod.product.price
                    shopPrice = prod.product.price
                    item.quantity = int(item.quantity)
                    QB = shop.checkProductStock(choiceName, item.quantity)
                    cost1 = QB * shopPrice
                    if QB < item.quantity:
                        str += f"\n---------------"
                        str += f"\n** We don't have that much {choiceName} in stock. We only have {QB} **"                   
                    if self.budget < cost1:
                        # QB = self.whatCanIAfford(QB)
                        # str += f"{QB}"
                        # QB = budget / choicePrice
                        # QB1 = math.floor(QB)
                        # totalCost = QB1 * item.product.price
                        str += f"\n** Sorry! You don't have enough money left for {choiceName}! **\n"
                        str += f"---------------"                      
                        continue                 
                    else:
                        totalBill += cost1
                        self.budget -= cost1
                        shop.cash += cost1
                        str += f"\n{item}"
                        str += f"- - - - - - - - \nQUANTITY PURCHASED: {QB}"
                        str += f"\nTOTAL ITEM COST: €{cost1:.2f}\n"
                        str += f"- - - - - - - -\n"
                        str += f"ADJUSTED BUDGET: €{self.budget:.2f}"
                        str += f"\n(ADJUSTED SHOP FLOAT: €{shop.cash:.2f})"
                        str += f"\n- - - - - - - -\n"
                        str += f"TOTAL BILL SO FAR: €{totalBill:.2f}"
                        str += "\n---------------"
                        # if (cost1 == 0):
                            # str += f"\nApologies\n"
                            # continue
                    prod.quantity -= QB  
                # else:
                    # str += f"\nWe don't stock {item.product.name}!\n"
                    # break
        str += f"\n\nTOTAL BILL: €{totalBill:.2f}"
        str += f"\nBUDGET REMAINING: €{self.budget:.2f}\n"
        str += f"\n** Thank you for your custom **\n"
            
        return str 

class Shop:
    
    def __init__(self, path): 
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)
    
    def printShop(self):
        print("\n//////////")
        print("Stock list")
        print("//////////")
        print(f"Shop has a float of €{shop.cash:.2f}")
        for item in self.stock:
            iq = int(item.quantity)
            print(item.product)
            print(f"The shop has {iq} in stock")
            print("---------------")
    
    def checkProductStock(self, n, q):
        for item in shop.stock:
            if n == item.product.name:
                if q <= item.quantity:
                    item.quantity = item.quantity - q
                    return q
                elif q > item.quantity:
                    q = int(item.quantity)
                    print("---------------")
                    print(f"** We don't have that many {n} in stock. We can only give you {q} **")
                    item.quantity = 0
                return q

    def liveMode(self):
        budget = float(input("What is your budget? \n"))
        totalBill = 0
        print("\n/////////////////////////////////////////")
        print("Welcome to the C shop LIVE SHOPPING MODE!")
        print("/////////////////////////////////////////\n")
        while True:
            print(f"Your current budget is €{budget:.2f}.\n\nPlease select what you would like to buy from the list below:\n")
            for prod in self.stock:
                print(f"{shop.stock.index(prod) + 1} - {prod.product.name} @ €{prod.product.price:.2f} each")
            print("*98* - Finish shopping and print total bill")
            print("*99* - Exit Live Mode\n")
            choice = int(input("Please make your selection: "))
            if choice == 99:
                print("\n--------------------\n")
                print("** Come again soon and have a nice day! **\n")
                print("--------------------\n")
                break
            elif choice <= 0:
                print("\n** Invalid entry - please try again! **\n")
            elif choice <= len(shop.stock) and budget > 0:
                choice = choice - 1
                choiceName = shop.stock[choice].product.name
                choicePrice = shop.stock[choice].product.price
                choiceDetails = shop.stock[choice].product
                quant = int(input(f"How many {choiceName} would you like to purchase? "))
                Product(choiceDetails)
                QB = self.checkProductStock(choiceName, quant)
                totalCost = QB * choicePrice
                if budget < totalCost:
                    print(f"\n** You don't have enough money for {choiceName}! **\n")
                    continue
                budget -= totalCost
                totalBill += totalCost
                shop.cash += totalBill
                print(f"QUANTITY REQUIRED: {quant}")
                print(f"QUANTITY PURCHASED: {QB}")
                print(f"TOTAL ITEM COST: €{totalCost:.2f}")
                print(f"ADJUSTED BUDGET: €{budget:.2f}")
                print(f"(ADJUSTED SHOP FLOAT: €{shop.cash:.2f})")
                print(f"- - - - - - - - - - - - - -\n")
                print(f"TOTAL BILL SO FAR: €{totalBill:.2f}") 
            elif choice == 98:
                print("\n--------------------\n")
                print(f"Your total bill is €{totalBill:.2f}\n")
                print("** Thank you for your custom. Please come again soon! **\n")
                print("--------------------\n")
                break
            else:
                print("** Invalid entry - please try again! **")
        shop.cash += totalBill
        mainMenu()

def mainMenu(): 
    print("\n/////////////////////")
    print(f"WELCOME TO THE C SHOP")
    print("/////////////////////\n")
    print("Please select from the following: \n")
    print("1 - Show shop's current stock and float")
    print("2 - Shop with Caoimhin's shopping list")
    print("3 - Shop with PJs's shopping list")
    print("4 - Shop with JimBob's shopping list")
    print("5 - Shop in Live Mode")
    print("0 - Exit\n")

shop = Shop("../stock.csv")

def main():
    mainMenu()
    while True:
        choice = input("Please make a selection: ")
        if (choice == "1"):
            shop.printShop()
            mainMenu()
        elif (choice == "2"):
            customer1 = Customer("../customer1.csv")
            customer1.printCustomer()
            print(customer1)
            mainMenu()
        elif (choice == "3"):
            customer2 = Customer("../customer2.csv")
            customer2.printCustomer()
            print(customer2)
            mainMenu()
        elif (choice == "4"):
            customer3 = Customer("../customer3.csv")
            customer3.printCustomer()
            print(customer3)
            mainMenu()
        elif (choice == "5"):
            print("\n////////////////////////////////")
            print("You are now entering our LIVE SHOPPING MODE!")
            print("////////////////////////////////")
            shop.liveMode()
        elif (choice == "0"):
            print("\n** Bye! Thanks for your custom! **\n** Come again soon! **\n")
            break
        else:
            print("** Invalid entry - please enter a number between 0 and 5! **")
            mainMenu()

if __name__ == "__main__":
	main()