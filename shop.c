// required libraries
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

// structs/containers for the various elements of the shop simulation
struct Product {
    char* name;
    double price;
};

struct ProductStock {
    struct Product product;
    int quantity;
};

struct Shop {
    double cash;
    struct ProductStock stock[20];
    int index;
};

struct Customer {
    char* name;
    double budget;
    struct ProductStock shoppingList[20];
    int index;
};

// create global variables to save rewriting multiple times
struct Customer c;
struct Shop s;

// function to print product info
void printProduct(struct Product p) {   
    printf("---------------\n");
    printf("PRODUCT NAME: %s \nPRODUCT PRICE: €%.2f\n", p.name, p.price);
    printf("- - - - - - - - -\n");
    }

// reading in the stock.csv file
struct Shop createAndStockShop() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    size_t read;
    fp = fopen("stock.csv", "r");
    if (fp == NULL) {
        printf("I can't access csv file? Gonna have to close down now. Please try again!");
        exit(EXIT_FAILURE);
        }
        read = getline(&line, &len, fp);
        double shopFloat = atof(line);
        s.cash = shopFloat;

    while ((read = getline(&line, &len, fp)) != -1) {
        char *n = strtok(line, ",");
        char *p = strtok(NULL, ",");
        char *q = strtok(NULL, ",");
        int quantity = atoi(q);
        double price = atof(p);
        char *name = malloc(sizeof(char) * 50);
        strcpy(name, n);
        struct Product product = {name, price};
        struct ProductStock stockItem = {product, quantity};
        s.stock[s.index++] = stockItem;
    }
    return s;
}

// function to print shop stock
void printShop() {    
    printf("//////////\n");
    printf("Stock list\n");
    printf("//////////\n");
    printf("Shop has a float of €%.2f\n", s.cash);
    for (int i = 0; i < s.index; i++) {
        printProduct(s.stock[i].product);
        printf("The shop has %d in stock\n", s.stock[i].quantity);
    }
}

// checks product stock. Updates if necessary
int checkProductStock(char *n, int order) {
	for (int i =0; i < s.index; i++) {
		struct ProductStock product = s.stock[i];
		char *name = product.product.name;
		if (strcmp(name, n) == 0) {
			if (s.stock[i].quantity >= order){
				s.stock[i].quantity = s.stock[i].quantity - order;
			}
			else {
				order = s.stock[i].quantity;
				s.stock[i].quantity = 0;
			}
			return order;
		}
	}
    // error if stock not found
	return -1;
}

// finds price of product
double findProductPrice(char *n) {
	for (int i = 0; i < s.index; i++) {
		struct Product product = s.stock[i].product;
		char *name = product.name;
		if (strcmp(name, n) == 0) {
			return product.price;
		}
	}
	return -1;
}

// reads in customer.csv file
struct Customer createCustomer(char *path_to_customer) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    size_t read;
        c.index = 0;
    // ***insert customer2.csv or customer3.csv for alternate outcomes
    fp = fopen(path_to_customer, "r");
    if (fp == NULL) {
            printf("I can't access csv file? Gonna have to close down now. Please try again!");
        exit(EXIT_FAILURE);
        }
        read = getline(&line, &len, fp);
        char *n = strtok(line, ","); 
        char *b = strtok(NULL, ","); 
        char *custName = malloc(sizeof(char) * 50); 
        strcpy(custName, n);                   
        double custBudget = atof(b);
        c.name = custName;
        c.budget = custBudget;
        struct ProductStock shopList;

    while ((read = getline(&line, &len, fp)) != -1) {
        char *n = strtok(line, ","); 
        char *q = strtok(NULL, ","); 
        char *name = malloc(sizeof(char) * 50);
        strcpy(name, n);                   
        int quantity = atoi(q);
        shopList.product.name = name; 
		shopList.product.price = findProductPrice(name);
		shopList.quantity = quantity;
		c.shoppingList[c.index++] = shopList;
    }
    return c;
}

// *** LIVE MODE ***
void liveMode() {
    double myBudget, totalCost, totalBill;
    int qr, qb, select;
    printf("What is your budget?\n");
    scanf("%lf", &myBudget);
        do {
            printf("\n//////////////////////\n");
            printf("Welcome to the C shop LIVE SHOPPING MODE!\n");
            printf("//////////////////////\n");
            printf("Your current budget is €%.2f.\nPlease select what you would like to buy from the list below:\n\n", myBudget);
            for(int i=0; i < s.index; i++) {
                printf("%d - %s @ €%.2f each.\n", i + 1, s.stock[i].product.name, findProductPrice(s.stock[i].product.name));
            }
            printf("99 - finish shopping and print total bill\n");
            printf("0 - Exit Live Mode");
            printf("\nPlease make your selection: ");
            scanf("%d", &select);
            switch(select) {
                case 0: {
                    printf("\n--------------------\n");
                    printf("Come again soon and have a nice day!\n");
                    printf("--------------------\n");
                    break;
                }
                case 99: {
                    printf("\n--------------------\n");
                    printf("Your total bill is €%.2f.\n", totalBill);
                    printf("Thank you for your custom. Please come again soon!\n");
                    printf("--------------------\n");
                    break;
                }
                default: {
                    if (select > s.index+1) {
                        printf("Please choose a number from the list above");
                        break;
                    }
                    printf ("How many %ss would you like to purchase? ", s.stock[select-1].product.name);
                    scanf("%d", &qr);
                    qb = qr;

                    totalCost = qb * findProductPrice(s.stock[select-1].product.name);

                    if (myBudget < totalCost) {
                        qb = myBudget / findProductPrice(s.stock[select-1].product.name);
                        }
                    qb = checkProductStock(s.stock[select-1].product.name, qb);

                    totalCost = qb * findProductPrice(s.stock[select-1].product.name);

                    myBudget -= totalCost;
                    totalBill += totalCost;
                    s.cash += totalCost;
	    			printProduct(s.stock[select-1].product);
	    			printf("QUANTITY REQUIRED: %d\n", qr);
	    			printf("QUANTITY PURCHASED: %d\n", qb);
	    			printf("TOTAL ITEM COST: €%.2f\n", totalCost);
	    			printf("ADJUSTED BUDGET: €%.2f\n", myBudget);
	    			printf("(ADJUSTED SHOP FLOAT: €%.2f)\n", s.cash);
                    printf("- - - - - - - - - - - - - -\n");
                    printf("TOTAL BILL SO FAR: €%.2f\n", totalBill);
                    if (qr != qb) {
                        printf("\n****We are unable to satisfy this order in full due to insufficient funds/stock****\n");
                        }
                    }
                }
            }  
            // exit if 0 or 99 is entered
            while (select != 0 && select != 99);
    }

