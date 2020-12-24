#imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product
#global variables

catalog =[]

#functions



def register_product():
    try:
        print_header("Register a new Product")
        #title, category, stock, price
        title= input("Please provide the Title:")
        category = input("Please provide the Category")
        stock = int(input("Please provide the Stock Qty:"))
        price = float(input("Please provide the Price:"))


        #create obj
        the_product = Product(0, title, category, stock, price)
    

  # add obj to a list
        catalog.append(the_product)

        print_line()
        print("**Product Registered")

    except:
        print("**** Error: verify values and try again")


def print_catalog():
        print_header("Current Catalog")

        for prod in catalog:
            print_product(prod)

def print_stock():
    print_header("Stock available 0")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_value():
    print_header("Total value for in stock products")
    
    total = 0.0
    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(str(total))


def cheapest_prod():
    print_header("Cheapest product")

    prices = []
    
    for prod in catalog:
        prices.append(prod.price)

    cheapest = min(prices)
    print("The cheapest product" + str(cheapest))


#intructions

opc= ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please choose an option:")


    #compare based on the user option
    if(opc == "1"): # compare strings with strings
        register_product()
    elif(opc == '2'):
        print_catalog()

    elif(opc == '3'):
        print_stock()

    elif(opc == '4'):
        total_value()

    elif(opc == '5'):
        cheapest_prod()

    elif(opc == 'a'):
        calculate_age()
    elif(opc == 'b'):
        calculate_tip()

    input("Press enter to continue...")

print("Good bye!!")



