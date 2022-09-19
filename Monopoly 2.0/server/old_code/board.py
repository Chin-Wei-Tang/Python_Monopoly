import pygame
import os
from player import Player
from game import Game
pygame.font.init()
pygame.mixer.init()



def draw_centred_rect(rect_width, rect_height, x, y, colour, win):
    rect = pygame.Rect(0, 0, rect_width, rect_height)
    rect.center = x , y
    pygame.draw.rect(win, colour, rect)
    
def draw_centred_text(text, colour, font, x, y, win):
    '''
    draws the text centred at x, y
    input:
        text- str
        colour- constant e.g WHITE
        font- constant e.g PLAYER_NAME_FONT
        x- int
        y- int
    returns: None
    '''
    textSurf = font.render(text, 1, colour)
    textRect = textSurf.get_rect()
    textRect.center = x , y
    win.blit(textSurf, textRect)



class Button():
    OUTLINE = 3
    BLACK = (0, 0, 0)
    FONT = pygame.font.SysFont('comicsans', 30)

    def __init__(self, colour, x,y,width,height, text=''):  #TODO ACTIVATE BUTTONS ONLY FOR PLAYERS TURN
        '''
        x, y is point of centre
        '''
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def set_colour(self, colour):
        self.colour = colour

    def draw(self,win,outline=None):
        '''
        input:
            outline- colour
        '''
        #Call this method to draw the button on the screen
        if outline != None:
            draw_centred_rect(self.width + 2*self.OUTLINE, self.height + 2*self.OUTLINE, self.x, self.y, outline, win)
            #pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        draw_centred_rect(self.width, self.height, self.x, self.y, self.colour, win)
        
        if self.text != '':
            draw_centred_text(self.text, self.BLACK, self.FONT, self.x, self.y, win)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - (self.width / 2) and pos[0] < self.x + (self.width / 2):
            if pos[1] > self.y - (self.height / 2) and pos[1] < self.y + (self.height / 2):
                return True
            
        return False