// does the shopping via the shopping list contained in customer.csv
void printCustomer(bool upd) {
    printf("////////////////////////\n");
	printf("%s's shopping list\n", c.name);
    printf("////////////////////////\n");
	printf("Budget: €%.2f\n", c.budget);
	int qb; 
    double cost, totalBill;
	for(int i = 0; i < c.index; i++){
		qb = c.shoppingList[i].quantity;
		printProduct(c.shoppingList[i].product);
		printf("QUANTITY REQUIRED: %d\n", c.shoppingList[i].quantity);
		if (c.shoppingList[i].product.price > -1){
			cost = qb * c.shoppingList[i].product.price; 
			if (upd){
				if(cost > c.budget){
					qb = c.budget / c.shoppingList[i].product.price;
				}
				qb = checkProductStock(c.shoppingList[i].product.name, qb);				
				cost = qb * c.shoppingList[i].product.price;				
				c.budget -= cost;				
				s.cash += cost;
                totalBill += cost;
				printf("QUANTITY PURCHASED: %d\n", qb);
				printf("TOTAL ITEM COST: €%.2f\n", cost);
                printf("- - - - - - - - \n");
				printf("ADJUSTED BUDGET: €%.2f\n", c.budget);
				printf("ADJUSTED SHOP FLOAT: €%.2f\n", s.cash);
                printf("---------------\n");
                printf("TOTAL BILL: €%.2f\n", totalBill);
                printf("---------------\n");
				if (c.shoppingList[i].quantity != qb){
					printf("\nSorry! Can't fulfill order on this item due to insufficient funds/stock.\n");
				}
				c.shoppingList[i].quantity -= qb;				
			}	
			else {
				printf("TOTAL ITEM COST: €%.2f\n", cost);
                printf("- - - - - - - - \n");
			}
		}	
		else {
			printf("Sorry, we do not stock %s!\n", c.shoppingList[i].product.name);
		}
	}
}

// main program with menu, etc.
void mainMenu(struct Shop s) {
	int menuSelect;
	do {
        printf("\n/////////////////////\n");
		printf("WELCOME TO THE C SHOP\n");
        printf("/////////////////////\n");
		printf("\nPlease select from the following:\n\n");
		printf("1 - Show shop's current stock and float\n"); 
		printf("2 - Show Caoimhin's shopping list\n"); 
        // other shopping lists?
		printf("3 - Shop with Caoimhin's shopping list\n"); 
        printf("4 - Shop with PJs's shopping list\n"); 
        printf("5 - Shop with JimBob's shopping list\n"); 
        // options for other shopping lists?
		printf("6 - Shop in Live Mode\n"); 
        // get rid of resets?
		// printf("7 - Reset shop stock and float\n"); 
		// printf("8 - Reset customer budget\n"); 
		printf("0 - Exit\n");
		printf("\nPlease make a selection: \n");
		scanf("%d", &menuSelect);
        // https://www.programiz.com/c-programming/c-switch-case-statement
		switch (menuSelect){

			case 1:{
				printShop();
				break;
			}
			case 2:{
                struct Customer customer_A = createCustomer("customer1.csv");
				printCustomer(false);
				break;
			}
			case 3:{
                struct Customer customer1 = createCustomer("customer1.csv");
				printCustomer(true);
				break;
			}
            case 4:{
                struct Customer customer2 = createCustomer("customer2.csv");
				printCustomer(true);
				break;
			}
            case 5:{
                struct Customer customer3 = createCustomer("customer3.csv");
				printCustomer(true);
				break;
			}
			case 6:{
                printf("\n////////////////////////////////");
				printf("\nYou are now entering our LIVE SHOPPING MODE!\n");
                printf("////////////////////////////////\n");
				liveMode();
				break;
			}
			case 0:{
				printf("\nBye %s! Thank's for your custom!\nCome again soon!\n", c.name);
				break;
			}
			default:{
				printf("\nIncorrect Selection - please try again\n");
				break;
			}
		}
	}
	    while (menuSelect != 0);
}
// main method
int main()
{

  // create shop
  struct Shop newShop = createAndStockShop();

  mainMenu(newShop);

  return 0;
}
