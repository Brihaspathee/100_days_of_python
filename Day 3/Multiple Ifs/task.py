print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill: int = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        # print("Please pay $5.")
    elif age <= 18:
        bill = 7
        # print("Please pay $7.")
    else:
        bill = 12
        # print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No. ")
    print(wants_photo)
    if wants_photo == "y":
        print("Your photo was taken")
        bill = bill + 3

    print(f"Your bill is: {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
