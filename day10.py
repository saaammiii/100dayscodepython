from day10art import logo

# calculator
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

# dict key symbol,val names of sym
operations = {
    '+': add,
    '-': subtract,
    '*': multi,
    '/': div
}

def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))
    continue_function=True
    for symbol in operations:
        print(symbol)

    while continue_function:

        operation_sym = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        operation_value = operations[operation_sym]
        answer=operation_value(num1,num2)
        print(f"{num1} {operation_sym} {num2} = {answer}")

        res=input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' to start new calculations.: ")
        if res=='y':
            num1=answer
        elif res=='n':
            continue_function=False
            exit
        else:
            continue_function=False
            calculator()

calculator()
