# To Create a Fibonacci sequence Using Recursion:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# Recurssion:

def fibonacci(length):
    if(length <= 1):
        return length
    else:
        return (fibonacci(length-1) + fibonacci(length-2))

for i in range(length):
    print(fibonacci(i))


# While_loop:

x = 0
y = 1
iteration = 0

if length == 1:
    print(x)
else:
    while iteration < length:
        print(x, end=', ')
        x, y = y, (x+y)
        iteration += 1
