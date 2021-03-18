from art import logo


# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "*": multiply,
    "+": add,
    "/": divide,
    "-": subtract
}


def calculation():
    print(logo)
    should_continue = False
    num1 = float(input("What's the first number?\n"))
    while not should_continue:

        ask_operations = input(' *\n /\n +\n -\n')
        num2 = float(input("What's the second number?\n"))

        call_operator = operations[ask_operations]
        answer = round(call_operator(num1, num2), 3)
        print(answer)
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n").lower() == "y":
            num1 = answer
        else:
            should_continue = True
            calculation()


calculation()
