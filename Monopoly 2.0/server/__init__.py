import pickle

from game_factory import Game_Factory


new_game = Game_Factory('first game')
new_game.game.start_game()

'''
with open('data.pkl', 'rb') as rf:
    z = pickle.load(rf)
    z.start_game()
'''

# TODO      CREATE THREAD TO STORE GAME DATA IN NEW FILE CONSTANTLY, CREATE GAME FACTORY TO CREATE NEW OBJECTS,FIND WAY TO INTERRUPT INPUT WHEN ROUND ENDS, START SERVER CODE