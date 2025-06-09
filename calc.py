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
result = None

while calculating:
    if result == None:
        n1 = float(input("What\'s the first number?: "))
    else:
        use_result = input(f"Type 'y' to continue calculating with {result} or type 'n' to start anew or 'q' to quit: ").lower()
        if use_result == "y":
            n1 = result
        elif use_result == "n":
            n1 = float(input("What\'s the first number?: "))
        else:
            calculating = False

    operator = input("+\n -\n *\n /\n Pick an operation: ")
    n2 = float(input("What\'s the next number?: "))
    result = operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
