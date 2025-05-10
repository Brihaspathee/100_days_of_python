print("Modulo operator")
input_number: int = int(input("What is your number? "))
remainder: int = input_number % 2
if remainder == 0:
    print("Number is even")
else:
    print("Number is odd")