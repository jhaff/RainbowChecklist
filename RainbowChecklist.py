checklist = list()

#Takes an item + adds to end of list
def create(item):
    checklist.append(item)

#Read function, takes an index + returns the item at specified index
def read(index):
    return checklist[index]

#Update function changes item at specified index
def update(index, item):
    checklist[index] = item

#Destroy function, deletes item at specified index
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()


test()
