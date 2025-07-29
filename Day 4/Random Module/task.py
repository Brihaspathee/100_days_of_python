import random
import myModule

value: int = random.randint(1,100)
print(value)
print(myModule.my_favourite_number)

float_value: float = random.uniform(1,100)
print(float_value)

value = random.randint(1,100)
if value % 2 == 0:
    print("Tails")
else:
    print("Heads")

