from ConnectFour import ConnectFour
from Caro import Caro

def find_game_by_name(games, name):
    for game in games:
        if game.name.lower() == name:
            return game

def choose_game(games):
    chosen_game_index = 0
    index_bol = False
    chosen_game_name = ''
    quit_index = len(games)+1
    print("Games: ")
    for i in range(len(games)):
        print(f"\t{i+1}. {games[i].name}")
    print(f"\t{quit_index}. QUIT")
    print(f"Choose one above (or enter {quit_index} to quit): ")
    chosen_game_str = input()
    try:
        chosen_game_index = int(chosen_game_str) - 1
        if chosen_game_index == quit_index - 1:
            print("See you next time.")
            return None
        index_bol = True
    except ValueError:
        chosen_game_name = chosen_game_str.lower()
        if chosen_game_name == 'quit':
            print("See you next time.")
            return None

    if chosen_game_name not in [game.name.lower() for game in games] and chosen_game_index not in range(len(games)):
        print("Not an available game. Please choose again.")
        choose_game(games)
    else:
        if index_bol:
            return games[chosen_game_index]
        else:
            return find_game_by_name(games, chosen_game_name)

def play_on_loop(games):
    print("What game do you want to play: ")
    game_to_play = choose_game(games)
    if game_to_play == None:
        return
    game_to_play.play()
    choice = ''
    while choice not in ["yes", "no"]:
        choice = input("Do you want to continue playing:\nYes || No\n").lower()
    if choice == "no":
        print("See you next time.")
        return
    play_on_loop(games)

def play_games(games):
    print("================================================")
    choice = ''
    while choice not in ["yes", "no"]:
        choice = input("Do you want to play games today:\nYes || No\n").lower()
    if choice == "no":
        print("See you next time.")
        return
    play_on_loop(games)


games = []
cf = ConnectFour()
xo = Caro()
games.append(cf)
games.append(xo)
play_games(games)