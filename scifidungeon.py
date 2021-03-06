import random
import sys

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
'name': 'Cyborge Mutant'
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
    print("GAME OVER -- ", player['name'], "You and everyone on The Hurcules Star base are dead, dessicated carbon. Decades\
     from now a scientific survey vessel will stumble across T.H.S.B. and investigators\
     will log the incident.")
    return sys.exit()

# have attack have effect the battles outcome

# have deffense have an effect on the battles outcome


def get_item(player):
    item_list = ["MRE", "First Aid Kit", "Meth-derived stim-pack"]

    print("You find a ", item_list[random.randint(0, 2)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    # player['HP'] += (abs(player['HP'] - 100))
    player['HP'] = 100
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



"""there are 4 encounters, each encounter offers an option to
open a door, the door will either have an enemy or an item"""


def main():
            # Player wakes up and makes a choice for name)
    # def start(begining):
    #     print('You wake up from cryo-sleep. Your head is pounding from the alarms and cant remembering what your name.')
    #     return beginging
    # def your_name(players_name):
    #     plyers_name = input
    #     input == players_name
    #     print ('Choose your name ________')
    #     return players_name
    #     print('placing your hands to your head,+(str("players_name") +, thats my name!, +(str("players_name")), You say to yourself as you get your barrings. With the alarm sounding you must make it to the bridge to get the damage report and shut off the alarm.')
    #     return players_name
    # fight(player, enemy1)

    # get_item(player)
    print('encounter 1...\n\n')
    
    encounter(player, enemy3)

    print('encounter 2...\n\n')

    encounter(player, enemy2)

    print('encounter 3...\n\n')

    encounter(player, enemy1)

    print("YOU HAVE ESCAPED -- WINNER", player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
