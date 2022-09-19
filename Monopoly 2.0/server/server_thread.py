import socket, time, pickle
from _thread import *
from game import Game
from game_factory import Game_Factory



create_game = Game_Factory('first game')
game = create_game.get_game()
players = game.get_players()


server = '127.0.0.1'  #'192.168.1.68'   #'10.34.196.211' 
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")


def authentication_thread(conn, player):
    '''
    setups up the thread that connects the server to the client
    input: player- player object
    returns: None
    '''
    conn.send(pickle.dumps(player))
    while True:
        try:    # FOR INITIAL CONNECTION- SENDING PLAYER AND GAME OBJECT
            data = pickle.loads(conn.recv(2048))
            reply = ''

            if not data:
                break
            elif data == 'get': # GET GAME
                reply = game
            elif data == 'start':
                reply = game_started
            elif data == 'reset':
                pass    #TODO sort out game reset
            elif data == 'players_turn':
                if player.get_name() == game.get_players()[0].get_name():
                    reply = True
                else:
                    reply = False
            elif data == 'TURBO +1':
                game.set_num_voted_turbo(1)  
            elif data == 'TURBO -1':
                if game.get_num_voted_turbo() > 0:
                    game.set_num_voted_turbo(-1)
                else:
                    game.set_delay(0.25)
            elif data == 'Houses':
                if game.get_button_pressed() == '':
                    game.set_player_buying_houses(player)
                    game.set_button_pressed('Houses')
            else:
                if game_started:
                    if game.get_player_buying_houses() != None:
                        if player == game.get_player_buying_houses():
                            print('previous button pressed - ', game.get_button_pressed())
                            if game.get_button_pressed() == '':
                                game.set_button_pressed(data)
                                print("button pressed - ", data)
                                print("button_pressed set to ", game.get_button_pressed())
                                print("sent ", reply)
                    else:
                        if player.get_name() == game.get_players()[0].get_name():  # LOOP FOR PLAYER'S TURN
                            print('previous button pressed - ', game.get_button_pressed())
                            if game.get_button_pressed() == '':
                                game.set_button_pressed(data)
                                print("button pressed - ", data)
                                print("button_pressed set to ", game.get_button_pressed())
                                print("sent ", reply)
                        else:
                            reply = "Observing player" #TODO HIGHLIGHT BUTTON PRESSED

            # print("[RECEIVED] :", player.get_name(), " :", data)
            # print("[SENDING] :", player.get_name(), " :", reply)
            
            conn.sendall(pickle.dumps(reply))


        except:
            break

    print("[DISCONNECTED] :", player.get_name())
    conn.close()




game_started = False
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("\n[CONNECTED] :", addr)
    start_new_thread(authentication_thread, (conn, players[currentPlayer]))
    if currentPlayer == 0: #TODO CHANGE BACK TO 3
        break
    currentPlayer += 1

time.sleep(1)
print("\n\n3 PLAYERS CONNECTED- GAME STARTED") #TODO delay game starting until all connected players have received game once to set up Game_Player objects


game_started = True
create_game.start_game()