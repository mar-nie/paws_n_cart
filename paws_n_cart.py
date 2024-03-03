"""
PAWS_N_CART - A portfolio project with HyperionDev

A simple terminal shopping cart appication with a friendly user
interface.

"""
from csv import reader

def import_stock():
    """
The function `import_stock()` reads a CSV file containing stock information and
categorizes the items into different lists based on their type (dog, cat,
rabbit).
    """

    all_stock = "pawsncart_stock.csv"

    with open(all_stock, "r", encoding='utf-8') as stock:
        items = reader(stock)
        for row in items:
            if row[0] != "freesample":
                all_items.append((row[1], row[2]))
                if row[0] == "dog":
                    dog_items.append((row[1], row[2]))
                elif row[0] == "cat":
                    cat_items.append((row[1], row[2]))
                elif row[0] == "rabbit":
                    rabbit_items.append((row[1], row[2]))


def import_samples(animal):
    """
The code snippet is opening a CSV file named "pawsncart_stock.csv" and reading
its contents using the `csv.reader()` function. It then iterates over each row
in the file and checks if the value in the first column (`row[0]`) is equal to
"freesample". If it is, it further checks if the value in the second column
(`row[1]`) is equal to the provided `animal` argument. If both conditions are
true, it returns the value in the third column (`row[2]`).
    """
    all_stock = "pawsncart_stock.csv"

    with open(all_stock, "r", encoding='utf-8') as stock:
        items = reader(stock)
        for row in items:
            if row[0] == "freesample":
                if row[1] == animal:
                    return row[2]


def dialogue_printer(dialogue_code):
    """ 
Print out interface text from external file pawsncart_interface according
to argument entered.
    """
    with open("pawsncart_interface.txt", "r", encoding='UTF-8') as text:
        content = text.readlines()
        for counter1, line in enumerate(content):
            if f"$$$ {dialogue_code} $$$" in line:
                start_position = counter1 + 1
            else:
                continue

        iterating = True
        end_position = 0
        counter2 = 0


        while iterating:
            if "$$$" in content[start_position + counter2]:
                end_position = counter2 + start_position
                iterating = False
            else:
                counter2 += 1


        for line in content[start_position:end_position]:
            print(line.strip("\n"))


def cart_printer():
    """
Display the customers current cart as a numbered list alongside the current
total.
    """
    total = 0
    for count, cart_item in enumerate(cart):
        count += 1
        total += int(cart_item[1])
        print(f"\t{count}.\t{cart_item[0]}\t\t£{cart_item[1]}")

    print(f"\tTOTAL:\t\t\t\t\t£{total}\n")


def stock_printer():
    """
The function `stock_printer` prints a formatted list of items and their prices
for dog, cat, and rabbit items.
    """

    print("\nDOG ITEMS" + "-" * 53)
    for i, item in enumerate(dog_items):
        i += 1
        print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")

    print("\nCAT ITEMS" + "-" * 53)
    for i, item in enumerate(cat_items):
        i += 1 + len(dog_items)
        print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")

    print("\nRABBIT ITEMS" + "-" * 50)
    for i, item in enumerate(rabbit_items):
        i += 1 + len(dog_items) + len(cat_items)
        print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")


def add_items():
    """
The function allows the user to browse and add items to their cart.
    """
    browsing = True

    dialogue_printer("browsing_opening")
    # Display all stock items as a numbered list for easy selection
    stock_printer()

    print(f"\n  {0}. Return to main menu")

    while browsing:
        # Loop for browsing store items, repeats if input is invalid
        dialogue_printer("cart_intro")
        cart_printer()
        dialogue_printer("browsing_command")

        # User selects cart item to add using numbered list
        product = input("\t")

        try:
            int(product)
        except ValueError:
            dialogue_printer("browsing_error")
            print("  Error: Please enter a number between"
                    + f"0-{len(all_items)}")
        else:
            if 1 <= int(product) <= 15:
                cart.append(all_items[(int(product) - 1)])
                browsing = False
            elif int(product) == 0:
                browsing = False
            else:
                dialogue_printer("browsing_error")
                print("  Error: Please enter a number between"
                    + f"0-{len(all_items)}")


