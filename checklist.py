# agile development: "allows for a project to rapildy improve by constant iteration"
# waterfall: "have an entire project built to perfection before being released"
# user stories
# create, read, update, and destroy
# data type: "classification that specifies the kind of data that exists somewhere"

# assign items to list
# declare variable
# can also be written as checklist = []

checklist = [] # creates empty list object/puts it in memory
# checklist.append("Blue") runs code within that object
# print(checklist) prints entire list to the console
# checklist.append("Orange") runs the same append code 
# print(checklist) prints list

# function: "a collection of code that allows for reuse"
# "functions accept any number values as parameters or inputs"
# "every line below the functino declaration must be indented"
# function declaration: "the line that tells python the name of the function along with any parameters it needs"

# create
def create(item):
    checklist.append(item)
    # create item code here

# read
def read(index):
    item = checklist[index]
    return item
    # read code here

# update
def update(index, item):
    checklist[index] = item
    # update code here

# destroy
def destroy(index):
    checklist.pop(index) # pop removes last item in list
    # destroy code here

# list item
# loop over every item in the checklist
def list_all_items():
    index = 0
    for list_item in checklist: # do something
        print("{} {}".format(index, list_item))
        index += 1

# mark completed
def mark_completed(index):
    item = checklist[index] # add code here that marks an item as completed 
    update(index, "√" + item)

def unmark_completed(index):
    checklist.pop("√")
    

# user_input
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input
    user_input = input(prompt).lower().upper()
    return user_input

# select
def select(function_code):
    # create item
    if function_code == "C":
        input_item = user_input("Item you want to add: ")
        create(input_item)
    # read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        if len(checklist) > int(item_index):
            read(int(item_index)) # item_index must exist or program will crash
        else:
            print("Sorry index doesn't exist. Please innput again: ")
    # destroy
    # removes item in list
    elif function_code == "D":
        item_index = user_input("Which index would you like to delete: ")
        if len(checklist) > int(item_index):
            destroy(int(item_index))
        else:
            print("Sorry index doesn't exist. Please innput again: ")
    # place checkmark
    elif function_code == "CM":
        item_index = user_input("Which index would you like to checkmark: ")
        if len(checklist) > int(item_index):
            mark_completed(int(item_index))
        else:
            print("Index not found. Please input again: ")
    # un-check checkmark
    elif function_code == "UC":
        item_index = user_input("Which index would you like to un-checkmark: ")
        if len(checklist) < int(item_index):
            unmark_completed(int(item_index))
        else:
            print("Index not found. Please input again: ")
    # update items from index
    elif function_code == "U":
        item_index = user_input("Which index would you like to update: ")
        if len(checklist) > int(item_index):
            item_index = user_input("Input update: ")
            update(int(item_index))
        else:
            print("Sorry index does not exist. Please select again: ")
     # print items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False # where we want to stop the loop
    # catch all
    else:
        print("Unknown Option")
    return True
    
# test
def test():
    create("violet hat")
    create("blue sweater")
    create("indigo shirt")
    create("green jeans")
    create("yellow jacket")
    create("orange shorts")
    create("red socks")
   


    #print(read(0))
    # print(read(1))
    # update(0, "purple socks")
    # destroy(1)
    # print(read(0))
    # list_all_items() // keeps running

test()

# while loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, and P to display list, U to update list, D to delete an item from list, CM to place a checkmark on index, UC to remove checkmark from index: ")
    running = select(selection)




    

    
