# Control Flow 1 - What is the value of b after execution?

e = 5
b = 1
for counter in range(e, e+4):
    b += counter-4
print(b)

# Control Flow 2 - What is the value of x after execution?

x = 4
val = 5
for it in range(0, 4):
    x += it*3
print(x)


# Control Flow 3 - What is the value of x after execution?

v = 2
b = 5
for counter in range(0, 5):
    v = b**2
v -= b//2
print(v)