def remove_items():
    """
The function `remove_items()` allows the user to remove items from a cart by
selecting them using a numbered list.
    """
    removing = True

    while removing:
        dialogue_printer("removal_opening")
        cart_printer()
        dialogue_printer("removal_command")

        # User selects cart item to remove using numbered list
        to_remove = input("\t")

        try:
            int(to_remove)
        except ValueError:

            dialogue_printer("removal_error")
            print("  Error: Please enter a number between "
                    + f"0-{len(cart)}")
        else:
            if 1 <= int(to_remove) <= len(cart):
                cart.remove(cart[int(to_remove) - 1])
            elif int(to_remove) == 0:
                removing = False
            else:
                dialogue_printer("removal_error")
                print("  Error: Please enter a number between "
                        + f"0-{len(cart)}")


def community_board():
    """
The `community_board` function checks the items in a shopping cart and prints
out information about dogs, cats, and rabbits based on the items in the cart.
    """

    dialogue_printer("community_opening")

    has_dog = len(set.intersection(set(cart), set(dog_items))) != 0
    has_cat = len(set.intersection(set(cart), set(cat_items))) != 0
    has_rabbit = len(set.intersection(set(cart),
                                        set(rabbit_items))) != 0

    if has_dog is True:
        dialogue_printer("community_dogs")

    if has_cat is True:
        dialogue_printer("community_cats")

    if has_rabbit is True:
        dialogue_printer("community_rabbits")

    if len(cart) == 0:
        dialogue_printer("community_dogs")
        dialogue_printer("community_cats")
        dialogue_printer("community_rabbits")

    done = False
    while not done:
        dialogue_printer("community_command")
        reading = input("\t")
        try:
            int(reading)
        except ValueError:

            dialogue_printer("community_error")

        else:
            if int(reading) == 0:
                done = True
            elif int(reading) == 1:
                dialogue_printer("community_dogs")
                dialogue_printer("community_cats")
                dialogue_printer("community_rabbits")
            else:
                dialogue_printer("community_error")


def reciept_printer():
    reciept_intro = ("  Thanks for shopping!"
    + "Your final cart & total was:")

    reciept += "\n  We've thrown in free samples of:"

    if has_dog is True:
        reciept += f"  {dog_treat}"

    if has_cat is True:
        reciept += f"  {cat_treat}"

    if has_rabbit is True:
        reciept += f"  {rabbit_treat}"

    print(reciept)


cart = []
dog_items = []
cat_items = []
rabbit_items = []
all_items = []

import_stock()

dog_treat = import_samples("dog")
cat_treat = import_samples("cat")
rabbit_treat = import_samples("rabbit")

dialogue_printer("welcome")
shopping = True
# Shopping loop only terminated by choosing to check out
while shopping:

    dialogue_printer("cart_intro")
    cart_printer()
    dialogue_printer("menu_options")

    choosing = True
    # Main menu loop
    while choosing:
        choice = input("\t")

        # 1 - Browsing the menu and adding items to the cart
        if choice == "1":

            add_items()
            choosing = False

        # 2 - Removing items from the cart
        elif choice == "2":

            remove_items()
            choosing = False

        # 3 - Displaying the pet shop community board
        elif choice == "3":

            community_board()
            choosing = False

        # 4 - Checking out and offering a free sample
        elif choice == "4":

            has_dog = len(set.intersection(set(cart), set(dog_items))) != 0
            has_cat = len(set.intersection(set(cart), set(cat_items))) != 0
            has_rabbit = len(set.intersection(set(cart),
                                              set(rabbit_items))) != 0

            if has_dog or has_cat or has_rabbit is True:

                reciept_printer()
                print("Thanks for shopping! Your Reciept has been printed.")

            else:
                print("\n  Thanks for browsing, hope to see you again soon!")

            shopping = False
            choosing = False

        else:
            print("\n  Error: Please enter a number between 1 and 4\n")
