#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

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

void printProduct(struct Product p) {   
    printf("PRODUCT NAME: %s \nPRODUCT PRICE: €%.2f\n", p.name, p.price);
    }

void printCustomer(struct Customer c)
{
    printf("CUSTOMER NAME: %s\nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
    for(int i = 0; i < c.index; i++)
    {
        printProduct(c.shoppingList[i].product);
        printf("%s ORDERS %d of ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
        double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
        printf("The cost to %s will be €%.2f\n", c.name, cost);
    };
};

struct Shop createAndStockShop() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    size_t read;

    fp = fopen("stock.csv", "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    read = getline(&line, &len, fp);
    double cash = atof(line);
    struct Shop shop = { cash };

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
        shop.stock[shop.index++] = stockItem;
    }
    return shop;
}

void printShop(struct Shop s) {    
    printf("Shop has €%.2f in cash\n", s.cash);
    for (int i = 0; i < s.index; i++) {
        printProduct(s.stock[i].product);
        printf("The shop has %d of the above in stock\n", s.stock[i].quantity);
    }
}

int checkProductStock(char *n, int order, struct Shop s)
{
	for (int i =0; i < s.index; i++)
	{
		struct ProductStock product = s.stock[i];
		char *name = product.product.name;
		if (strcmp(name, n) == 0) 
		{
			if (s.stock[i].quantity >= order){
				s.stock[i].quantity = s.stock[i].quantity - order;
			}
			else{
				order = s.stock[i].quantity;
				s.stock[i].quantity = 0;
			}
			return order;
		}
	}
	return -1;
}

double findProductPrice(char *n, struct Shop s)
{
	for (int i =0; i < s.index; i++)
	{
		struct Product product = s.stock[i].product;
		char *name = product.name;
		if (strcmp(name, n) == 0) 
		{
			return product.price;
		}
	}
	return -1;
}

struct Customer create_customer(char *path_to_customer, struct Customer c, struct Shop s) {
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

        read = getline(&line, &len, fp);

        char *n = strtok(line, ","); 
        char *b = strtok(NULL, ","); 
        char *name = malloc(sizeof(char) * 50); 
        strcpy(name, n);                   
        double budget = atof(b);

        struct Customer customer = {name, budget};
        struct ProductStock shopList;

    while ((read = getline(&line, &len, fp)) != -1) {
        char *n = strtok(line, ","); 
        char *q = strtok(NULL, ","); 
        char *name = malloc(sizeof(char) * 50);
        strcpy(name, n);                   
        int quantity = atoi(q);
        shopList.product.name = name; 
		shopList.product.price = findProductPrice(name, s);
		shopList.quantity = quantity;
		customer.shoppingList[customer.index++] = shopList;
    }
    return customer;
}

int main(void)
{
    struct Customer dominic = { "Dominic", 100.0 };

    struct Product coke = { "Can Coke", 1.10 };
    struct Product bread = { "Bread", 0.70 };
    // printProduct(coke);

    struct ProductStock cokeStock = { coke, 20 };
    struct ProductStock breadStock = { bread, 2 };

    dominic.shoppingList[dominic.index++] = cokeStock;
    dominic.shoppingList[dominic.index++] = breadStock;

    printCustomer(dominic);

    struct Shop shop = createAndStockShop();
    printShop(shop);
    printf("The shop has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);

    return 0;
}