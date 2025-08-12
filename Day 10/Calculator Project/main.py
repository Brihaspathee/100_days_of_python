def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

def calculate(num1: float, num2: float, operation:str):
    operation_function = operations[operation]
    ans = operation_function(num1, num2)
    return ans



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

switch_off:bool = False
while not switch_off:
    num_1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)
    operator = input("Pick an operation: ")
    num_2 = float(input("What is the second number: "))
    answer = calculate(num_1, num_2, operator)
    print(f"{num_1} {operator} {num_2} = {answer}")
    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    while continue_calculating == "y":
        num_2 = float(input("What is the next number: "))
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        answer = calculate(answer, num_2, operator)
        print(f"{answer} {operator} {num_2} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    exit_calc: str = input("Do you want to exit? Type 'y' for yes and 'n' for no:")
    if exit_calc == "y":
        switch_off = True
    else:
        print("New calculation started.")


