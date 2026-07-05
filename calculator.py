print("""logo = r'''
 _____
|  _____  |
| | Python Calc    | |
| |_____| |
|  _ _ _   _  |
| | 7 | 8 | 9 | | + | |
| |_|_|_| |_| |
| | 4 | 5 | 6 | | - | |
| |_|_|_| |_| |
| | 1 | 2 | 3 | | * | |
| |_|_|_| |_| |
| | 0 | . | = | | / | |
| |_|_|_| |_| |
|______|
'''""")
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    first_number = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation = input("Pick an operation: ")

        second_number = float(input("What's the next number?: "))

        calculation_function = operations[operation]

        answer = calculation_function(first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        if choice == "y":
            first_number = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
while should_continue :
      operations = input("pick an operation: ")
      second_number = float(input("whats the next number?:"))
      calculation_fuction = operations
   
  