import random

while True:
    option = input("Do you want to roll the dice? (y/n): ").lower()
    if option == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Die 1: {dice1}")
        print(f"Die 2: {dice2}")
    elif option == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid response. Please enter 'y' or 'n'.")

#if user enters 'y'
#generate random number
#print them
#if user enters 'n'
#print goodbye message
#exit
#else print invalid response