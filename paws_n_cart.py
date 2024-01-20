"""
PAWS_N_CART - A portfolio project with HyperionDev

A simple terminal shopping cart appication with a friendly user
interface. 

PSEUDOCODE:
- Establish the cart and stock, packaged into groups individual to each animal
- Create a base user menu which loops until the user chooses to exit, and
displays the user's current cart contents.
- According to numerical input within the menu, execute the following:
    - Option 1: Add an item to the cart
        - Display entire stock with prices and numerical key codes for the
        user to input, in order to add it to their cart. Once they have added
        an item return to main menu, and if they decide not to, allow them to
        enter 0 to escape back to main menu.
    - Option 2: Remove an item from the cart
        - Display their current cart with numerical key codes for the user to
        input. Repeat this until they enter 0 to return to the main menu. 
    - Option 3: Resources and advice:
        - Display a selection of resources specific to the animals that the
        items in the users cart are associated with, or give them the option
        to view all. This will display until the exit to menu by entering 0
    - Option 4: Check out
        - Display their final cart and offer a free sample depending on the
        animals that the items in their cart are associated with. 
        Exit programme.

"""

cart = []
# Pet shop stock
dog_items = [("Meaty Bits Dog Chow", 15),
             ("Lil Meats Puppy Chow", 13),
             ("Schmacko Dog Treats", 5),
             ("Super Squeaky Ball", 3),
             ("Cosy Canine Dog Bed", 30)]
cat_items = [("Kitty Bitties Kibble", 12),
             ("Whisker Wet Food", 8),
             ("Yummies Cat Treats", 4),
             ("Royalty Cat Tree", 40),
             ("Cuddly Cosy Cat bed", 20)]
rabbit_items = [("Bunny Mansion Hutch", 60),
                ("Compressed Hay Bale", 6),
                ("No Stink! Sawdust", 4),
                ("Carrot Chew/Knaw Toy", 1),
                ("Small Drinking bottle", 2)]

# Free sample to be given upon checkout depending on basket items
dog_treat = "Schmakos dog treats"
cat_treat = "Yummies cat treats"
rabbit_treat = "Dried Strawberry rabbit treats"

all_items = dog_items + cat_items + rabbit_items
shopping = True


print("""
==================================================================
      
                      Welcome to Paws n' Cart! 
                            
                               /\\ /\\
                              (=^.^=)              
                                      
          Your premium one-stop-shop for all things pets""")

while shopping:

    print("""
==================================================================
  This is your current shopping cart:""")
    total = 0
    for i, item in enumerate(cart):
        i += 1
        total += int(item[1])
        print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")        
    print(f"\tTOTAL:\t\t\t\t\t£{total}""""
------------------------------------------------------------------
  What would you like to do?
  1. Browse Items
  2. Remove an item from your cart
  3. Resources and Advice
  4. Check out
------------------------------------------------------------------""")
    choosing = True

