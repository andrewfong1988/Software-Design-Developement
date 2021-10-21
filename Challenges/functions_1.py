# Function challenge 1 - what is the value of the output? 

def f(e):
    return 1-e
z = f(3)
print(f(z))

# Function challenge 2 - what is the value of the output?

def calc(d, z):
    d += 11//z
    return z-z
def h(e, d):
    d += 5//e
    return e+d
z = h(1, 5)
print(calc(z, h(h(4, z), z)))


