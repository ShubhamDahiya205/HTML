#! python3
import random

# Main Comment 1 : Defining the strategies (brute force, lucky guess, odd-even run) , user input for guess and function that generates number and runs the strategies

def strategy1(number, lowerrange, upperrange , compare_number):
    # Strat1 : Brute force lower limit to upper limit
    global questionmode
    guess_taken1 = 0
    if questionmode == "div":
        if number % compare_number == 0:
            guess_taken1 = 0
            for i in range(compare_number, upperrange + 1, compare_number):
                guess_taken1 += 1
                if i == number:
                    return guess_taken1            
        else:
            guess_taken1 = 0
            for i in range(lowerrange, upperrange + 1):
                if i % compare_number == 0 :
                    continue
                guess_taken1 += 1
                if i == number:
                    return guess_taken1
    elif questionmode == "compare" :
        if number > compare_number:
            lowerrange = compare_number + 1
        elif number < compare_number:
            upperrange = compare_number - 1
        else:
            return 0
    for i in range(lowerrange, upperrange + 1):
        guess_taken1 += 1
        if i == number:
            return guess_taken1
    
def strategy2(number, lowerrange, upperrange, compare_number):
    # Strat2 : Lucky number guess
    global questionmode
    guess_taken2 = 1
    if questionmode == "div":
        possible_list = list()
        times = 1
        while compare_number*times < upperrange :
            possible_list.append(compare_number*times)
            times += 1
        if number % compare_number == 0 :
            guess_taken2 = 1
            number_guessed = random.choice(possible_list)
            while number_guessed != number :
                guess_taken2 += 1
                possible_list.remove(number_guessed)
                number_guessed = random.choice(possible_list)
            return guess_taken2
        else:
            guess_taken2 = 1
            possible_list = set(possible_list)
            new_possible_list = list()
            for i in range(lowerrange , upperrange +1):
                if i not in possible_list :
                    new_possible_list.append(i)
            number_guessed = random.choice(new_possible_list)
            while number_guessed != number :
                guess_taken2 += 1
                new_possible_list.remove(number_guessed)
                number_guessed = random.choice(new_possible_list)
            return guess_taken2        
    elif questionmode == "compare" :
        if number > compare_number:
            lowerrange = compare_number + 1
        elif number < compare_number:
            upperrange = compare_number - 1
        else:
            return 0
    numbers_guessed = set()
    number_guessed = random.randint(lowerrange, upperrange)
    while number_guessed != number:
        if number_guessed not in numbers_guessed:
            numbers_guessed.add(number_guessed)
            guess_taken2 += 1
        number_guessed = random.randint(lowerrange, upperrange)
    return guess_taken2

def strategy3(number, lowerrange, upperrange, compare_number):
    # Strat3 : Odd Even run
    global questionmode
    guess_taken3 = 0
    if questionmode == "div":
        if number % compare_number == 0 :
            for i in range(compare_number, upperrange, compare_number):
                if i % 2 == 1 :
                    guess_taken3 += 1
                    if number == i :
                        return guess_taken3
            for i in range(compare_number, upperrange, compare_number):
                if i % 2 == 0:
                    guess_taken3 += 1
                    if number == i :
                        return guess_taken3
        else:
            for i in range(lowerrange, upperrange):
                if number % compare_number != 0 :
                    if i % 2 == 1:
                        guess_taken3 += 1
                        if number == i :
                            return guess_taken3
            for i in range(lowerrange , upperrange):
                if number % compare_number != 0:
                    if i % 2 == 0:
                        guess_taken3 += 1
                        if number == i:
                            return guess_taken3
    elif questionmode == "compare" :
        if number > compare_number:
            lowerrange = compare_number + 1
        elif number < compare_number:
            upperrange = compare_number - 1
        else:
            return 0
    for i in range(lowerrange, upperrange + 1):
        if i % 2 == 1:
            guess_taken3 += 1
            if i == number:
                return guess_taken3
    for i in range(lowerrange, upperrange + 1):
        if i % 2 == 0:
            guess_taken3 += 1
            if i == number:
                return guess_taken3
    
def userinputmessage():
    #takes user guesses and choice to skip
    while True:
        try:
            usernumber = input("Enter your guess or press \"s\" to skip: ").strip()
            if usernumber.lower() == "s":
                return None
            else:
                return int(usernumber)
        except ValueError:
            print("Enter valid input")

def run_strats():
    #generates number and runs strategies
    global lowerrange , upperrange, compare_number
    number = random.randint(lowerrange, upperrange)
    guess_taken1 = strategy1(number, lowerrange, upperrange,compare_number)
    guess_taken2 = strategy2(number, lowerrange, upperrange, compare_number)
    guess_taken3 = strategy3(number, lowerrange, upperrange, compare_number)
    return [guess_taken1, guess_taken2, guess_taken3, number]

# Main Comment 2 : Defining variables and the print stuff.

questionmode = 0
compare_number = 1

print("Welcome to the Number Guessing Game!")
print("Try to guess the number as quickly as possible using different strategies.")
print("If you want the number to be from 1 to 20, press 'y'.")
print("If you want a custom range, press 'n'.")
print("If you want to enter question mode, press 'q'.")
print("If you want to enter data mode, press 'd'.")

# Main Comment 3 : Deals with first main input of user.


