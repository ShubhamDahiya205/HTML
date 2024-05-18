import random, sys
print("Check How random the \"random\" module really is.")
while True:
    try:
        upper = int(input("Enter upper limit: "))
    except:
        print("Enter a number!")
        continue  
    if upper >1 :
        probability = {}
        for i in range(1,upper+1):
            probability[i] = 0
        for i in range(1,upper+1):
            number = random.randint(1,upper)
            probability[number] = probability[number] + 1
        print(probability)
        user_choice = input("Enter \"exit\" to exit or press enter to continue : ")
        if user_choice == "exit":
            sys.exit()    
    else:
        print("Number should be > 1")
        pass