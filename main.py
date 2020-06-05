from room import Room
from item import Item
from character import Enemy, Friend

# Description
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with golden decorations.")
ballroom = Room("Ballroom")
ballroom.set_description("A shiny room with a shiny.")
void = Room("Void")
void.set_description("...space....")

# Linked rooms directions
kitchen.link_room(dining_hall, "south")
kitchen.link_room(ballroom, "southwest")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(kitchen, "northeast")

# Items
time_machine = Item("Time Machine")
time_machine.set_description("It's a small metallic intricate cube, with a rotating ball nestled in it.")
time_machine.set_power("teleport")

# Items in rooms
ballroom.set_item(time_machine)

# Characters
jeff = Enemy("Jeff", "A bare knock fighter")
jeff.set_conversation("I'll blow you down like smoke!")
jeff.set_weakness("melon")
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("I'm all bones.")

# Characters in rooms
dining_hall.set_character(jeff)
kitchen.set_character(catrina)

# No repetitions
new_room = True
new_inhabitant = True
new_gadget = True

# Starting elements
current_room = kitchen
backpack = []
dead = False

while not dead:

    print("\n")
    # Print room details if not the same room
    if new_room:
        current_room.get_details()
        new_room = False

    gadget = current_room.get_item()
    # Check if there is an Item in the room
    if gadget is not None and new_gadget:
        print("there is something there, what is it? To take it write 'pick'... ")  # Gadget intro
        new_gadget = False

    inhabitant = current_room.get_character()
    if inhabitant is not None and new_inhabitant:
        # Check if there is a Character in the room
        inhabitant.describe()
        print(f"You can talk to {inhabitant.name} writing 'talk'.")
        if isinstance(inhabitant, Enemy):
            print("Or you can fight, writing 'fight'!")
        if isinstance(inhabitant, Friend):
            print(f"You can also hug {inhabitant.name} writing 'hug'.")

    command = input("> ")
    # current_room.direction
    if command in ["south", "southwest", "north", "west", "east", "northeast"]:
        temp = current_room
        current_room = current_room.move(command)
        if temp != current_room:
            new_room = True
            new_inhabitant = True
            new_gadget = True

    elif command == "talk":
        new_inhabitant = False
        # Talk to the inhabitant - check if there is one
        if inhabitant is not None:
            print("\n")
            inhabitant.talk()

    elif command == "fight":
        new_inhabitant = False
        # Fight with the inhabitant
        if inhabitant is None or isinstance(inhabitant, Friend):
            print("\nThere is no one here to fight with.")
        else:
            # fight with the enemy if there is one
            print("\nWhat will you fight with?"
                  "\nYou can choose to fight with:"
                  "\n- a 'pillow'"
                  "\n- a 'melon'"
                  "\n- the 'grandmother'"
                  "\n select one by entering the corresponding name.")
            fight_with = input("> ")
            if inhabitant.fight(fight_with):
                # What happens if you win?
                print("\nYou win!!"
                      f"\nYou're in the {current_room.name} where do you wanna go now?")
            else:
                # What happens if you lose?
                if fight_with == "pillow":
                    print("Who fights with a pillow? It's not a childish game. Jeff killed you."
                          "\nThis is the end of the game.")
                if fight_with == "grandmother":
                    print("Grandma' is mad at you and started to help Jeff to knock you down!"
                          "\nThis is the end of the game.")
                dead = True

    elif command == "hug":
        new_inhabitant = False
        if inhabitant is None:
            print("\nThere is no one here to hug")
        else:
            if isinstance(inhabitant, Enemy):
                print("\nI wouldn't do that if I were you!")
            else:
                inhabitant.hug()

    elif command == "pick":
        print("\n")
        gadget.describe()
        print(f"Looks like a {gadget.name}."
              f"\nI will keep it in my backpack.")
        backpack.append(gadget)  # returns 'Time Machine'
        print(f"You can use it typing '{gadget.power}'.")
        new_gadget = False  # Removing gadget intro
        current_room.item = None  # Removing the gadget from the room

    if command == "teleport":
        y = lambda x: True if x == "teleport" in backpack else False
        if y:
            print("\n")
            last_room = current_room
            current_room = void
            print(f"You're in the {current_room.name}.\n")
            current_room.describe()
            print("\nthere is no other way to go. "
                  "You can use the time machine to get back to the ballroom.\nTo do so, type 'reuse'.")
            get_to_previous_room = input("> ")
            while get_to_previous_room != "reuse":
                print("\nNothing happens, nothing can be seen, it's all empty...\nI feel strange in this place ")
                current_room.describe()
                get_to_previous_room = input("> ")
            if get_to_previous_room == "reuse":
                current_room = last_room
                print(f"\nFiuu... I couldn't breathe, I thought I would get stuck there forever."
                      f"\nI'm back to the {last_room.name}."
                      f"\nWait a moment something has changed, my hands are old. "
                      f"That time machine must have messed up with time. "
                      f"Let's drink some water.\n"
                      f"To drink type 'water'.")

    elif command == "drop":
        # Leave an item you have in your backpack.
        if not backpack:
            print("Your backpack is empty.")
        if backpack:
            print(f"\nWhich item do you wanna leave?"
                  f"\nYou have a:")
            for item in backpack:
                print(f"- {item.name}")
            print(f"\nType the name of the item you wanna leave.")
            drop_item = input("> ")
            for item in backpack:
                if drop_item != item.name:
                    print(f"\nI can't find any {drop_item}")
                if drop_item == item.name:
                    print(f"\nOK! I'll leave it here!"
                          f"\nThe {item.name} is now in the {current_room.name}.")
                    current_room.set_item(item)
                    backpack.remove(item)

    elif command == "water":
        print("I feel weak."
              "\nI'll go for a nap.")
        break
    elif command == "exit":
        # Terminating the game
        print("See you soon!")
        break

        # Look hot to highlight or annotate
        # Look hot to highlight or annotate
