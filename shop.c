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

// struct ProductQuantity {
//   struct Product product; 
//   int quantity;
// };

struct Shop {
    double cash;
    struct ProductStock stock[20];
    int index;
};

struct Customer {
    char* name;
    double budget;
    struct ProductQuantity shoppingList[10];
    int index;
};

void printProduct(struct Product p)
{
    if (p.price == 0) {
        printf("PRODUCT NAME: %s;", p.name);
    }
    else {
    printf("PRODUCT NAME: %s\nPRODUCT PRICE: €%.2f\n", p.name, p.price);
    }
}

// // ????
// void printCustomer(struct Customer c)
// {
//     printf("-------------------\n");
//     printf("CUSTOMER NAME: %s\nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
//     printf("-------------------\n");
//     for(int i = 0; i < c.index; i++)
//     {
//         printProduct(c.shoppingList[i].product);
//         printf("%s ORDERS %d of ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
//         double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
//         printf("The cost to %s will be €%.2f\n", c.name, cost);
//     };
// };

double get_product_price(struct Product p) {
  return p.price;
}

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
    };

    return shop;
}

void printShop(struct Shop s)
{
    printf("Shop has €%.2f in cash\n", s.cash);
    for (int i = 0; i < s.index; i++)
    {
        printProduct(s.stock[i].product);
        printf("The shop has %d of the above\n", s.stock[i].quantity);
    }
}

struct Customer create_customer(char *path_to_customer) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    size_t read;

    fp = fopen(path_to_customer, "r"); 
    if (fp == NULL)
    {
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

    while ((read = getline(&line, &len, fp)) != -1) {
    char *p_n = strtok(line, ","); 
    char *p_q = strtok(NULL, ","); 
    char *name = malloc(sizeof(char) * 50);
    strcpy(name, p_n);                   
    int quantity = atoi(p_q);

    struct Product product = {name}; 

    struct ProductQuantity shopping_list_item = {product, quantity}; 
    customer.shoppingList[customer.index++] = shopping_list_item;
    }
    return customer;
}

void printShop(struct Shop *sh)
{
  printf("\nShop has €%.2f in cash\n", sh->cash);

  for (int i = 0; i < sh->index; i++)
  {
    printProduct(sh->stock[i].product);
    printf("Available amount: %d\n", sh->stock[i].quantity);
  }
  printf("\n");
}

double print_customers_details(struct Customer *cust, struct Shop *sh) {
    printf("\nCustomer name: %s, budget: €%.2f \n", cust->name, cust->budget); 
    double total_cost = 0.0;
    printf("%s wants the following products: \n", cust->name);

    for (int i = 0; i < cust->index; i++) {
        printf(" -%s, quantity %d. ", cust->shoppingList[i].product, cust->shoppingList[i].quantity);
        double sub_total = 0;
        int match_exist = 0;                                      
        char *cust_item_name = cust->shoppingList[i].product.name; 

    for (int j = 0; j < sh->index; j++)
    {
      char *sh_item_name = sh->stock[j].product.name; 

      if (strcmp(cust_item_name, sh_item_name) == 0) 
      {
        match_exist++;        
        if (cust->shoppingList[i].quantity <= sh->stock[j].quantity) {
            printf("\tOK, there is enough in stock and "); 
            double sub_total_full = cust->shoppingList[i].quantity * sh->stock[j].product.price; 
            printf("the sub-total cost is €%.2f. \n", sub_total_full);                         
            sub_total = sub_total_full;                                                         
            }

        else {
            int partial_order_qty = cust->shoppingList[i].quantity - (cust->shoppingList[i].quantity - sh->stock[j].quantity);
            double sub_total_partial = partial_order_qty * sh->stock[j].product.price;                                                         
            printf("\tOnly %d are available and the sub-total cost for that many is €%.2f. \n", partial_order_qty, sub_total_partial); 
            sub_total = sub_total_partial;
            }
        total_cost = total_cost + sub_total;
        }
    }
    if (match_exist == 0) {
        printf("\tThis product is not available. The sub-total cost will be €%.2f. \n", sub_total); 
        }
  }
  printf("\nTotal shopping cost will be €%.2f. \n\n", total_cost);

  return total_cost;
}

void process_order(struct Customer *cust, struct Shop *sh, double *total_cost) {
    if (cust->budget < *total_cost) {
        printf("Unfortunately, the customer does not have enough money for all of those items - he is short €%.2f. ", (*total_cost - cust->budget));
        printf("Shopping is aborted. Please try again later!\n\n");
        }

    else {
        printf("Processing...\n");

        for (int i = 0; i < cust->index; i++) {
            int match_exist = 0;                                       
            char *cust_item_name = cust->shoppingList[i].product.name; 

            for (int j = 0; j < sh->index; j++) {
                char *sh_item_name = sh->stock[j].product.name; 
                if (strcmp(cust_item_name, sh_item_name) == 0) {
                    match_exist++; 

                    if (cust->shoppingList[i].quantity <= sh->stock[j].quantity) {
                        sh->stock[j].quantity = sh->stock[j].quantity - cust->shoppingList[i].quantity;
                        printf("Stock quantity of %s updated to: %d \n", cust->shoppingList[i].product.name, sh->stock[j].quantity);
                        }

                    else {
                        int partial_order_qty = cust->shoppingList[i].quantity - (cust->shoppingList[i].quantity - sh->stock[j].quantity);
                        double sub_total_partial = partial_order_qty * sh->stock[j].product.price; 

                        sh->stock[j].quantity = sh->stock[j].quantity - partial_order_qty;

                        printf("Stock quantity of %s updated to %d. \n", cust->shoppingList[i].product.name, sh->stock[j].quantity);
                        }
                    }
                }
                if (match_exist == 0) {
                    printf("\tThis product is not available. Total cost will be €0.00. \n");
                    }
                }

            sh->cash = sh->cash + *total_cost;

            cust->budget = (cust->budget - *total_cost);

            printf("\nShop has now €%.2f in cash. \n", sh->cash);
            printf("%s has €%.2f remaining in cash. \n", cust->name, cust->budget);
            printf("\n");
        };

        return;
}   

// int main(void)
// {
//     struct Customer dominic = { "Dominic", 100.0 };

//     struct Product coke = { "Can Coke", 1.10 };
//     struct Product bread = { "Bread", 0.70 };
//     // printProduct(coke);

//     struct ProductStock cokeStock = { coke, 20 };
//     struct ProductStock breadStock = { bread, 2 };

//     dominic.shoppingList[dominic.index++] = cokeStock;
//     dominic.shoppingList[dominic.index++] = breadStock;

//     printCustomer(dominic);

//     struct Shop shop = createAndStockShop();
//     printShop(shop);
//     printf("The shop has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);

//     return 0;
// }