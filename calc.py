def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
calculating = True

while calculating:
    n1 = int(input("What\'s the first number?: "))
    operator = input("+\n -\n *\n /\n Pick an operation")
    n2 = int(input("What\'s the next number?: "))

    if operator == "+":
        print(operations["+"](n1,n2))