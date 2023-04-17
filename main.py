import random
print("Totally Random one-thousand-to-one")
print()
count = 1
my_number = random.randint(1,1000)
while True:
    guess = int(input("What is your guess?: "))
    if guess< my_number:
        count += 1
        print("Too low")
    elif guess > my_number:
        count += 1
        print("Too high")
    elif guess== my_number:
        count += 1
        print("Correct!")
        print()
        print(f"It took you {count} guesses to get the correct number")
        print()
        play=input("Type 'run' to try again with a different number: ")
        print()
        if play!="run":
          break
        else:
          my_number=random.randint(1,1000)
          count=1
          continue

