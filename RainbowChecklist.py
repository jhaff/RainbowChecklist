# -*- coding: utf-8 -*-

checklist = list()

#Takes an item + adds to end of list
def create(item):
    checklist.append(item)

#Read function, takes an index + returns the item at specified index
def read(index):
    Print(checklist[int(index)])

#Update function changes item at specified index
def update(index, item):
    checklist[int(index)] = item

#Destroy function, deletes item at specified index
def destroy(index):
    checklist.pop(index)

#Prints all items in the list
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


# marks an item as completed
def mark_completed(index):
    checklist[index] = "√ " + checklist[index]

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        #print('TYPE: {}'.format(type(input_item)))
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number: ")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    elif function_code == "U":
        #asks user for an index number to update and a new string to update it with
        item_index = user_input("Index Number: ")
        updated_item = user_input("Updated Item: ")

        update(item_index, updated_item)


    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print('step 4')
        print("Unknown Option")

    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input.upper()

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

       # Call your new function with the appropriate value
    select("C")
    # View the results
    # list_all_items()
    # Call function with new value
    #select(user_input("Please Enter a value:")

    # View results
    # list_all_items()
    # Continue until all code is run

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, U to update or Q to quit: ")
    running = select(selection)




#test()