class Board():
    WIDTH, HEIGHT = 1200, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MONOPOLY GAME")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    

    FPS = 60

    BOARD_WIDTH = 600
    PLAYER_CARD_WIDTH = 250
    PLAYER_CARD_HEIGHT = 350
    PROPERTY_BOX_WIDTH = 30
    BUTTON_WIDTH = 290
    BUTTON_HEIGHT = 40
    OUTLINE = 3
    PLAYER_NAME_FONT = pygame.font.SysFont('comicsans', 30)
    TIME_FONT = pygame.font.SysFont('comicsans', 50)

    BACKGROUND = pygame.transform.scale(pygame.image.load(r'G:\My Drive\05 Python\Python\Projects\Monopoly\Monopoly 2.0\server\Assets\background3.jpg'), (WIDTH, HEIGHT))
    MONOPOLY_BOARD = pygame.transform.scale( pygame.image.load(r'G:\My Drive\05 Python\Python\Projects\Monopoly\Monopoly 2.0\server\Assets\monopolyImage.jpg'), (BOARD_WIDTH, BOARD_WIDTH))
    #CHANCE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(r'G:\My Drive\05 Python\Python\Projects\Monopoly\Monopoly 2.0\server\Assets\chance.jpg'), (80, 110)), 315) TODO FIX CHANCE AND COM -> MAYBE USE PHOTOSHOP TO ROT
    #COMMUNITY_CHEST = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(r'G:\My Drive\05 Python\Python\Projects\Monopoly\Monopoly 2.0\server\Assets\communityChest.jpg'), (80, 110)), 315)
    CAR = pygame.transform.scale(pygame.image.load(r'G:\My Drive\05 Python\Python\Projects\Monopoly\Monopoly 2.0\server\Assets\car.png'), (60, 60))


    
    def __init__(self, players):  # TODO HOW TO USE GAME AND PLAYER METHODS WHEN BOARD FILE IS SEPARATED FROM GAME AND PLAYER FIELS
        '''
        input:
            player - player who is running this client
        '''
        #self.game = game
        self.players = players
        self.connected_players = [p1, p2, p3]   #keep track of players that are still connected
        self.player_turn = self.players[0]
        #self.player = player
        self.p1_button = Button(self.WHITE, 150, 200, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, )
        self.p2_button = Button(self.WHITE, 150, 600, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, )
        self.p3_button = Button(self.WHITE, 1050, 200, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, )
        self.p4_button = Button(self.WHITE, 1050, 600, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, )
        self.roll_button = Button(self.WHITE, 450, 710, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 'ROLL')
        self.houses_button = Button(self.WHITE, 750, 710, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 'HOUSES')
        self.trade_button = Button(self.WHITE, 450, 760, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 'TRADE')
        self.mortgage_button = Button(self.WHITE, 750, 760, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 'MORTGAGE')

        self.main()

    def update(self, game):
        self.game = game
        self.players = game.get_players()
        self.connected_players = [p1, p2, p3]
        #self.player = player

    def draw_window(self):
        #self.WIN.fill(self.GREY)
        self.WIN.blit(self.BACKGROUND, (0,0))
        draw_centred_rect(self.BOARD_WIDTH + 2*self.OUTLINE, self.BOARD_WIDTH + 2*self.OUTLINE, 600, 380, self.BLACK, self.WIN)
        self.WIN.blit(self.MONOPOLY_BOARD, (300, 80))
        self.WIN.blit(self.CAR, (800, 600))     #TODO PUT OUTLINE AROUND OBJECT

        for player in self.players:
            self.draw_player(player)

        draw_centred_rect(self.BOARD_WIDTH + 2*self.OUTLINE, 42 + 2*self.OUTLINE, 600, 45, self.BLACK, self.WIN)
        draw_centred_rect(self.BOARD_WIDTH , 42, 600, 45, self.WHITE, self.WIN)
        draw_centred_text('Time', self.BLACK, self.TIME_FONT, 600, 45, self.WIN)

        self.roll_button.draw(self.WIN, True)
        self.houses_button.draw(self.WIN, True)
        self.trade_button.draw(self.WIN, True)
        self.mortgage_button.draw(self.WIN, True)

        pygame.display.update()

    def draw_player(self, player):
        '''
        input: player - object
        '''
        index = self.players.index(player)
        cords = []
        outline_colour = self.RED
        card_colour = self.WHITE
        msg = player.get_name()
        money = player.get_money()

        if index == 0:
            cords = [150, 200, 50] # x centre for rect and text, y centre for rect, y centre for text
        elif index == 1:
            cords = [150, 600, 450]
        elif index == 2:
            cords = [1050, 200, 50]
        elif index == 3:
            cords = [1050, 600, 450]
        else:
            print("Error- more players then expected")

        if player == self.player_turn:
            outline_colour = self.GREEN
            
        if player not in self.connected_players:
            card_colour = self.GREY
            outline_colour = self.GREY
            msg = 'DISCONNECTED'
            money = ''

        draw_centred_rect(self.PLAYER_CARD_WIDTH + 2*self.OUTLINE, self.PLAYER_CARD_HEIGHT + 2*self.OUTLINE, cords[0], cords[1], outline_colour, self.WIN)
        draw_centred_rect(self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, cords[0], cords[1], card_colour, self.WIN)
        draw_centred_text(msg, self.BLACK, self.PLAYER_NAME_FONT, cords[0], cords[2], self.WIN)
        draw_centred_text('£' + str(money), self.BLACK, self.PLAYER_NAME_FONT, cords[0], cords[2] + 20, self.WIN)


    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            self.draw_window()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.roll_button.isOver(pos):
                        print("Clicked roll")
                    if self.houses_button.isOver(pos):
                        print("Clicked houses")
                    if self.trade_button.isOver(pos):
                        print("Clicked trade")
                    if self.mortgage_button.isOver(pos):
                        print("Clicked mortgage")

                if event.type == pygame.MOUSEMOTION:
                    if self.roll_button.isOver(pos):
                        self.roll_button.set_colour(self.GREEN)
                    else:
                        self.roll_button.set_colour(self.WHITE)

                    if self.houses_button.isOver(pos):
                        self.houses_button.set_colour(self.GREEN)
                    else:
                        self.houses_button.set_colour(self.WHITE)

                    if self.trade_button.isOver(pos):
                        self.trade_button.set_colour(self.GREEN)
                    else:
                        self.trade_button.set_colour(self.WHITE)

                    if self.mortgage_button.isOver(pos):
                        self.mortgage_button.set_colour(self.GREEN)
                    else:
                        self.mortgage_button.set_colour(self.WHITE)

            


if __name__ == '__main__':
    p1 = Player('p1', 0, 1500)
    p2 = Player('p2', 0, 1500)
    p3 = Player('p3', 0, 1500)
    p4 = Player('p4', 0, 1500)

    players = [p1, p2, p3, p4]
    new_board = Board(players)