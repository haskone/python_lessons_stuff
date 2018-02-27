import random

with open("data.txt", "w+") as f:
    for i in range(int(1e3)):
        # f.write(f"{random.randint(100, 999)}\n")
        f.write(f"{i}")
