#bryanvaughanduke
import random
from time import sleep


# print("This is a magic 8 ball game")
# print("Please ask me a question?")

# question = input()

# sleep(1)
# randnum = random.randint(1,9)
# print(randnum)
#


def intro():
    return input('This is a magic 8 ball game...Think of a question.... and hit enter')

def get_input():
    """this function gets user input"""

    return get_fortune

def get_randnum():
    """this function gets a random number"""
    randnum = random.randint(1,9)
    return randnum

def get_fortune(randnum):
    if randnum == 1:
        fortune = "it is certain"
        return fortune
    elif randnum == 2:
        fortune = "Outlook good"
        return fortune
    elif randnum == 3:
        fortune = "Outlook bad"
        return fortune
    elif randnum == 4:
        fortune = "Outlook is hazy"
        return fortune
    elif randnum == 5:
        fortune = "You may rely on it"
        return fortune
    elif randnum == 6:
        fortune = "Ask again later"
        return fortune
    elif randnum == 7:
        fortune = "Are you for real?"
        return fortune
    elif randnum == 8:
        fortune = "My reply is no"
        return fortune
    elif randnum == 9:
        fortune = "Are you really sure about that?"
        return fortune

# get fourtun based on random number
# show user fortune

def main():
    intro()
    sleep(1)
    randnum = get_randnum()
    output = get_fortune(randnum)
    print(output)

main()
