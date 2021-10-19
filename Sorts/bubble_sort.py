# a function to sort a list using bubble sort algorithm
def bubblesort(lst):
        # get the length of the list
        n = len(lst)
        # go through the list n number of times
        for i in range(n):
                # variable to keep check for any swaps
                swap = False
                # traverse through all adjacent elements
                for j in range(0, n-i-1):
                    # if current element greater than next element, swap them
                    if lst[j]>lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                        swap = True
                # if no swaps, then break out of the loop
                if swap == False:
                        break
        # print the final sorted list
        print(lst)

# an example unsorted list 
y = [1,5,4,6,7,8,3,2,12,10,9,11]

# function call to sort list y
bubblesort(y)