# Need to add a try-except for this data entry

    while choosing:
        choice = input("  Please enter a number from the above list: ")

        if choice == "1":

            browsing = True

            print("""
==================================================================
Feel free to browse our range of products:
                """)

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

                print("""
==================================================================
  This is your current shopping cart:""")
                total = 0
                for i, item in enumerate(cart):
                    i += 1
                    total += int(item[1])
                    print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")        
                print(f"\tTOTAL:\t\t\t\t\t£{total}")

                product = input("""
  Please enter the number associated with the product
  you would like to purchase, or 0 to return to main menu: """)
                try:
                    int(product)
                except ValueError:
                    print(f"""
------------------------------------------------------------------  
  Error: Please enter a number between 0-{len(all_items)}""")
                else:
                    if 1 <= int(product) <= 15:
                        cart.append(all_items[(int(product) - 1)])
                        browsing = False
                    elif int(product) == 0:
                        browsing = False
                    else:
                        print(f"""
------------------------------------------------------------------  
  Error: Please enter a number between 0-{len(all_items)}""")

            choosing = False

        elif choice == "2":

            removing = True

            while removing:
                print("""
==================================================================
  Which item would you like to remove from your cart?
  
  This menu will repeat so you can remove as many items as
  you need at once. 
                     """)
                total = 0
                for i, item in enumerate(cart):
                    i += 1
                    total += int(item[1])
                    print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")
                print(f"\tTOTAL:\t\t\t\t\t£{total}")

                to_remove = input("""
  Please enter the number associated with the product
  you would like to remove, or 0 to return to main menu: """)

                try:
                    int(to_remove)
                except ValueError:

                    print(f"""
------------------------------------------------------------------
  Error: Please enter a number between 0-{len(cart)}""")
                else:
                    if 1 <= int(to_remove) <= len(cart):
                        cart.remove(cart[int(to_remove) - 1])
                    elif int(to_remove) == 0:
                        removing = False
                    else:
                        print(f"""
------------------------------------------------------------------  
  Error: Please enter a number between 0-{len(cart)}""")

            choosing = False

        elif choice == "3":

            dog_owner = """
--DOGS------------------------------------------------------------

  Guide Dogs UK:
  Support our dogs on their way to becoming a guide dog, or by
  looking after our dogs at different points in their journey.
  volunteer@guidedogs.org.uk                     0345 143 0191

  BarkHappy:
  Discover the dog friendly world around you! Explore Dog
  Friendly Places and Events, Connect with Dog Owners Nearby,
  Even Lost and Found alerts and Deals!
  barkhappy.com
            
  Dog Owner Top Tips:
  1. ENVIRONMENT - Dogs are intelligent so if they get bored,
  and don't have enough to do, they can suffer. You need to
  make sure your dog can exercise outdoors every day, play and
  interact with people or other dogs.
  2. DIET - Your dog needs a well-balanced diet to stay fit
  and healthy as well as constant access to fresh, clean
  drinking water at all times.
  3. COMPANY - Dogs are sociable animals so they need and
  enjoy company. If they are treated well as puppies, they
  learn to see people as friends and companions.          
"""
            cat_owner = """
--CATS------------------------------------------------------------
  
  Cats Protection:
  We help an estimated 157,000 cats and kittens a year through
  our national network which includes around 210 volunteer-run
  branches and 34 centres.
  cats.org.uk                                   03000 12 12 12
  
  catforum:
  A forum community dedicated to breeds of cat owners and
  enthusiasts. Come join the discussion about breeds, training,
  kittens, food reviews, and rescues.
  catforum.com
  
  Cat Owner Top Tips:
  1. FEEDING - Cats require taurine, an essential amino acid,
  for heart and eye health. The food you choose should be
  balanced for the life stage of your cat or kitten. Properly
  balanced foods will contain taurine.
  2. HANDLING - To pick up your cat, place one hand behind the
  front legs and another under the hindquarters. Lift gently.
  Never pick up a cat by the scruff of the neck or by the front
  legs.
  3. IDENTIFICATION - If allowed outdoors, your cat must wear
  a safety collar and an ID tag. A safety collar with an elastic
  panel will allow your cat to break loose if the collar gets
  caught on something.
"""

            rabbit_owner = """
--RABBITS---------------------------------------------------------

  Rabbit Rehome:
  Rabbit Rehome was set up in 2002 with the goal of helping to
  find homes for these unwanted rabbits. Rabbit Rehome is based
  around an internet website which includes a database of over
  600 rabbits available for adoption, a list of rescue centres,
  special appeals, information on volunteering, printable posters
  and guides to rabbit care.
  rabbitrehome.org.uk
"""

            print("""
==================================================================
          Welcome to the Paws n' Cart community board!
                
      Here we offer pet care advice and information on ways
      you can assist the community by volunteering locally.
            
      Based on the items in your cart, this is what we would
      reccomend to you:""")

            has_dog = len(set.intersection(set(cart), set(dog_items))) != 0
            has_cat = len(set.intersection(set(cart), set(cat_items))) != 0
            has_rabbit = len(set.intersection(set(cart),
                                              set(rabbit_items))) != 0

            if has_dog is True:
                print(dog_owner)

            if has_cat is True:
                print(cat_owner)

            if has_rabbit is True:
                print(rabbit_owner)

            if len(cart) == 0:
                print(dog_owner)
                print(cat_owner)
                print(rabbit_owner)

            done = False
            while not done:
                reading = input("""
      Enter 0 to return to the main menu, or 1 to view all
      pet advice and volunteer opportunities: """)
                try:
                    int(reading)
                except ValueError:

                    print("""
------------------------------------------------------------------
  Error: Please enter 0 or 1""")                    
                else:
                    if int(reading) == 0:
                        done = True
                    elif int(reading) == 1:
                        print(dog_owner)
                        print(cat_owner)
                        print(rabbit_owner)
                    else:
                        print("""
------------------------------------------------------------------  
  Error: Please enter 0 or 1""")

            choosing = False

        elif choice == "4":

            has_dog = len(set.intersection(set(cart), set(dog_items))) != 0
            has_cat = len(set.intersection(set(cart), set(cat_items))) != 0
            has_rabbit = len(set.intersection(set(cart),
                                              set(rabbit_items))) != 0

            if has_dog or has_cat or has_rabbit is True:

                print("\n  Thanks for shopping! Your final cart & total was:")

                total = 0
                for i, item in enumerate(cart):
                    i += 1
                    total += int(item[1])
                    print(f"\t{i}.\t{item[0]}\t\t£{item[1]}")        
                print(f"\tTOTAL:\t\t\t\t\t£{total}")

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
