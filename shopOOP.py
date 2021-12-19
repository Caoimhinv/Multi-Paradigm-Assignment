import csv
import math

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'---------------\nPRODUCT NAME: {self.name}\nPRODUCT PRICE: €{self.price:.2f}\n- - - - - - - - -'

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
                
    def printCustomer(self, shop_stock):
        for prod in shop_stock:
            for item in self.shoppingList:
                if item.name() == prod.name():
                    item.product.price = prod.itemPrice()
                    shopPrice = item.product.price
                    shopQuant = int(prod.quantity)
                    item.quantity = int(item.quantity)
                    # print (shopPrice)
            if shopQuant < item.quantity:
                print("\nSorry! Can't fulfill order on this item due to insufficient stock.")
            else:
                totalBill = 0
                cost = item.quantity * shopPrice
                totalBill += cost
                self.budget -= cost
                shop.cash += cost
                print("---------------")
                print(f"PRODUCT NAME: {item.product.name}")
                print(f"PRODUCT PRICE: €{shopPrice:.2f}")
                print(f"QUANTITY REQUIRED: {item.quantity}")
                print("- - - - - - - - ")
                print(f"QUANTITY PURCHASED: {item.quantity}")
                print(f"TOTAL ITEM COST:: €{cost:.2f}")
                print("- - - - - - - - ")
                print(f"ADJUSTED BUDGET: €{self.budget:.2f}")
                print(f"(ADJUSTED SHOP FLOAT: €{shop.cash:.2f})")
                print("---------------")
                print(f"TOTAL BILL SO FAR: €{totalBill:.2f}")
                print("---------------")
                shopQuant -= item.quantity
        # print(f"TOTAL BILL: €{totalBill:.2f}\n** Thank you for your custom **\n")
        return self

    def order_cost(self):
        cost = 0
        for i in self.shoppingList:
            cost += i.cost()
        return cost
        
    def __repr__(self):
        print('')
        format_float = "{:.2f}".format(self.budget)
        str = f"\n////////////////////////\n{self.name}'s shopping list\n////////////////////////\n"
        str += f"BUDGET: €{format_float}\n"
        for item in self.shoppingList:
            cost = item.cost()
            str += f"\n{item}"
            if (cost == 0):
                str += f"Sorry, we don't stock {item.product.name}\n"
            else:
                str += f"TOTAL COST: €{round(self.order_cost(),2)}\n"
                
        str += f"\n{self.name}'s budget is now €{round(self.budget - self.order_cost(),2)}\n"
        str += f"\nTOTAL BILL: €{round(self.order_cost(),2)}\n** Thank you for your custom **\n"
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

    # def shop_balance(self):
    #     print(f'Initial cash value for the shop is {shop.cash}')
    
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
                
    def check_shop(self, customerShoppingList):
        stock = self.stock
        for i in stock:
            shop_item_name = i.product.name
            if shop_item_name == customerShoppingList: 
                return i
    
    def checkProductStock(self, n,q):
        for item in shop.stock:
            if n == item.product.name:
                if q <= item.quantity:
                    return q
                elif q > item.quantity:
                    q = int(item.quantity)
                    print(f"We don't have that many in stock. We only have {q}")
                    return q
            else:
                print(f"Sorry, we don't stock {n}!")

    def liveMode(self):
        budget = float(input("What is your budget? \n"))
        totalBill = 0
        print("\n//////////////////////")
        print("Welcome to the C shop LIVE SHOPPING MODE!")
        print("//////////////////////\n")
        while True:
            print(f"Your current budget is €{budget:.2f}.\n\nPlease select what you would like to buy from the list below:\n")
            for prod in shop.stock:
                print(f"{shop.stock.index(prod) + 1} - {prod.product.name} @ €{prod.product.price:.2f} each")
            print("**98** - finish shopping and print total bill")
            print("**99** - Exit Live Mode\n")
            choice = int(input("Please make your selection: "))
            if choice == 99:
                print("\n--------------------\n")
                print("Come again soon and have a nice day!\n")
                print("--------------------\n")
                break
            elif choice <= len(shop.stock) and budget > 0:
                choice = choice - 1
                choiceName = shop.stock[choice].product.name
                choicePrice = shop.stock[choice].product.price
                choiceDetails = shop.stock[choice].product
                quant = int(input(f"How many {choiceName} would you like to purchase? "))
                QB = self.checkProductStock(choiceName, quant)
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
                shop.cash += totalBill
                Product(choiceDetails)

                print(f"QUANTITY REQUIRED: {quant}")
                print(f"QUANTITY PURCHASED: {QB}")
                print(f"TOTAL ITEM COST: €{totalCost:.2f}")
                print(f"ADJUSTED BUDGET: €{budget:.2f}")
                print(f"(ADJUSTED SHOP FLOAT: €{shop.cash:.2f}")
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

def mainMenu(): 
    print("\n////////////////////////")
    print(f"WELCOME TO THE C SHOP")
    print("////////////////////////\n")
    print("Please select from the following: \n")
    print("1 - Show shop's current stock and float")
    print("2 - Shop with Caoimhin's shopping list")
    print("3 - Shop with PJs's shopping list")
    print("4 - Shop with JimBob's shopping list")
    print("5 - Live Mode")
    print("0 - Exit application")

shop = Shop("stock.csv")

def main():
    mainMenu()
    while True:
        choice = input("Please make a selection: ")
        if (choice == "1"):
            shop.printShop()
            mainMenu()
        elif (choice == "2"):
            customer1 = Customer("customer1.csv")
            customer1.printCustomer(shop.stock)
            print(customer1)
            mainMenu()
        elif (choice == "3"):
            customer2 = Customer("customer2.csv")
            customer2.printCustomer(shop.stock)
            print(customer2)
            mainMenu()
        elif (choice == "4"):
            customer3 = Customer("customer3.csv")
            customer3.printCustomer(shop.stock)
            print(customer3)
            mainMenu()
        elif (choice == "5"):
            print("\n////////////////////////////////")
            print("You are now entering our LIVE SHOPPING MODE!")
            print("////////////////////////////////")
            shop.liveMode()
        elif (choice == "0"):
            break
        else:
            mainMenu()

if __name__ == "__main__":
	main()