while True:
    userinput_y_or_n = input("y / n / q / d: ").lower().strip()
    if userinput_y_or_n == "y":
        lowerrange , upperrange = 1, 20
        break
    elif userinput_y_or_n == "n":
        while True:
            try:
                lowerrange = int(input("Enter lower range: "))
                upperrange = int(input("Enter upper range: "))
                if lowerrange > upperrange or lowerrange < 1:
                    print('Enter a valid range')
                    continue
                break
            except ValueError:
                print("Enter integers!")
        break
    elif userinput_y_or_n == "q" :
        print("Question mode will allow you to ask one question about the selected number.")
        print("The question will be asked once, so ask the question which gives you the most information and helps you guess faster.")
        print("In question mode, the number is picked from 1 to 100")
        print("The questions available are :")
        print("compare : you can compare the generated number with any number.")
        print("div : you can check if the generated number is divisible by a number.")
        lowerrange , upperrange = 1, 100
        break
    elif userinput_y_or_n == "d":
        print("Data mode will test each strategy 20 times and give the average number of guesses.")
        print("In data mode, the number is picked from 1 to 100")
        lowerrange , upperrange = 1, 100
        break
    else:
        print("Please enter 'y', 'n', 'q' or 'd' only.")

#Checks userinput mode (y/n/q/d) and proceeds accordingly.

if userinput_y_or_n == "y" or userinput_y_or_n == "n" : 
    Answerslist = run_strats()
    guess_taken1, guess_taken2, guess_taken3, number = Answerslist
    Answers = {"Strat1": guess_taken1, "Strat2": guess_taken2, "Strat3": guess_taken3}
    usernumber = userinputmessage()
    if usernumber is not None:
        userguess = 1
        while usernumber != number:
            print("Wrong, try again.")
            userguess += 1
            usernumber = userinputmessage()
            if usernumber is None:
                break

        if usernumber == number:
            print(f"Correct, you guessed it in {userguess} tries.")
            Answers.update({"YourStrat": userguess})
    
    print(f"The number was {number}")
    print("Strategy Performance:")
    print(f"Your Strategy: {Answers.get('YourStrat', 'N/A')} guesses")
    print(f"Strategy 1 (Brute Force): {Answers['Strat1']} guesses")
    print(f"Strategy 2 (Lucky Guess): {Answers['Strat2']} guesses")
    print(f"Strategy 3 (Odd-Even): {Answers['Strat3']} guesses")

elif userinput_y_or_n == "q" :
    while True:
        questionmode = input("compare or div : ").lower().strip()
        if questionmode == "compare" or questionmode == "div" :
            break
        else:
            print("Enter proper input.")
    while True:
        if questionmode == "compare" :    
            try:
                compare_number = int(input("Enter the number you want to compare it with : "))
                if compare_number <1 or compare_number > 100 :
                    print("Enter a number between 1 and 100.")
                    continue
                break
            except:
                print("Enter an integer.")
        else:
            try:
                compare_number = int(input("Enter the number you want to check its divisibility with : "))
                if compare_number < 1 or compare_number > 100 :
                    print("Enter a number between 1 and 100.")
                    continue
                break
            except:
                print("Enter an integer.")

    Answerslist = run_strats()
    guess_taken1, guess_taken2, guess_taken3, number = Answerslist
    Answers = {"Strat1": guess_taken1, "Strat2": guess_taken2, "Strat3": guess_taken3}
    answerfound = False

    if questionmode == 'div' :
        if number % compare_number == 0:
            print(f"The number is divisible by {compare_number}")
        else:
            print(f"The number is not divisible by {compare_number}")
    else:
        if number > compare_number :
            print(f"The number is greater than {compare_number}")
        elif number < compare_number:
            print(f"The number is less than {compare_number}")
        else:
            print(f"The number is {compare_number}!!")
            answerfound = True
    if answerfound:
        print("Congratulations, you guessed it in the question itself. You guessed it in zero tries.")
        Answers.update({"YourStrat" : 0})
    else:
        usernumber = userinputmessage()
        if usernumber is not None:
            userguess = 1
            while usernumber != number:
                print("Wrong, try again.")
                userguess += 1
                usernumber = userinputmessage()
                if usernumber is None:
                    break
            if usernumber == number:
                print(f"Correct, you guessed it in {userguess} tries.")
                Answers.update({"YourStrat": userguess})
    print(f"The number was {number}")
    print("Strategy Performance:")
    print(f"Your Strategy: {Answers.get('YourStrat', 'N/A')} guesses")
    print(f"Strategy 1 (Brute Force): {Answers['Strat1']} guesses")
    print(f"Strategy 2 (Lucky Guess): {Answers['Strat2']} guesses")
    print(f"Strategy 3 (Odd-Even): {Answers['Strat3']} guesses")          

else:
    Strat1, Strat2, Strat3, number = [], [], [], []
    for i in range(20):
        Answerslist = run_strats()
        Strat1.append(Answerslist[0])
        Strat2.append(Answerslist[1])
        Strat3.append(Answerslist[2])
        number.append(Answerslist[3])
    Strat1_avg = sum(Strat1) / 20
    Strat2_avg = sum(Strat2) / 20
    Strat3_avg = sum(Strat3) / 20
    number_avg = sum(number) / 20
    print("The average number of guesses for each strategy over 20 runs:")
    Answers = {"Strat1": Strat1_avg, "Strat2": Strat2_avg, "Strat3": Strat3_avg}
    print(f"Strategy 1 (Brute Force): {Strat1_avg:.2f} guesses")
    print(f"Strategy 2 (Lucky Guess): {Strat2_avg:.2f} guesses")
    print(f"Strategy 3 (Odd-Even): {Strat3_avg:.2f} guesses")
    print(f"The randomly generated number on average was: {number_avg}")
