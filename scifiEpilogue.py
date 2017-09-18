import random
import sys
import time
import colorama
from colorama import Fore




"""text based game where user makes decisions which affect a series of
encounters with 'enemies'"""

player = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Player 1'
}

enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Zombie AI human'
}

enemy2 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Zombie crewman'
}

enemy3 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Pack of zombie mutated dogs'
}


def game_over(player):
    print("GAME OVER -- ", player['name'], "You and everyone on Star-Base Titan are dead, dessicated carbon. Decades\
     from now a scientific survey vessel will stumble across your Star-Base and investigators will log the incident.")
    return sys.exit()


def get_item(player):
    item_list = ["M.R.E.", "First Aid Kit", "Meth-derived stim-pack"]

    print("You find a ", item_list[random.randint(0, 2)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    player['HP'] += (abs(player['HP'] - 100))
    return player


def attack(opponent):
    rand_damage = random.randint(8, 32)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print('player1 oppo1 HP: ', oppo1['HP'])
    print('enemy1  oppo2 HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        input('Press any key to continue')
    elif opponent['name'] == 'Zombie AI human':
        fight(player, opponent)
        # return player
    else:
        get_item(player)
        input('Press any key to continue')



"""there are 4 encounters, each encounter offers an option to open a door,
the door will either have an enemy or an item"""

def main():
    # fight(player, enemy1)
    def update_name(character):
        print("")
        print(Fore.BLUE + "You wake up from Cryo-Sleep.")
        print ("")
        print(Fore.GREEN + "Your head is pounding from the alarms and you cant remember your name.")
        print("")
        print(Fore.BLUE + "Enter a NAME for your character and hit <[Return/Enter]>")
        new_name = input()
        character['name'] = new_name
        return character

# print(Fore.BLUE + "Hello World")
    update_name(player)
    print(player)
    print("")
    print("")
    print(Fore.CYAN + "making your way up the hall you hear something comeing, Fearing it may take you out")
    print("")
    print(Fore.RED + "...YOU ATTACK...")
    print('encounter 1...\n\n')
    encounter(player, enemy3)
    print(Fore.GREEN + ".......you make your way up a hall")
    print(Fore.RED + "...YOU DEFEND YOURSELF AGAIN...")
    print('encounter 2...\n\n')
    encounter(player, enemy2)
    print('encounter 3...\n\n')
    encounter(player, enemy1)
    print(Fore.YELLOW + "You have made it to the space pod and eject")
    print(Fore.GREEN + "The space station explodes as you look back")
    print(Fore.YELLOW + "now,   now the darkness of space imbraces you." , player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
