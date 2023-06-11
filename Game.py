from ConnectFour import ConnectFour
def find_game(games, game_name):
        for key, value in games.items():
            if key.lower() == game_name:
                return value

def choose_game(games):
    chosen_game_name = ""
    print("Games: ")
    for i in range(len(games)):
        print(f'\t{i+1}. {games[i].name}')
    chosen_game_name = int(input("Choose one above: "))
    while chosen_game_name not in list(range()):
        print("Not an available game. Please choose again.")
        print("Games: ")
        for i in range(len(games)):
            print(f'\t{i+1}. {games[i].name}')
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


games = []
cf = ConnectFour()
games.append(cf)
play_games(games)