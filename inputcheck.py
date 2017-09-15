"""input test"""

player = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Player 1'
}

enemy = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Player 1'
}

def update_name(entity):
    print("enter a name for your entity")
    new_name = input()
    entity['name'] = new_name
    return entity

update_name(player)
print(player)
update_name(enemy)
print(player, enemy)
