from ConnectFour import ConnectFour
def find_game(games, game_name):
        for key, value in games.items():
            if key.lower() == game_name:
                return value

def choose_game(games):
    chosen_game_name = ""
    print("Games: "  +', '.join(games.keys())) 
    chosen_game_name = input("Choose one above: ").lower()
    while chosen_game_name not in [game_name.lower() for game_name in games.keys()]:
        print("Not an available game. Please choose again.")
        print("Games: "  +', '.join(games.keys())) 
        chosen_game_name = input("Choose one above: ").lower()
    return chosen_game_name

def play_on_loop(games):
    print("What game do you want to play: ")
    chosen_game_name = choose_game(games)
    game_to_play = find_game(games, chosen_game_name)
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


games = {}
cf = ConnectFour()
games['Connect Four'] = cf
play_games(games)