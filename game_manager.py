from game import Game


def selection_Menu():

    while True:
        choice = input("Y to play, Q to quit: ").lower()
        if choice == "y" or choice == "q":
            break
        print("Not a valid choice!")

    return choice


def create_Game():
    my_Game = Game()
    my_Game.play_Game()


while True:
    choice = selection_Menu()
    if choice == "q":
        break

    create_Game()
