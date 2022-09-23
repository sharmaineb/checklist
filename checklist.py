# agile development: "allows for a project to rapildy improve by constant iteration"
# waterfall: "have an entire project built to perfection before being released"
# user stories
# create, read, update, and destroy
# data type: "classification that specifies the kind of data that exists somewhere"

# assign items to list
# declare variable
# can also be written as checklist = []

checklist = list() # creates empty list object/puts it in memory
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
    checklist.pop(index)
    # destroy code here

# list item
# loop over every item in the checklist
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# mark completed
def mark_completed(index):
    item = checklist[index] # add code here that marks an item as completed 
    update(index, "√" + item)

# user_input
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input
    user_input = input(prompt)
    return user_input

# select
def select(function_code):
    # create item
    if function_code == "C":
        input_item = user_input("Input Item: ")
        create(input_item)
    # read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index) # item_index must exist or program will crash
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
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    
    list_all_items()

# while loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, and P to display list: " )
    running = select(selection)

test()


    

    
