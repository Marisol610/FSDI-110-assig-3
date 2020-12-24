

def print_menu():
    print("*" * 40)
    print("   Welcome to PyWarehouse   ")
    print("*" * 40)

    print("[1] Register Product")
    print("[2] View Catalog")
    print("[3] Display out of stock")
    print("[4] Total value for in stock products")
    print("[5] Cheapest Product")
    print('')

    print("[a] Calculate age")
    print("[b] Calculate Tip")
    print('')


    print(" [x] Close the system")

def print_header(header_text):
    clear()
    print('_' * 40)
    print(header_text)
    print('_' * 40)


def clear():
    print("\n\n\n\n\n")

def print_line():
    print("-"* 40)

def print_product(prod):
    print(
        str(prod.id )
          + "|" + prod.title
          + "|" + prod.category
          + "|" + str(prod.stock)
          + "|" + str(prod.price)
    )