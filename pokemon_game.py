import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    # print(pokemon['name'])
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defend': pokemon['stats'][2]['base_stat']
    }

def stats(my_stat, opponent_stat):
    if my_stat > opponent_stat:
            print('You win!')
            my_scored = 100
            opponent_scored = 0
    elif my_stat < opponent_stat:
            print('You Lose :(')
            my_scored = 0
            opponent_scored = 100
    else:
            print('Draw!')
            my_scored = 50
            opponent_scored = 50

    score_dictionary = {'my_scored': my_scored, 'opponent_scored': opponent_scored}
    print(score_dictionary)
    return score_dictionary

def fight(stat_choice, my_pokemon, opponent_pokemon):
    if stat_choice == 'attack':
        print("{} is attacking {}".format(my_pokemon_name, opponent_pokemon_name))
        the_score = stats(my_pokemon['attack'], opponent_pokemon['defend'])
    elif stat_choice == 'defend':
        print("{} is attacking {}".format(opponent_pokemon_name, my_pokemon_name))
        the_score = stats(my_pokemon['defend'], opponent_pokemon['attack'])


    return the_score

def game(my_score, opponent_score):
    my_pokemon = random_pokemon()
    opponent_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    player_or_opponent = input("Would you like to choose the stat or let the opponent? me/opponent: ")
    if player_or_opponent == 'me':
        stat_choice = input('Would you like to attack or defend from your opponents attack?: ')
    else:
        number = random.randint(1, 2)
        if number == 1:
            stat_choice = 'attack'
            print("Stat choice is {}".format(stat_choice))
        elif number == 2:
            stat_choice = 'defend'
            print("Stat choice is {}".format(stat_choice))

    global opponent_stat
    opponent_stat = opponent_pokemon[stat_choice]
    print(opponent_stat)
    global my_stat
    my_stat = my_pokemon[stat_choice]
    print(my_stat)
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    global my_pokemon_name
    my_pokemon_name = my_pokemon['name']
    global opponent_pokemon_name
    opponent_pokemon_name = opponent_pokemon['name']


    score = fight(stat_choice, my_pokemon, opponent_pokemon)

    return score


final_results = {'my_score': 0, 'opponent_score': 0, }
while True:
    my_scored = 0
    opponent_scored = 0
    game_play = game(my_scored, opponent_scored)
    final_results['my_score'] += game_play['my_scored']
    final_results['opponent_score'] += game_play['opponent_scored']
    print("Your points: " + str(final_results['my_score']))
    print("Opponents points: " + str(final_results['opponent_score']))
    if (final_results['my_score'] or final_results['opponent_score']) >= 1000:
        break
