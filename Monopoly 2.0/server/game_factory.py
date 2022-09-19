import pickle
from game import Game

class Game_Factory():
    def __init__(self, name):
        self.name = name
        self.game = None #     actual game object
        self.create_new_game(name)

    def get_game(self):
        return self.game

    def create_new_game(self, name):
        while True:
            ans = input("\n\nDo you want to start a new game (S) or continue a previous game (C)?    ")

            if ans == 'S':
                self.game = Game(name)
                break

            elif ans == 'C':
                with open('data.pkl', 'rb') as rf:
                    z = pickle.load(rf)
                    self.game = z
                break

            else:
                print("Invalid input.")

    def start_game(self):
        self.game.start_game()
    