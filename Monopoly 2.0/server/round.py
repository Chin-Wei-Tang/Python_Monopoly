import threading, time, pickle

class Round:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.time_left = 30
        self.round_ended = False
        self.stop_thread = False
        if self.game.get_delay() == 0.15:
            self.game.set_delay(0)
        #self.save_game()



    def get_time_left(self):
        return self.time_left

    def get_round_ended(self):
        return self.round_ended

    def timer(self):
        for _ in range(10):
            if self.stop_thread:
                return
            time.sleep(1)
            self.time_left -= 1
            '''
            if self.time_left % 5 == 0:
                print("\n      - - - - - - - - - - - \n      " + str(self.time_left) + " seconds left\n      - - - - - - - - - - - ")
        print("\n      - - - - - - - - - - - - - - - - - - \n      " + "Round is over- 0 seconds left.\n      - - - - - - - - - - - - - - - - - - \n")
        '''
        self.round_ended = True
        time.sleep(1)
        return

    def start_round(self):
        '''
        starts a new round
        input: game- object ; player- object
        returns
        '''
        roll = False

        x = threading.Thread(target = self.timer)
        x.start()

        while True:
            for i in self.game.get_players():
                self.game.add_owned_property(i.get_property(''))
            #time.sleep(1)
            self.game.street(self.player)

            if self.round_ended and roll == True:
                return

            if self.game.get_delay() == 0:
                self.game.set_msg("\n\n" + self.player.get_name() + "'s turn.")
                self.game.roll(self.player)
                if self.player not in self.game.get_players():
                    break # TODO  ENDING ROUND
                self.game.street(self.player)
                break
            else:
                self.game.choice_lock(['Roll', 'Houses', 'Trade', 'Mortgage'], ) # TODO TEMPORARY MESSAGES
                button_pressed = self.game.get_button_pressed()
                if self.round_ended:
                    if roll == True:
                        break
                    else:
                        self.game.roll(self.player)
                        return
                if button_pressed == 'Roll':
                    if roll == False:
                        roll = True
                        self.game.roll(self.player)
                        if self.player not in self.game.get_players():
                            break
                        self.game.street(self.player)
                    elif roll == True:
                        #print("You've already rolled this turn dummy- you cannot roll again")
                        self.game.set_msg("You've already rolled this turn dummy- you cannot roll again")
                elif button_pressed == 'Houses':
                    self.game.buy_houses()
                elif button_pressed == 'Trade':
                    self.game.trading(self.player, '')
                elif button_pressed == 'Mortgage':
                    self.game.mortgage(self.player)
                elif button_pressed == 'Info':
                    self.game.info()
                elif button_pressed == 'End Go':
                    if roll == False:
                        #print("You cannot end your go now- you have to roll.")
                        self.game.set_msg("You cannot end your go now- you have to roll")
                    else:
                        self.stop_thread = True
                        break
                else:
                    #print('Not one of the options. Try again')
                    self.game.set_msg('Not one of the options.')
                self.game.street(self.player)