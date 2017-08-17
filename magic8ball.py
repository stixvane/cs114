import random
from time import sleep

print("This is a magic 8 ball game")
print("Please ask me a question?")

question = input()

sleep(1)

randnum = random.randint(1,9)
print(randnum)

if randnum == 1:
    print("fortun one")

# elif randnum == (1):
#     print("it is certain")

elif randnum == (2):
    print("Outlook good")

elif randnum == (3):
    print("Outlook bad")

elif randnum == (4):
    print("Outlook is hazy")

elif randnum == (5):
    print("You may rely on it")

elif randnum == (6):
    print("Ask again later")

elif randnum == (7):
    print("Are you for real?")

elif randnum == (8):
    print("My reply is no")

elif randnum == (9):
    print("My sources say hell no")
