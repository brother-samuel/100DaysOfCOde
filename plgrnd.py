
digits = input("Enter a number: ")

def persitence(n):
    count = 0
    while len(str(n)) > 1:
        result = 1
        for d in str(n):
            result *= int(d)
            n = result
        count +=1
    print(n)

persitence(digits)