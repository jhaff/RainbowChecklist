checklist = list()
checklist.append('Blue')
print(chec  klist)
checklist.append('Orange')
print(checklist)

//Takes an item + adds to end of list
def create(item):
    checklist.append(item)

//Read function, takes an index + returns the item at specified index
def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item
