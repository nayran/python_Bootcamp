import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99")
print("to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
x = input("What's your guess between 1 and 99? ")
att = 1
rand = random.randint(1, 99)
correct = 0
while(x != 'exit'):
    if x.isdigit() is False:
        print("That's not a number.")
    elif(int(x) == rand and att == 1):
        print("You're lucky!")
        correct = 1
    elif(int(x) == rand):
        print("Congrats! %d attempts" % att)
        correct = 1
    elif(int(x) < rand):
        print("Too low!")
    elif(int(x) > rand):
        print("Too high!")
    if(correct == 1 and rand == 42):
        print("The answer to everything is 42.")
    x = input("What's your guess between 1 and 99? ")
    att += 1
print("Goodbye!")
