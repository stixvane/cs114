import random
import sys
import time

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
    item_list = ["MRE", "First Aid Kit", "Meth-derived stim-pack"]

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
        print("You wake up from Cryo-Sleep.")
        print ("")
        print("Your head is pounding from the alarms and you cant remember your name.")
        print("")
        print("enter a name for your character and hit <[Return/Enter]>")
        new_name = input()
        character['name'] = new_name
        return character
    def next_scene(next1):
        next1=print("placing your hands to your head,", character['name'], "thats my name!", character['name'], "You say to yourself as you get your barrings. With the alarm sounding you must make it to the bridge to get the damage report and shut off the alarm.")
        print("")
        print(",player['name'], Makes your way up the hall when you hear something comeing, Fearing it may take you out you attack")
        return next1

    update_name(player)
    print(player)

    # print(next1)

    # print(reaction)
    # update_name(player)
    # print(player)
        # update_name(enemy)
        # print(player, enemy)

    # get_item(player)
    print('encounter 1...\n\n')
    encounter(player, enemy3)
    print("you make your way up a hall")
    print('encounter 2...\n\n')
    encounter(player, enemy2)
    print('encounter 3...\n\n')
    encounter(player, enemy1)
    print("You've made it to the space pod and eject... The space station explodes as you look back..... now.....now the darkness of space inbraces you.", player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
