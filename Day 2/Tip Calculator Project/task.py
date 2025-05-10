print("Welcome to the tip calculator!")
bill: float = float(input("What was the total bill? $"))
tip: int = int(input("What percentage tip would you like to give? 10 12 15 "))
people: int = int(input("How many people to split the bill? "))
payment: float = (bill + (bill * (tip / 100)))/people
payment = round(payment, 2)
print(f"Each person should pay: ${payment}")


