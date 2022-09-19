import pickle

a = pickle.dumps(-1)

print(pickle.loads(a))


'''
with open('data.pkl', 'rb') as rf:
    z = pickle.load(rf)
    print(vars(z))

    for player in z.get_players():
        print(player.get_money())
'''


'''

p1 = Player('p1', 0, 1500)
p2 = Player('p2', 0, 1500)
p3 = Player('p3', 0, 1500)
p4 = Player('p4', 0, 1500)

new_game.add_player(p1)
new_game.add_player(p2)
new_game.add_player(p3)
new_game.add_player(p4)

#database = {'CHIN': [16, 556, {11: 4, 13: 4, 14: 4, 21: 0.0, 25: 1, 35: 1}, ['Pink'], 0, 0], 'KALE': [11, 14, {6: 3, 8: 3, 9: 3, 26: 0, 27: 0, 29: 0}, ['Light Blue', 'Yellow'], 0, 0], 'BAGGY': [32, 704, {23: 0.0, 24: 0.0, 31: 1, 32: 1, 34: 1}, ['Green'], 0, 0], 'ROARLIKELEO': [13, 117, {15: 0.0, 16: 3, 18: 3, 19: 3}, ['Orange'], 0, 0], 'GIAN': [12, 314, {1: 5, 3: 5, 5: 0, 12: 1, 28: 1, 37: 0, 39: 0}, ['Brown', 'Dark Blue'], 0, 0]}

p1.set_property('', '', {11: 4, 13: 4, 14: 4, 21: 0.0, 25: 0, 35: 0})
p2.set_property('', '', {6: 3, 8: 3, 9: 3, 26: 0, 27: 0, 29: 0})
p3.set_property('','', {23: 0.0, 24: 0.0, 31: 1, 32: 1, 34: 1})
p4.set_property('' ,'', {15: 0.0, 16: 3, 18: 3, 19: 3})


p1.set_streets('', ['Pink'])
p2.set_streets('', ['Light Blue', 'Yellow'])
p3.set_streets('', ['Green'])
p4.set_streets('', ['Orange'])

'''