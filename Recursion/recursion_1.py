# Example 1 - ulgometh (infinite)

# def ulgometh(x):
#     print(x)
#     ulgometh(x-1)
# ulgometh(5)

# Example 2 - ulgometh (fixed)

def ulgometh(x):
    if x > 0:
        print(x)
        ulgometh(x-1)
ulgometh(5)

Example 3 - lists 
letters = ["A","B","C"]
numbers = [1,2,3]

# def join(letters, numbers):
#     if len(letters)>0:
#         numbers.append(letters[0]) #add the first item of letters to numbers
#         join(letters[1:len(letters)], numbers) # run the join function again but only pass in left over
    
# join(letters, numbers)

# Example 4 - factorials

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# num = 6
# print("The factorial of", num, "is", factorial(num))