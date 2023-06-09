import Games.ConnectFour as ConnectFour

def find_game(games, game_name):
        for key, value in games.items():
            if key == game_name:
                return value

def choose_game(games):
    chosen_game_name = ""
    while chosen_game_name not in [game_name for game_name in games.keys()]:
        print(', '.join(games.keys())) 
        chosen_game_name = input("Choose one above: ")
    return chosen_game_name

def play_on_loop(games):
    print("What game do you want to play: ")
    chosen_game_name = choose_game(games)
    game_to_play = find_game(games, chosen_game_name)
    game_to_play.play()
    while choice.title() not in ["Yes", "No"]:
        choice = input("Do you want to continue playing:")
        print("Yes || No")
    if choice == "No":
        print("See you next time.")
        return
    play_on_loop(games)

def play_games(games):
    print("================================================")
    choice = ''
    while choice.title() not in ["Yes", "No"]:
        choice = input("Do you want to play games today:")
        print("Yes || No")
    if choice == "No":
        print("See you next time.")
        return
    play_on_loop(games)
    
    
    
    
    
games = {}
cf = ConnectFour()
games['Connect Four'] = cf
play_games(games)