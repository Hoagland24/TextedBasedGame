#Sean Hoagland
user_input = input()
current_room = "Bathroom"
inventory = []


def intro():
    print('You are in school and a bully beat you up and hid your personal items throughout the school.\nYou must go to each room and find all 6 items before you get to the main entrance which is where the bully is.\nIf you do not collect all 6 items before getting to him he will beat you up again.\nIn order to move to different rooms type: North, East, South or West.\nTo add an item to your inventory just type the name of the item as it is written, ex. Shirt.\nDo not pick up the same item twice or you will lose the game.\n')
    return


intro()


def in_room(room, direct):
    where_to = rooms[room]
    print("moving to room {}".format(where_to[direct]))
    print("------------------")
    return where_to[direct]


rooms = {
    "Computer Lab": {'South': 'Math Class', 'East': 'Bathroom', 'Item': "Shorts"},
    "Bathroom": {'West': 'Computer Lab', 'Item': ''},
    "Math Class": {'North': 'Computer Lab', 'West': 'Library', 'Item': "iPod"},
    "Library": {'South': 'Main Entrance', 'East': 'Math Class', 'West': 'Science Class', 'North': 'Cafeteria',
                'Item': "Backpack"},
    "Main Entrance": {'North': 'Library', 'Item': "Bully"},
    "Science Class": {'East': 'Library', 'Item': "Cell Phone"},
    "Cafeteria": {'South': 'Library', 'East': 'Gymnasium', 'Item': "Shirt"},
    "Gymnasium": {'West': 'Cafeteria', 'Item': "Shoes"}
    }


item = rooms[current_room]['Item']


def instructions(room):
    print("You are in the {}".format(current_room))
    print("Inventory: {}".format(inventory))
    item = rooms[current_room]['Item']
    for i in item:
        if i in item:
            print("There's my {}".format(item))
            break
        elif i not in item:
            break
    print('---------------')
    print("To stop playing enter 'Exit'")
    print("Enter your next move: ")
    for i in item:
        if user_input == item:
            inventory.append(item)
            print('Adding {} to your inventory'.format(item))
            print("Press Enter to continue: ")
            break
        break
    if current_room == "Main Entrance":
        if len(inventory) == 6:
            print("Congratulations, you gathered all 6 items! You beat the bully!")
            inventory.append("Bully")
        elif len(inventory) != 6:
            print("*Punch! *Punch!\nThe Bully beat you up and scattered your things again...\nThanks for playing!")
            inventory.append("Bully")


stop = 'go'
while stop != 'Exit':
    user_input = input(instructions(current_room))
    if "Bully" in inventory:
        user_input = "Exit"
    if user_input == 'Exit':
        print('Thanks for playing, hope you enjoyed it!')
        break
    elif user_input not in rooms[current_room]:
        print("-----------")
        continue
    if current_room == 'Bathroom':
        current_room = in_room("Bathroom", user_input)
    elif current_room == 'Computer Lab':
        current_room = in_room("Computer Lab", user_input)
    elif current_room == 'Math Class':
        current_room = in_room("Math Class", user_input)
    elif current_room == 'Library':
        current_room = in_room("Library", user_input)
    elif current_room == 'Main Entrance':
        current_room = in_room("Main Entrance", user_input)
    elif current_room == 'Science Class':
        current_room = in_room("Science Class", user_input)
    elif current_room == 'Cafeteria':
        current_room = in_room("Cafeteria", user_input)
    elif current_room == 'Gymnasium':
        current_room = in_room("Gymnasium", user_input)
    continue


