import random
print("Hello World!")
#adjust the program to print Hello World with
#a random amount of "o"'s in Hello

ans = input("Print again? ")

while ans != "":
    oNum = random.randint(1,25)
    print(f"Hell{oNum * 'o'} World!")
    ans = input("Print again? ")