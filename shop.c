// required libraries
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

// structs/containers for the various aspects of the shop simulation
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
    struct ProductStock shoppingList[10];
    int index;
};

// create global variables
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
        exit(EXIT_FAILURE);
    };
        getline(&line, &len, fp);
        double cash = atof(line);
        s.cash = cash;

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

// checks product stock
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
struct Customer createCustomer() {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    size_t read;
        c.index = 0;
    fp = fopen("customer.csv", "r"); 
    if (fp == NULL) {
        printf("File not found\n");
        exit(EXIT_FAILURE);
        }
        getline(&line, &len, fp);
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
    };
    return c;
};

// *** LIVE MODE ***
void liveMode() {
    struct Shop s;
    double myBudget, totalCost;
    int qr, qb, select;
    printf("What is your budget?\n");
    scanf("%lf", &myBudget);
        do {
            printf("Welcome to my shop");
            printf("Your current budget is %.2f.\nPlease select what you would like to buy from the list below:\n\n", myBudget);
            for(int i=0; i < s.index; i++) {
                printf("%d - %s @ %.2f each.\n", i + 1, s.stock[i].product.name, findProductPrice(s.stock[i].product.name));
            }
            printf("0 - Exit Live Mode");
            printf("\nPlease make your selection: ");
            scanf("%d", &select);
            switch(select) {
                case 0: {
                    printf("Thank you for choosing Live Mode. Come again soon and have a nice day!");
                    break;
                }
                default: {
                    if (select > s.index+1) {
                        printf("Please select from the list above");
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
	    			printProduct(s.stock[select-1].product);
	    			printf("QUANTITY REQUIRED: %d\n", qr);
	    			printf("QUANTITY PURCHASED: %d\n", qb);
	    			printf("TOTAL ITEM COST: EUR %.2f\n", totalCost);
	    			printf("ADJUSTED BUDGET: EUR %.2f\n", myBudget);
	    			printf("ADJUSTED SHOP FLOAT: EUR %.2f", s.cash);
                    if (qr != qb) {
                        printf("\nWe are unable to fulfill order on this item because of insufficient funds/stock");
                    }
                    printf("**********");
                    }
                }
            }  
            while (select != 0);
    }

// does the shopping via the shopping list contained in customer.csv
void printCustomer(bool upd) {
    printf("////////////////////////\n");
	printf("%s's shopping list\n", c.name);
    printf("////////////////////////\n");
	printf("Budget: €%.2f\n", c.budget);
	int qb; 
	for(int i = 0; i < c.index; i++){
		qb = c.shoppingList[i].quantity;
		printProduct(c.shoppingList[i].product);
		printf("QUANTITY REQUIRED: %d\n", c.shoppingList[i].quantity);
		double cost;
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

				printf("QUANTITY PURCHASED: %d\n", qb);
				printf("TOTAL ITEM COST: EUR %.2f\n", cost);
                printf("- - - - - - - - \n");
				printf("ADJUSTED BUDGET: EUR %.2f\n", c.budget);
				printf("ADJUSTED SHOP FLOAT: EUR %.2f\n", s.cash);
                printf("---------------\n");
				if (c.shoppingList[i].quantity != qb){
					printf("\nUnable to fulfill complete order on this item due to insufficient funds / stock.");
				}
				c.shoppingList[i].quantity -= qb;				

			}	
			else {
				// Relays the information to the user
				printf("TOTAL ITEM COST: EUR €%.2f\n", cost);
                printf("- - - - - - - - \n");
			}
		}	
		else {
			printf("Sorry, shop does not stock %s.", c.shoppingList[i].product.name);
		}
	}
}

// could have done this from the start I guess!
struct Shop shop;
struct Customer customer;

// main program with menu, etc.
int main(void) 
{
	shop = createAndStockShop();
	customer = createCustomer();
	int menuSelect;
	do {
        printf("\n/////////////////////\n");
		printf("WELCOME TO THE C SHOP\n");
        printf("/////////////////////\n");
		printf("\nPlease select from the following:\n\n");
		printf("1 - Show shop stock\n"); 
		printf("2 - Show current shopping list\n"); 
		printf("3 - Shop with shopping list\n"); 
		printf("4 - Shop in Live Mode\n"); 
		printf("5 - Reset shop stock and float\n"); 
		printf("6 - Reset customer shopping list and budget\n"); 
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
				printCustomer(false);
				break;
			}
			case 3:{
				printCustomer(true);
				break;
			}
			case 4:{
				printf("\nYou are now entering LIVE Mode!\n");
				liveMode();
				break;
			}
			case 5:{
				shop = createAndStockShop();
				printf("\n*** Shop now reset. ***\n");
				break;
			}
			case 6:{
				customer = createCustomer();
				printf("\n*** Customer now reset. ***!\n");
				break;
			}
			case 0:{
				printf("\nGoodbye %s and thank you for your custom!\n", customer.name);
				break;
			}
			default:{
				printf("\nIncorrect Selection - please try again\n");
				break;
			}
		}
	}
	while (menuSelect != 0);
    return 0;
}
