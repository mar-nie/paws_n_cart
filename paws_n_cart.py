"""
PAWS_N_CART - A portfolio project with HyperionDev

A simple terminal shopping cart appication with a friendly user
interface.

"""

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
Display the customers current cart and their current total.
    """
    total = 0
    for count, cart_item in enumerate(cart):
        count += 1
        total += int(cart_item[1])
        print(f"\t{count}.\t{cart_item[0]}\t\t£{cart_item[1]}")

    print(f"\tTOTAL:\t\t\t\t\t£{total}\n")


# Free sample to be given upon checkout depending on basket items
dog_treat = "Schmakos dog treats"
cat_treat = "Yummies cat treats"
rabbit_treat = "Dried Strawberry rabbit treats"

cart = []
# Pet shop stock
dog_items = [
    ("Meaty Bits Dog Chow", 15),
    ("Lil Meats Puppy Chow", 13),
    ("Schmacko Dog Treats", 5),
    ("Super Squeaky Ball", 3),
    ("Cosy Canine Dog Bed", 30)
    ]
cat_items = [
    ("Kitty Bitties Kibble", 12),
    ("Whisker Wet Food", 8),
    ("Yummies Cat Treats", 4),
    ("Royalty Cat Tree", 40),
    ("Cuddly Cosy Cat bed", 20)
    ]
rabbit_items = [
    ("Bunny Mansion Hutch", 60),
    ("Compressed Hay Bale", 6),
    ("No Stink! Sawdust", 4),
    ("Carrot Chew/Knaw Toy", 1),
    ("Small Drinking bottle", 2)
    ]

all_items = dog_items + cat_items + rabbit_items

shopping = True

dialogue_printer("welcome")

# Shopping loop only terminated by choosing to check out
while shopping:

    dialogue_printer("cart_intro")
    cart_printer()
    dialogue_printer("menu_options")

    choosing = True

    while choosing:
        choice = input("\t")

        if choice == "1":

            browsing = True

            dialogue_printer("browsing_opening")

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

            print(f"\n  {0}. Return to main menu")

            while browsing:

                dialogue_printer("cart_intro")
                cart_printer()
                dialogue_printer("browsing_command")

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

            choosing = False

        elif choice == "2":

            removing = True

            while removing:
                dialogue_printer("removal_opening")
                cart_printer()
                dialogue_printer("removal_command")

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

            choosing = False

        elif choice == "3":

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

            choosing = False

        elif choice == "4":

            has_dog = len(set.intersection(set(cart), set(dog_items))) != 0
            has_cat = len(set.intersection(set(cart), set(cat_items))) != 0
            has_rabbit = len(set.intersection(set(cart),
                                              set(rabbit_items))) != 0

            if has_dog or has_cat or has_rabbit is True:

                print("\n  Thanks for shopping! Your final cart & total was:")
                cart_printer()
                print("\n  We've thrown in free samples of:")

            if has_dog is True:
                print(f"  {dog_treat}")

            if has_cat is True:
                print(f"  {cat_treat}")

            if has_rabbit is True:
                print(f"  {rabbit_treat}")

            else:
                print("\n  Thanks for browsing, hope to see you again soon!")

            shopping = False
            choosing = False

        else:
            print("\n  Error: Please enter a number between 1 and 4\n")
