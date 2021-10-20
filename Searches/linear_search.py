# Simple linear search 1

def linear_search(lst, target):
    for i in range(len(lst)):
        if(lst[i] == target):
            return i
    return -1

# Simple linear search 2

def l_search(lst, target):
    found = False
    counter = 0
    while found== False and counter < len(lst):
        if lst[counter] == target:
            found = True
        counter += 1

    if found == True:
        print("Target",target,"found at location",counter-1)  

l_search([5,4,10,20,5],20)