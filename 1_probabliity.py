import random as rand
probability = {}
for i in range(1,101):
    probability[i] = 0
for i in range(1,101):
    number = rand.randint(1,100)
    probability[number] = probability[number] + 1
    print(str(number), end= " ")
print("")
print(probability)