#! python3
import random, sys
print("Welcome to the Randomness Checker!")
print("This program will help you see how random the 'random' module really is.")
print("You will enter an upper limit, and the program will generate random numbers within that limit to see their distribution.")

while True:
    try:
        upper = int(input("Enter the upper limit (must be greater than 1): "))
    except:
        print("Enter a number!")
        continue  
    if upper >1 :
        print(f"\nGenerating random numbers from 1 to {upper}...\n")
        probability = {i: 0 for i in range(1, upper + 1)}
        for i in range(1,upper+1):
            number = random.randint(1,upper)
            probability[number] += 1
        print("Here is the distribution of the generated random numbers:")
        for num, count in probability.items():
            print(f"Number {num}: {count} times")

        user_choice = input("\nEnter 'exit' to exit or press Enter to continue: ").strip().lower()
        if user_choice == "exit":
            print("Exiting the program. Thank you for using the Randomness Checker!")
            sys.exit()    
    else:
        print("The number should be greater than 1. Please try again.")