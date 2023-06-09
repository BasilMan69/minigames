import Games.ConnectFour as ConnectFour

def find_game(games, game_name):
        for key, value in games.items():
            if key == game_name:
                return value

def choose_game(games):
    chosen_game_name = ""
    while chosen_game_name not in [game_name for game_name in games.keys()]:
        for game_name in games.keys():
            print(game_name)
        chosen_game_name = input("Choose one above: ")
    return chosen_game_name

def play_games(games):
    choice = ''
    while choice not in ["Yes", "No"]:
        choice = input("Do you want to play games today:")
    print("What do you want to play today: ")
    chosen_game_name = choose_game(games)
    game_to_play = find_game(games, chosen_game_name)
    game_to_play.play()
    
games = {}
cf = ConnectFour()
games['Connect Four'] = cf
play_games(games)