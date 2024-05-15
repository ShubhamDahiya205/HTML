import random as rand
while True:
    upper = int(input("Enter upper limit"))
    probability = {}
    for i in range(1,upper+1):
        probability[i] = 0
    for i in range(1,upper+1):
        number = rand.randint(1,upper+1)
        probability[number] = probability[number] + 1
    print(probability)
    user_choice = input("Enter \"exit\" to exit")
    if user_choice == "exit":
        break
print("Thanks")