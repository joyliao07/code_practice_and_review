# To Create a Fibonacci sequence Using Recursion:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fibonacci(length):
    if(length <= 1):
        return length
    else:
        return (fibonacci(length-1) + fibonacci(length-2))

for i in range(length):
    print(fibonacci(i))








