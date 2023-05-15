#%%
# Alt click  -  multiple cursors 
# Ctrl L  -  select whole line
# Ctrl left right  -  moving through whole words
# Ctrl D  -  selecting multiple of same elements
# Ctrl+X  -  cut line
# Ctrl+C  -  copy line
# Alt up down  -  move line up/ down
# Shift Alt up down  -  copy line up/ down
# Ctrl Shift k  -  delete line
# Ctrl /  -  comment


# Continue with buying houses, CLIENT BUTTONS
# FINISH CONNECTING ALL CLIENT TO SERVER TO GAME LOGIC,
# when transferring money -> use red and green to highlight mnoney, create loading menu, purchase history
# CHANGE THE SERVER CODE SO IT LISTENS AFTER ALL DISCONNECTS, 
# continue with turbo -> FIX TIMINGS FOR TURBO, showing game history



'cd Monopoly 2.0/server' 
'python client.py'


import pygame, threading, time, os, random, copy
from network import Network
from game import Game

pygame.init()
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



class Board():
    WIDTH, HEIGHT = 1200, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MONOPOLY GAME")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    GREEN = (0, 255, 0)
    DARKGREEN = (50,205,50)
    MONOPOLYGREEN = (229, 255, 204)
    BLUE = (0, 0, 255)
    
    BROWN = (139, 69, 19)
    LIGHTBLUE = (106, 203, 237)
    PINK = (255, 0, 144)
    ORANGE = (251, 163, 26)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PROPGREEN = (80, 220, 100)
    ROYALBLUE = (18, 10, 143)
    CREAM = (255, 204, 153)

    FPS = 60 #CHANGE

    BOARD_WIDTH = 600
    PLAYER_ICON_WIDTH = 13
    PLAYER_CARD_WIDTH = 250
    PLAYER_CARD_HEIGHT = 350
    PROPERTY_BOX_WIDTH = 30
    PROPERTY_WIDTH = 18
    PROPERTY_CARD_WIDTH = 168
    PROPERTY_CARD_HEIGHT = 196
    BUTTON_WIDTH = 290
    BUTTON_HEIGHT = 40
    OUTLINE = 2

    PLAYER_PROP_FONT = pygame.font.SysFont('comicsans', 20)
    PLAYER_NAME_FONT = pygame.font.SysFont('comicsans', 30)
    TIME_FONT = pygame.font.SysFont('comicsans', 50)
    BIG_FONT = pygame.font.SysFont('comicsans', 70)


    BACKGROUND = pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Backgrounds\background3.jpg'), (WIDTH, HEIGHT)).convert_alpha()
    #BACKGROUND = pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Backgrounds\background3.jpg'), (WIDTH, HEIGHT)).convert_alpha()
    MONOPOLY_BOARD = pygame.transform.scale( pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Backgrounds\monopolyImage.jpg'), (BOARD_WIDTH, BOARD_WIDTH)).convert_alpha()
    PROPERTY_IMAGES = {1 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\OldKent.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       3 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Whitechapel.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       6 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Angel.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       8 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Euston.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       9 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Pentonville.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       11 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\PallMall.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       13 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Whitehall.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       14 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Northumberland.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       16 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Bow.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       18 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Marlborough.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       19 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Vine.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       21 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Strand.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       23 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Fleet.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       24 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Trafalgar.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       26 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Leicester.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       27 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Coventry.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       29 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Piccadilly.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       31 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Regent.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       32 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Oxford.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       34 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Bond.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       37 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\ParkLane.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       39 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Mayfair.png'), (PROPERTY_CARD_WIDTH, PROPERTY_CARD_HEIGHT)).convert_alpha(),
                       12 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Electric.png'), (177, 242)).convert_alpha(),
                       28 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Water.png'), (185, 214)).convert_alpha(),
                       5 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\King.png'), (180, 182)).convert_alpha(),
                       15 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Marlebone.png'), (180, 182)).convert_alpha(),
                       25 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Frenchurch.png'), (180, 182)).convert_alpha(),
                       35 : pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\Property\New Property\Liverpool.png'), (180, 182)).convert_alpha()}
    #CHANCE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\chance.jpg'), (80, 110)), 315) TODO FIX CHANCE AND COM -> MAYBE USE PHOTOSHOP TO ROT
    #COMMUNITY_CHEST = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(r'C:\Users\44772\Desktop\OneDrive - University of Bristol\Projects\Monopoly\Python_Monopoly\Monopoly 2.0\server\Assets\communityChest.jpg'), (80, 110)), 315)

    STREET_ICONS = {0: {'prop': [1, 3], 'colour': BROWN},
                    1: {'prop': [6, 8 , 9], 'colour': LIGHTBLUE}, 
                    2: {'prop': [11, 13, 14], 'colour': PINK}, 
                    3: {'prop': [16, 18, 19], 'colour': ORANGE},
                    4: {'prop': [21, 23, 24], 'colour': RED}, 
                    5: {'prop': [26, 27, 29], 'colour': YELLOW}, 
                    6: {'prop': [31, 32, 34], 'colour': PROPGREEN}, 
                    7: {'prop': [37, 39], 'colour': ROYALBLUE},
                    8: {'prop': [12, 28], 'colour': CREAM},
                    9: {'prop': [5, 15, 25, 35], 'colour': BLACK}}

    #ALL_STREETS = {street : STREET_ICONS[street]['prop'] for street in STREET_ICONS}

    
    def __init__(self):
        print('\nCLIENT STARTED')  # TODO FURTHER AUTHENTICATION & CONSTANT COMMUNICATION
        self.network = Network()
        self.game = self.network.get_game()
        self.round = None
        self.player = self.network.get_player() # TODO SORT OUT UPDATING PLAYER / BINDING IT TO PLAYERS LIST -> use get name?
        self.players = self.game.get_players()
        #self.connected_players = self.players   #TODO keep track of players that are still connected
        self.player_turn = None
        self.buttons = self.game.get_buttons() # list of communication buttons that need to be shown on the client
        self.msg = self.game.get_msg()
        self.morg_property = self.game.get_morg_property()
        self.displayed_msg = ''
        self.game_started = False
        self.your_turn = False
        self.player_buying_houses = None # player object who is buying houses
        self.client_buying_houses = False # tracks if your client is buying houses
        self.buying_houses_mode = False # tracks if someone is buying houses or not
        self.voted_turbo = False
        
        print(vars(self.player))
        print(vars(self.game))

        self.PROPERTY_BUTTONS = self.create_property_buttons(self)
        self.ALL_STREETS = {street : self.STREET_ICONS[street]['prop'] for street in self.STREET_ICONS}
        self.display_property = False
        self.all_displayed_property = self.Displayed_Property(self, self.ALL_STREETS, self.PROPERTY_BUTTONS)
        self.morg_displayed_property = self.Displayed_Property(self, {})
        self.current_displayed_property = None
        self.houses_ui = None # houses_ui object that handles buying houses

        self.icon_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.icon_event, 200)
        self.p1_button = self.Button(self, self.WHITE, 150, 255, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, 'P1')
        self.p2_button = self.Button(self, self.WHITE, 150, 615, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, 'P2')
        self.p3_button = self.Button(self, self.WHITE, 1050, 255, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, 'P3')
        self.p4_button = self.Button(self, self.WHITE, 1050, 615, self.PLAYER_CARD_WIDTH, self.PLAYER_CARD_HEIGHT, 'P4')
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.temp_player_buttons = [self.p1_button, self.p2_button, self.p3_button, self.p4_button]
        self.Board_Player_Objects = [self.player1, self.player2, self.player3, self.player4]

        for i in range(len(self.players)):
            self.Board_Player_Objects[i] = self.Board_Player(self, self.players[i])
            self.temp_player_buttons.pop(0)
        
        self.msg_button_options = ['Message', '32 houses', '12 hotels', '£0 free parking']
        self.hover_msg_button_options = ['Display number houses free', 'Display number hotels free', 'Display free parking money', 'Display game message']
        self.turbo_button_options = ['TURBO OFF', 'Vote for TURBO']
        self.time_button_options = ['Time : 0s left', 'End Go']

        self.prop_button = self.Button(self, self.RED, 460, 570, 120, 30, 'Property')
        self.prop_button.set_text_colour(self.WHITE)
        self.exit_button = self.Button(self, self.RED, 1150, 90, 60, 30, 'Exit')
        self.exit_button.set_text_colour(self.WHITE)
        self.msg_button = self.Button(self, self.WHITE, 600, 45, 600, 42, 'Message')
        self.turbo_button = self.Button(self, self.WHITE, 150, 45, 250, 42, 'TURBO OFF')
        self.time_button = self.Button(self, self.WHITE, 1050, 45, 250, 42, 'Time : 0s left')
        self.choose_prop_button = self.Button(self, self.WHITE, 450, 710, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, 'Choose properties')
        
        self.button1 = self.Button(self, self.WHITE, 450, 710, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, '')
        self.button2 = self.Button(self, self.WHITE, 750, 710, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, '')
        self.button3 = self.Button(self, self.WHITE, 450, 760, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, '')
        self.button4 = self.Button(self, self.WHITE, 750, 760, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, '')
        
        self.dice1 = self.Dice(self, 710, 410)
        self.dice2 = self.Dice(self, 630, 500)   
        self.dice_event = 4000
        pygame.time.set_timer(self.dice_event, 100)

        self.turbo_event = 4001
        pygame.time.set_timer(self.turbo_event, 3000)

        
        self.buttons_list = [self.prop_button, self.msg_button, self.turbo_button, self.time_button] # list of buttons that are always there
        self.display_prop_buttons = self.PROPERTY_BUTTONS.values()
        self.comms_buttons = [self.button1, self.button2, self.button3, self.button4]
        self.act_comms_buttons = []

        self.main()



    class Button():
        FONT = pygame.font.SysFont('comicsans', 30)

        def __init__(self, board, colour, x, y, width, height, text='', image = None):  #TODO ADD PICTURE OPTION, ACTIVATE BUTTONS ONLY FOR PLAYERS TURN
            '''
            x, y is point of centre #TODO MAYBE HAVE ATTRIBUTE OUTLINE THAT CAN BE TURNED ON AND OFF
            To make an outline permanent, set self.outline_colour to a colour. To make it temp, set it back to None. To lock an outline, toggle self.outline_lock
            '''
            self.board = board
            self.colour = colour
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.text_colour = self.board.BLACK
            self.image = image
            self.outline_colour = None
            self.outline_thickness = 0
            self.outline_lock = False
            self.outline_altcolour = None
            self.outline_altthickness = 0
            self.outline_lock_bypass = False
            self.click_counter = 0
            self.mouse_over = False
            self.active = True

        def set_colour(self, colour):
            if self.active:
                self.colour = colour
            else:
                self.colour = self.board.GREY

        def get_width(self):
            return self.width

        def get_height(self):
            return self.height

        def get_text(self):
            return self.text

        def set_text(self, text):
            self.text = text

        def set_text_colour(self, colour):
            self.text_colour = colour

        def get_click_counter(self):
            return self.click_counter

        def set_click_counter(self, num):
            self.click_counter = num

        def get_mouse_over(self):
            return self.mouse_over

        def set_mouse_over(self, bool):
            self.mouse_over = bool

        def set_active(self, bool):
            self.active = bool
            if bool == False:
                self.colour = self.board.GREY
                self.mouse_over = False

        def set_cords(self, x, y):
            self.x = x
            self.y = y

        def set_size(self, width, height):
            self.width = width
            self.height = height
            if self.image != None:
                pygame.transform.scale(self.image, (int(self.width), int(self.height)))

        def set_outline(self, thickness = 0, outline_colour = None, lock = False):
            '''
            if no parameters set, it will reset default outline attributes and turn off the outline
            '''
            self.outline_thickness = thickness
            self.outline_colour = outline_colour
            self.outline_lock = lock

        def set_outline_bypass(self, thickness = 0, outline_colour = None, lock_bypass = False):
            self.outline_altthickness = thickness
            self.outline_altcolour = outline_colour
            self.outline_lock_bypass = lock_bypass

        def draw(self, thickness = 0, outline = None, draw_bypass = False):
            '''
            hierarchy : draw_bypass > outline_lock_bypass > outline_lock > draw with no bypass
            input:
                thickness - int
                outline- colour
                draw_bypass - bool
            '''
            #Call this method to draw the button on the screen
            if draw_bypass:
                if outline == None and thickness != 0:
                    if self.outline_lock_bypass:
                        draw_centred_rect(self.width + (2*thickness), self.height + (2*thickness), self.x, self.y, self.outline_altcolour, self.board.WIN)
                    elif self.outline_lock:
                        draw_centred_rect(self.width + (2*thickness), self.height + (2*thickness), self.x, self.y, self.outline_colour, self.board.WIN)
                    else:
                        draw_centred_rect(self.width + (2*thickness), self.height + (2*thickness), self.x, self.y, self.board.BLACK, self.board.WIN)
                else:
                    draw_centred_rect(self.width + (2*thickness), self.height + (2*thickness), self.x, self.y, outline, self.board.WIN)
            elif self.outline_lock_bypass:
                draw_centred_rect(self.width + (2*self.outline_altthickness), self.height + (2*self.outline_altthickness), self.x, self.y, self.outline_altcolour, self.board.WIN)
            elif self.outline_lock:
                draw_centred_rect(self.width + (2*self.outline_thickness), self.height + (2*self.outline_thickness), self.x, self.y, self.outline_colour, self.board.WIN)
            elif outline != None:
                draw_centred_rect(self.width + (2*thickness), self.height + (2*thickness), self.x, self.y, outline, self.board.WIN)

            if self.image == None:
                draw_centred_rect(self.width, self.height, self.x, self.y, self.colour, self.board.WIN)            
                draw_centred_text(self.text, self.text_colour, self.FONT, self.x, self.y, self.board.WIN)
            else:
                self.board.WIN.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))

        def isOver(self, pos):
            #Pos is the mouse position or a tuple of (x,y) coordinates
            if self.active:
                if pos[0] > self.x - (self.width / 2) and pos[0] < self.x + (self.width / 2):
                    if pos[1] > self.y - (self.height / 2) and pos[1] < self.y + (self.height / 2):
                        self.mouse_over = True
                        return True
                
                self.mouse_over = False
                return False
            else:
                return False
                    


    class Dice():
        dice_width = 50
        delay = 700

        def __init__(self, board, x, y):
            self.board = board
            self.x = x
            self.y = y
            self.cords = {'x' : 0, 'y' : 0, 'x2' : 0, 'y2' : 0, 'x3' : 0, 'y3' : 0, 'x4' : 0, 'y4' : 0, 'x5' : 0, 'y5' : 0, 'x6' : 0, 'y6' : 0}
            self.rolling = None

        def get_rolling(self):
            return self.rolling

        def start(self):
            
            self.rolling = True

        def end(self):
            #pygame.time.set_timer(self.event, 0)
            self.rolling = False

        def randomise(self, num = None):
            if self.rolling:
                if num == None:
                    num = random.randrange(1, 7)
                if num == 1:
                    self.cords = {'x' : 0, 'y' : 0, 'x2' : 0, 'y2' : 0, 'x3' : 0, 'y3' : 0, 'x4' : 0, 'y4' : 0, 'x5' : 0, 'y5' : 0, 'x6' : 0, 'y6' : 0}
                elif num == 2:
                    self.cords = {'x' : -15, 'y' : -15, 'x2' : -15, 'y2' : -15, 'x3' : -15, 'y3' : -15, 'x4' : -15, 'y4' : -15, 'x5' : -15, 'y5' : -15, 'x6' : 15, 'y6' : 15}
                elif num == 3:
                    self.cords = {'x' : -15, 'y' : -15, 'x2' : -15, 'y2' : -15, 'x3' : -15, 'y3' : -15, 'x4' : -15, 'y4' : -15, 'x5' : 15, 'y5' : 15, 'x6' : 0, 'y6' : 0}
                elif num == 4:
                    self.cords = {'x' : -15, 'y' : -15, 'x2' : 15, 'y2' : 15, 'x3' : 15, 'y3' : -15, 'x4' : -15, 'y4' : 15, 'x5' : -15, 'y5' : -15, 'x6' : -15, 'y6' : -15}
                elif num == 5:
                    self.cords = {'x' : -15, 'y' : -15, 'x2' : 15, 'y2' : 15, 'x3' : 15, 'y3' : -15, 'x4' : -15, 'y4' : 15, 'x5' : 0, 'y5' : 0, 'x6' : 0, 'y6' : 0}
                elif num == 6:
                    self.cords = {'x' : -15, 'y' : -15, 'x2' : 15, 'y2' : 15, 'x3' : 15, 'y3' : -15, 'x4' : -15, 'y4' : 15, 'x5' : -15, 'y5' : 0, 'x6' : 15, 'y6' : 0}

        def draw(self, num = None, outline = None):
            if num != None:
                self.randomise(num)
            if outline != None:
                draw_centred_rect(self.dice_width + 2*self.board.OUTLINE, self.dice_width + 2*self.board.OUTLINE, self.x, self.y, outline, self.board.WIN)

            draw_centred_rect(self.dice_width, self.dice_width, self.x, self.y, self.board.RED, self.board.WIN)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x'], self.y + self.cords['y']], 5)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x2'], self.y + self.cords['y2']], 5)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x3'], self.y + self.cords['y3']], 5)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x4'], self.y + self.cords['y4']], 5)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x5'], self.y + self.cords['y5']], 5)
            pygame.draw.circle(self.board.WIN, self.board.WHITE, [self.x + self.cords['x6'], self.y + self.cords['y6']], 5)



    class Displayed_Property():
        def __init__(self, board, streets, property_buttons = None):
            '''
            input:
                streets - dict
            '''
            self.board = board
            self.displayed_streets = streets
            self.owned_properties = [property for street in self.displayed_streets.values() for property in street]
            if property_buttons == None:
                self.property_buttons = self.board.create_property_buttons(self.board)
            else:
                self.property_buttons = property_buttons
            self.selected_property = []

        def get_selected_property(self):
            return self.selected_property

        def hover(self, pos):
            '''
            check isOver for all properties buttons
            '''
            for property in self.owned_properties:
                self.property_buttons[property].isOver(pos)

        def set_outline(self, thickness = 0, colour = None, lock = False):
            '''
            to set outline for all buttons
            '''
            for property in self.owned_properties:
                self.property_buttons[property].set_outline(thickness, colour, lock)

        def set_outline_bypass(self, thickness = 0, colour = None, lock_bypass = False):
            '''
            to set outline bypass for all buttons
            '''
            for property in self.owned_properties:
                self.property_buttons[property].set_outline_bypass(thickness, colour, lock_bypass)

        def rotate(self, property):
            for street in self.displayed_streets:
                properties = self.displayed_streets[street]
                if property in properties:
                    self.displayed_streets[street].remove(property)
                    self.displayed_streets[street].insert(0, property)
                    self.property_buttons[property].draw(self.board.OUTLINE, self.board.BLACK)
                    break

        def sort_streets(self):
            if self.displayed_streets != self.board.ALL_STREETS:
                streets_copy = copy.deepcopy(self.displayed_streets)
                for street in streets_copy:
                    if streets_copy[street] == []:
                        self.displayed_streets.pop(street)
                        self.displayed_streets[street] = []

        def select_property(self, property): #TODO SEND SELECTED DATA SO THAT OTHER CLIENTS CAN SEE WHAT IS SELECTED
            if property in self.selected_property:
                self.selected_property.remove(property)
                self.property_buttons[property].set_outline()
            else:
                self.selected_property.append(property)
                self.property_buttons[property].set_outline(self.board.OUTLINE*1.5, self.board.GREEN, True)

        def stacked_select(self):
            '''
            for mouse down
            '''
            for street in self.displayed_streets:
                properties = self.displayed_streets[street]
                counter = len(properties) 
                for _ in range(counter):
                    property = properties[counter-1]
                    button = self.property_buttons[property]
                    if button.get_mouse_over():
                        if counter == 1:
                            self.select_property(property)
                            return
                        else:
                            counter2 = counter - 2
                            while counter2 >= 0:
                                if self.property_buttons[properties[counter2]].get_mouse_over():
                                    break
                                elif counter2 == 0:
                                    self.rotate(property)
                                    return
                                counter2 -= 1
                    counter -= 1

        def update(self, streets):# TODO UPDATE SELF.DISPLAYED_STREETS WITHOUT DISRUPTING ORDER 
            for street in streets:
                if street not in self.displayed_streets.keys():
                    self.displayed_streets[street] = streets[street]
                else:
                    properties = streets[street]
                    for property in properties:
                        if property not in self.displayed_streets[street]:
                            self.displayed_streets[street].append(property)

            if self.displayed_streets != streets:
                displayed_streets_copy = copy.deepcopy(self.displayed_streets)
                for street in displayed_streets_copy:
                    properties = displayed_streets_copy[street]
                    for property in properties:
                        if property not in list(streets.values()):
                            self.displayed_streets[street].remove(property)

            self.owned_properties = [property for street in self.displayed_streets.values() for property in street]
            self.sort_streets()

        def reset(self):
            '''
            resets all button outlines and order of buttons
            '''
            for property in self.selected_property:
                self.property_buttons[property].set_outline()
            self.selected_property = []
            self.displayed_streets = copy.deepcopy(self.board.ALL_STREETS)
            displayed_streets_copy = copy.deepcopy(self.displayed_streets)
            for street in displayed_streets_copy:
                for property in displayed_streets_copy[street]:
                    if property not in self.owned_properties:
                        self.displayed_streets[street].remove(property)

        def draw(self):
            for street in self.displayed_streets:
                street_index = list(self.displayed_streets.keys()).index(street)
                properties = self.displayed_streets[street]
                counter = len(properties) 
                for _ in range(counter):
                    property = properties[counter-1]
                    button = self.property_buttons[property]
                    x = 200 + 200 * (street_index % 5)
                    if street_index > 4:
                        y = 650
                    else:
                        y = 300
                    if property == 28:
                        y -= 70
                    else:
                        y -= (counter * 35)

                    button.set_cords(x, y)
                    if button.get_mouse_over():
                        if counter == 1:
                            if property in self.selected_property:
                                button.draw(self.board.OUTLINE*3, None, True)
                            else:
                                button.draw(self.board.OUTLINE*2, self.board.RED, True)
                        else:
                            counter2 = counter - 2
                            while counter2 >= 0:
                                if self.property_buttons[properties[counter2]].get_mouse_over():
                                    button.draw(self.board.OUTLINE, self.board.BLACK)
                                    break
                                elif counter2 == 0:
                                    if property in self.selected_property:
                                        button.draw(self.board.OUTLINE*3, None, True)
                                    else:
                                        button.draw(self.board.OUTLINE*2, self.board.RED, True)
                                counter2 -= 1
                    else:
                        button.draw(self.board.OUTLINE, self.board.BLACK)
                    counter -= 1



    class Houses_UI():
        STREET_CARD_WIDTH = 150
        STREET_CARD_HEIGHT = 200
        STREET_CONV = {'Brown' : [1, 3], 'Light Blue' : [6, 8 , 9], 'Pink' : [11, 13, 14], 'Orange' : [16, 18, 19], 'Red' : [21, 23, 24], 'Yellow' : [26, 27, 29], 'Green' : [31, 32, 34], 'Dark Blue' : [37, 39]} # to convert from street name to list of properties 

        def __init__(self, board, player):
            '''
            class to handle buying/ selling houses
            '''
            self.board = board
            self.player = player
            self.streets = self.player.get_streets()
            self.properties = self.player.get_property()
            self.new_properties = self.properties
            self.ALL_STREET_BUTTONS = {'Brown': self.board.Button(self.board, self.board.BROWN, 0, 0, self.     STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Brown'),
                                'Light Blue': self.board.Button(self.board, self.board.LIGHTBLUE, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Light Blue'),
                                'Pink': self.board.Button(self.board, self.board.PINK, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Pink'),
                                'Orange': self.board.Button(self.board, self.board.ORANGE, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Orange'),
                                'Red': self.board.Button(self.board, self.board.RED, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Red'),
                                'Yellow': self.board.Button(self.board, self.board.YELLOW, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Yellow'),
                                'Green': self.board.Button(self.board, self.board.PROPGREEN, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Green'),
                                'Dark Blue': self.board.Button(self.board, self.board.ROYALBLUE, 0, 0, self.STREET_CARD_WIDTH, self.STREET_CARD_HEIGHT, 'Dark Blue')}
            self.street_buttons = {i : self.ALL_STREET_BUTTONS[i] for i in self.ALL_STREET_BUTTONS if i in self.streets} # to choose which street to buy houses on
            self.selected_street = None
            self.property_buttons = {} # display the 2/3 properties & allow adding/ selling houses
            self.draw_streets = True # tracks whether to draw street buttons or houses buttons

        def get_selected_street(self):
            return self.selected_street

        def hover(self, pos):
            '''
            check isOver for all properties buttons
            '''
            if self.draw_streets:
                for street in self.street_buttons:
                    self.street_buttons[street].isOver(pos)
            else:
                pass
                # TODO CHECK HOVER FOR PROPERTY BUTTONS

        def update(self, player):
            self.player = player
            self.streets = self.player.get_streets()
            self.properties = self.player.get_property()
            self.street_buttons = {i : self.ALL_STREET_BUTTONS[i] for i in self.ALL_STREET_BUTTONS if i in self.streets}

        def reset(self): # resets the board's houses ui
            self = None # TODO check if this works

        def draw(self):
            if self.draw_streets:
                counter = 0
                for street in self.street_buttons:
                    button = self.street_buttons[street]
                    x = 195 + 270 * (counter % 4)
                    if counter < 4:
                        y = 230
                    else:
                        y = 530
                    button.set_cords(x, y)
                    button.draw(self.board.OUTLINE, self.board.BLACK)                        
                    counter += 1
            else:
                pass
                # TODO HANDLE PROPERTY BUTTONS



    class Board_Player(): # the manifestation of every player on the client (displays all player data)
        num_players = 0  # x centre for rect and text, y centre for rect, y centre for text
        player_cords = [[150, 255, 50], [150, 615, 450], [1050, 255, 50], [1050, 615, 450]]
        adjustments = {'name' : -150, 'money' : -118, 'property' : {'x': -150, 'y' : -88}}
        board_cords = {0: {0: (879.7, 659.7), 1: (806.7, 659.7), 2: (758.1, 659.7), 3: (709.4, 659.7), 4: (660.8, 659.7), 5: (612.1, 659.7), 6: (563.5, 659.7), 7: (514.9, 659.7), 8: (466.21, 659.7), 9: (417.6, 659.7), 
                           10: (344.6, 659.7), 11: (344.6, 586.7), 12: (344.6, 538.1), 13: (344.6, 489.4), 14: (344.6, 440.8), 15: (344.6, 392.1), 16: (344.6, 343.5), 17: (344.6, 294.8), 18: (344.6, 246.1), 19: (344.6, 197.5), 
                           20: (344.6, 124.59), 21: (417.6, 124.59), 22: (466.21, 124.59), 23: (514.9, 124.59), 24: (563.5, 124.59), 25: (612.1, 124.59), 26: (660.8, 124.59), 27: (709.4, 124.59), 28: (758.1, 124.59), 29: (806.7, 124.59),
                           30: (879.7, 124.59), 31: (879.7, 197.5), 32: (879.7, 246.1), 33: (879.7, 294.8), 34: (879.7, 343.5), 35: (879.7, 392.1), 36: (879.7, 440.8), 37: (879.7, 489.4), 38: (879.7, 538.1), 39: (879.7, 586.7)},

                       1: {0: (855.4, 659.7), 1: (782.4, 659.7), 2: (733.8, 659.7), 3: (685.1, 659.7), 4: (636.5, 659.7), 5: (587.8, 659.7), 6: (539.2, 659.7), 7: (490.6, 659.7), 8: (441.9, 659.7), 9: (393.3, 659.7), 
                           10: (320.3, 659.7), 11: (320.3, 586.7), 12: (320.3, 538.1), 13: (320.3, 489.4), 14: (320.3, 440.8), 15: (320.3, 392.1), 16: (320.3, 343.5), 17: (320.3, 294.8), 18: (320.3, 246.1), 19: (320.3, 197.5), 
                           20: (320.3, 124.59), 21: (393.3, 124.59), 22: (441.9, 124.59), 23: (490.6, 124.59), 24: (539.2, 124.59), 25: (587.8, 124.59), 26: (636.5, 124.59), 27: (685.1, 124.59), 28: (733.8, 124.59), 29: (782.4, 124.59),
                           30: (855.4, 124.59), 31: (855.4, 197.5), 32: (855.4, 246.1), 33: (855.4, 294.8), 34: (855.4, 343.5), 35: (855.4, 392.1), 36: (855.4, 440.8), 37: (855.4, 489.4), 38: (855.4, 538.1), 39: (855.4, 586.7)},

                       2: {0: (879.7, 635.4), 1: (806.7, 635.4), 2: (758.1, 635.4), 3: (709.4, 635.4), 4: (660.8, 635.4), 5: (612.1, 635.4), 6: (563.5, 635.4), 7: (514.9, 635.4), 8: (466.21, 635.4), 9: (417.6, 635.4), 
                           10: (344.6, 635.4), 11: (344.6, 562.4), 12: (344.6, 513.8), 13: (344.6, 465.1), 14: (344.6, 416.5), 15: (344.6, 367.8), 16: (344.6, 319.2), 17: (344.6, 270.5), 18: (344.6, 221.8), 19: (344.6, 173.2), 
                           20: (344.6, 100.3), 21: (417.6, 100.3), 22: (466.21, 100.3), 23: (514.9, 100.3), 24: (563.5, 100.3), 25: (612.1, 100.3), 26: (660.8, 100.3), 27: (709.4, 100.3), 28: (758.1, 100.3), 29: (806.7, 100.3),
                           30: (879.7, 100.3), 31: (879.7, 173.2), 32: (879.7, 221.8), 33: (879.7, 270.5), 34: (879.7, 319.2), 35: (879.7, 367.8), 36: (879.7, 416.5), 37: (879.7, 465.1), 38: (879.7, 513.8), 39: (879.7, 562.4)},

                       3: {0: (855.4, 635.4), 1: (782.4, 635.4), 2: (733.8, 635.4), 3: (685.1, 635.4), 4: (636.5, 635.4), 5: (587.8, 635.4), 6: (539.2, 635.4), 7: (490.6, 635.4), 8: (441.9, 635.4), 9: (393.3, 635.4), 
                           10: (320.3, 635.4), 11: (320.3, 562.4), 12: (320.3, 513.8), 13: (320.3, 465.1), 14: (320.3, 416.5), 15: (320.3, 367.8), 16: (320.3, 319.2), 17: (320.3, 270.5), 18: (320.3, 221.8), 19: (320.3, 173.2), 
                           20: (320.3, 100.3), 21: (393.3, 100.3), 22: (441.9, 100.3), 23: (490.6, 100.3), 24: (539.2, 100.3), 25: (587.8, 100.3), 26: (636.5, 100.3), 27: (685.1, 100.3), 28: (733.8, 100.3), 29: (782.4, 100.3),
                           30: (855.4, 100.3), 31: (855.4, 173.2), 32: (855.4, 221.8), 33: (855.4, 270.5), 34: (855.4, 319.2), 35: (855.4, 367.8), 36: (855.4, 416.5), 37: (855.4, 465.1), 38: (855.4, 513.8), 39: (855.4, 562.4)},

                       4: {0: (867.6, 647.6), 1: (794.6, 647.6), 2: (746, 647.6), 3: (709.4, 647.6), 4: (660.8, 648.5), 5: (600, 647.6), 6: (551.4, 647.6), 7: (502.8, 647.6), 8: (454.1, 647.6), 9: (405.5, 647.6), 
                           10: (332.5, 647.6), 11: (332.5, 574.6), 12: (332.5, 526), 13: (344.6, 474.3), 14: (332.5, 428.7), 15: (332.5, 380), 16: (332.5, 331.4), 17: (332.5, 282.7), 18: (332.5, 234), 19: (332.5, 185.4), 
                           20: (332.5, 112.5), 21: (405.5, 112.5), 22: (454.1, 112.5), 23: (502.8, 112.5), 24: (551.4, 112.5), 25: (600, 112.5), 26: (648.7, 112.5), 27: (697, 112.5), 28: (746, 112.5), 29: (794.6, 112.5),
                           30: (867.6, 112.5), 31: (867.6, 185.4), 32: (867.6, 234), 33: (867.6, 282.7), 34: (867.6, 331.4), 35: (867.6, 380), 36: (867.6, 428.7), 37: (867.6, 477.3), 38: (867.6, 526), 39: (867.6, 574.6)}
                       }


        def __init__(self, board, player):
            '''
            holds at the board attributes of players 
            input: player - obj
            '''
            self.board = board
            self.player = player
            self.card_cords = self.player_cords[self.num_players]
            self.options_pos_cords = self.board_cords[self.num_players]
            self.name = self.player.get_name()
            self.current_position = self.new_position = self.player.get_position()
            self.pos_cords = self.options_pos_cords[self.current_position]
            self.money = self.player.get_money() # TODO MONEY BUTTON THAT SHOWS PURCHASE HISTORY
            self.money_history = []
            self.property = self.player.get_property('')
            self.streets = self.player.get_streets()
            self.jail_turns = self.player.get_jail_turns()
            self.jail_card = self.player.get_jail_card()
            self.displayed_property = self.set_displayed_property()
            self.display_property = False # TODO SORT OUT DISPLAYING PROPERTY FOR INSTANCES OF PLAYERS

            self.card = self.board.Button(self.board, self.board.WHITE, self.card_cords[0], self.card_cords[1], self.board.PLAYER_CARD_WIDTH, self.board.PLAYER_CARD_HEIGHT)
            self.icon = self.board.Button(self.board, self.board.WHITE, self.pos_cords[0], self.pos_cords[1], self.board.PLAYER_ICON_WIDTH, self.board.PLAYER_ICON_WIDTH)
            self.name_button = self.board.Button(self.board, self.board.WHITE, self.card_cords[0], self.card_cords[1] + self.adjustments['name'], self.board.PLAYER_CARD_WIDTH-25, 25, self.name)
            self.player_buttons = [self.icon, self.card, self.name_button]
            self.moving = False
            self.board_player_turn = False
            self.board_player_buying_houses = False
            self.__class__.num_players += 1

        def get_name(self):
            return self.name

        def set_displayed_property(self):   # TODO UPDATE DISPLAYED PROPERTY - DISPLAYED PROEPRTY STREET ATTRIBUTE HAS TO BE IN DICT FORM
            streets = copy.deepcopy(self.board.ALL_STREETS)
            streets_copy = copy.deepcopy(streets)

            for street in streets_copy:
                properties = streets_copy[street]
                for property in properties:
                    if property not in self.property.keys():
                        streets[street].remove(property)
            return self.board.Displayed_Property(self.board, streets)

        def update_displayed_property(self):
            streets = copy.deepcopy(self.board.ALL_STREETS)
            streets_copy = copy.deepcopy(streets)

            for street in streets:
                properties = streets_copy[street]
                for property in properties:
                    if property not in self.property.keys():
                        streets[street].remove(property)
            self.displayed_property.update(streets)

        def colour_bind(self, buttons, colour):
            '''
            makes all buttons same colour
            input: button - list
            '''
            for button in buttons:
                button.set_colour(colour)

        def activate_icon(self, bool, colour):
            '''
            True makes icon red & enlarged
            '''
            if bool:
                self.icon.set_colour(colour)
                self.icon.set_size(self.board.PLAYER_ICON_WIDTH*1.5 , self.board.PLAYER_ICON_WIDTH*1.5)
            elif not bool:
                self.icon.set_colour(self.board.WHITE)
                self.icon.set_size(self.board.PLAYER_ICON_WIDTH , self.board.PLAYER_ICON_WIDTH)

        def click(self, event, pos): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.card.isOver(pos):
                    if not self.name_button.isOver(pos) and self.property != {}:
                        self.board.display_property = True
                        self.board.current_displayed_property = self.displayed_property

            if event.type == pygame.MOUSEMOTION:
                for button in self.player_buttons:
                    button.isOver(pos)
                
        def set_position(self):
            if self.current_position != self.new_position:
                self.moving = True
                self.current_position = (self.current_position + 1) % 40
            else:
                self.moving = False

        def update(self, player):
            self.player = player
            self.new_position = self.player.get_position()
            self.money = self.player.get_money()
            self.money_history = []
            self.property = self.player.get_property('')
            self.streets = self.player.get_streets()
            self.jail_turns = self.player.get_jail_turns()
            self.jail_card = self.player.get_jail_card()

            if self.current_position != self.new_position:
                self.pos_cords = self.board_cords[4][self.current_position]
            else:
                self.pos_cords = self.options_pos_cords[self.current_position]
            self.icon.set_cords(self.pos_cords[0], self.pos_cords[1])

            if self.name == self.board.players[0].get_name():
                self.board_player_turn = True
            else:
                self.board_player_turn = False
                
            try: # check if this board player is buying houses
                if self.name == self.board.game.get_player_buying_houses().get_name():
                    self.board_player_buying_houses = True
                else:
                    self.board_player_buying_houses = False
            except Exception:
                self.board_player_buying_houses = False

            self.update_displayed_property()

        def draw(self):
            if self.board_player_buying_houses: # make player board card red if buying houses
                if self.moving or self.icon.get_mouse_over() or self.card.get_mouse_over():
                    self.activate_icon(True, self.board.RED)
                    self.card.draw(self.board.OUTLINE*2.5, self.board.RED)
                else:
                    self.activate_icon(False, self.board.WHITE)
                    self.card.draw(self.board.OUTLINE*1.5, self.board.RED)
                self.icon.draw(2, self.board.RED)
            elif self.board_player_turn:
                if self.moving or self.icon.get_mouse_over() or self.card.get_mouse_over():
                    self.activate_icon(True, self.board.GREEN)
                    self.card.draw(self.board.OUTLINE*2.5, self.board.GREEN)
                else:
                    self.activate_icon(False, self.board.WHITE)
                    self.card.draw(self.board.OUTLINE*1.5, self.board.GREEN)
                self.icon.draw(2, self.board.GREEN)
            elif self.icon.get_mouse_over() or self.card.get_mouse_over():
                self.activate_icon(True, self.board.RED)
                self.icon.draw(2, self.board.RED)
                self.card.draw(self.board.OUTLINE*1.5, self.board.RED)
            else:
                self.activate_icon(False, self.board.WHITE)
                self.icon.draw(2, self.board.RED)
                self.card.draw(self.board.OUTLINE, self.board.BLACK)
            

            if self.name_button.get_mouse_over():
                if self.board_player_buying_houses:
                    self.name_button.draw(self.board.OUTLINE*1.5, self.board.RED)
                elif self.board_player_turn:
                    self.name_button.draw(self.board.OUTLINE*1.5, self.board.GREEN)
                else:
                    self.name_button.draw(self.board.OUTLINE*1.5, self.board.RED)
            else:
                self.name_button.draw(0, self.board.BLACK)

            x = self.card_cords[0] + self.adjustments['property']['x']
            y = self.card_cords[1] + self.adjustments['property']['y']

            for i in range(10):
                ycounter = 1
                for property in self.board.STREET_ICONS[i]['prop']:
                    draw_centred_rect(self.board.PROPERTY_WIDTH + 4, self.board.PROPERTY_WIDTH + 4, x + (ycounter*60), y + (i*26), self.board.BLACK, self.board.WIN)
                    if property in list(self.property): #TODO HIGHLIGHT STREETS
                        draw_centred_rect(self.board.PROPERTY_WIDTH, self.board.PROPERTY_WIDTH, x + (ycounter*60), y + (i*26), self.board.STREET_ICONS[i]['colour'], self.board.WIN)
                        if isinstance(self.property[property], float):
                            draw_centred_text('M', self.board.BLACK, self.board.PLAYER_PROP_FONT, x + (ycounter*60), y + (i*26), self.board.WIN)
                        else:
                            draw_centred_text(str(self.property[property]), self.board.BLACK, self.board.PLAYER_PROP_FONT, x + (ycounter*60), y + (i*26), self.board.WIN)
                    else:
                        draw_centred_rect(self.board.PROPERTY_WIDTH, self.board.PROPERTY_WIDTH, x + (ycounter*60), y + (i*26), self.board.GREY, self.board.WIN)
                    ycounter += 1

            draw_centred_text("£" + str(self.money), self.board.BLACK, self.board.PLAYER_NAME_FONT, self.card_cords[0], self.card_cords[1] + self.adjustments['money'], self.board.WIN)



    def create_property_buttons(self, board):
        '''
        creates an instance of property_buttons
        '''
        property_buttons = {prop : board.Button(board, None, 0, 0, board.PROPERTY_CARD_WIDTH, board.PROPERTY_CARD_HEIGHT, '', board.PROPERTY_IMAGES[prop]) for prop in board.PROPERTY_IMAGES}
        for prop in property_buttons:
            button = property_buttons[prop]
            if prop == 12:
                button.set_size(177, 242)
            elif prop == 28:
                button.set_size(185, 214)
            elif prop == 5 or prop == 15 or prop == 25 or prop == 35:
                button.set_size(180, 182)
        return property_buttons



    def update(self, game):
        self.game = game
        self.players = game.get_players()
        self.buttons = game.get_buttons()
        self.msg = game.get_msg()
        self.morg_property = self.game.get_morg_property()
        self.roll_num = self.game.get_roll_num()
        
        if not self.game_started:
            for i in range(len(self.players)):
                if self.Board_Player_Objects[i] == None:
                    self.Board_Player_Objects[i] = self.Board_Player(self, self.players[i])
                    self.temp_player_buttons.pop(0)
                else:
                    self.Board_Player_Objects[i].update(self.players[i])

        if self.game_started:
            self.player_turn = self.players[0]
            self.round = self.game.get_round()
            self.player_buying_houses = self.game.get_player_buying_houses()

            if self.game.get_player_buying_houses() == None: # check if someone is buying houses
                self.buying_houses_mode = False
            else:
                self.buying_houses_mode = True

            for player in self.players:
                for board_player in self.Board_Player_Objects:
                    if player.get_name() == board_player.get_name():
                        board_player.update(player)

            try: # check if this client is buying houses
                if self.player.get_name() == self.game.get_player_buying_houses().get_name():
                    self.client_buying_houses = True
                else:
                    self.client_buying_houses = False
            except Exception:
                self.client_buying_houses = False

            try: # update houses_ui with player info
                self.houses_ui.update(self.player_buying_houses)
            except Exception:
                pass

            if self.game.get_delay() == 0 or self.game.get_delay() == 0.15:
                self.turbo_button_options = ["TURBO ON", "Turn off"]
                self.voted_turbo = False
            else:
                self.turbo_button_options[1] = "Vote for TURBO"
                if self.turbo_button_options[0] == "TURBO ON":
                    self.turbo_button_options[0] = "TURBO OFF"
                if self.voted_turbo:
                    self.turbo_button_options = ["Voted for TURBO", "Cancel vote"]
            
            if self.msg != '':
                self.displayed_msg = self.msg
            self.msg_button_options = [self.displayed_msg, str(self.game.get_houses()) + ' houses', str(self.game.get_hotels()) + ' hotels', '£' + str(self.game.get_freePMon()) + ' free parking']

            self.time_button_options = ['Time : ' + str(self.round.get_time_left()) + 's left', 'End Go']

            if self.game.get_rolling() and self.game.get_roll1() == None and self.game.get_roll2() == None:
                self.dice1.start()
                self.dice2.start()
            if self.game.get_roll1() != None:
                self.dice1.draw(self.game.get_roll1(), True)
                self.dice1.end()
            if self.game.get_roll2() != None:
                self.dice2.draw(self.game.get_roll2(), True)
                self.dice2.end()
            
            streets = copy.deepcopy(self.ALL_STREETS)
            streets_copy = copy.deepcopy(streets)
            for street in streets_copy:
                properties = streets_copy[street]
                for property in properties:
                    if property not in self.morg_property:
                        streets[street].remove(property)
            self.morg_displayed_property.update(streets)

        #self.connected_players = []

        self.act_comms_buttons = []

        if self.buttons[0] == 'Choose properties':
            self.comms_buttons[1].set_text(self.buttons[1])
            self.comms_buttons[2].set_text('Cancel')
            for n in [1,2]:
                self.act_comms_buttons.append(self.comms_buttons[n])
            if self.choose_prop_button not in self.buttons_list:
                self.buttons_list.append(self.choose_prop_button)

        else:
            if self.buttons == ['Choose street', 'Exit']: # setup houses_ui
                if self.houses_ui == None: # TODO wipe houses_ui data
                    self.houses_ui = self.Houses_UI(self, self.player_buying_houses)
            for button in self.buttons:
                self.comms_buttons[self.buttons.index(button)].set_text(button)
                self.act_comms_buttons.append(self.comms_buttons[self.buttons.index(button)])
            if self.choose_prop_button in self.buttons_list:
                self.buttons_list.remove(self.choose_prop_button)



    def draw_window(self):
        self.WIN.blit(self.BACKGROUND, (0,0))
        draw_centred_rect(self.BOARD_WIDTH + 2*self.OUTLINE, self.BOARD_WIDTH + 2*self.OUTLINE, 600, 380, self.BLACK, self.WIN)
        self.WIN.blit(self.MONOPOLY_BOARD, (300, 80))
        self.dice1.draw(None, True)
        self.dice2.draw(None, True)

        for player in self.Board_Player_Objects:
            player.draw()

        for player in self.temp_player_buttons:
            player.draw(self.OUTLINE, self.BLACK)

        for button in self.buttons_list + self.act_comms_buttons:
            if button == self.msg_button:
                if button.get_mouse_over():
                    button.set_text(self.hover_msg_button_options[button.get_click_counter()])
                else:
                    button.set_text(self.msg_button_options[button.get_click_counter()])
            elif button == self.turbo_button:
                if button.get_mouse_over():
                    button.set_text(self.turbo_button_options[1])
                else:
                    button.set_text(self.turbo_button_options[0])
            elif button == self.time_button:
                if button.get_mouse_over():
                    button.set_text(self.time_button_options[1])
                else:
                    button.set_text(self.time_button_options[0])
            button.draw(self.OUTLINE, self.BLACK)

        if self.display_property:
            self.exit_button.draw(self.OUTLINE, self.BLACK)
            self.current_displayed_property.draw()

        if self.buying_houses_mode:
            try:
                self.houses_ui.draw()
            except Exception:
                pass

        pygame.display.update()



    def main(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(self.FPS)
            started = self.network.send('start')
            self.update(self.network.send('get'))

            if started:
                print("Game started")
                self.game_started = True
                while self.Board_Player_Objects[-1] == None:
                    self.Board_Player_Objects.remove(self.Board_Player_Objects[-1])

                while run:
                    clock.tick(self.FPS)
                    self.update(self.network.send('get'))
                    self.your_turn = self.network.send('players_turn') # to check if it is this clients turn
                    self.time_button.set_active(self.your_turn)
                    for button in self.act_comms_buttons: # changes the client depending on who's turn it is
                        if button.get_text() == 'Houses':
                            button.set_active(True)
                        else:
                            if self.game.get_player_buying_houses() != None:
                                if self.client_buying_houses:
                                    button.set_active(True)
                                else:
                                    button.set_active(False)
                            else:
                                button.set_active(self.your_turn)

                    self.draw_window()

                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()

                        if event.type == pygame.QUIT:
                            run = False
                            pygame.quit()


                        if self.display_property: # to check if mouse over displayed property buttons
                            self.current_displayed_property.hover(pos)
                        elif self.buying_houses_mode: # to check if mouse over buying houses buttons
                            try:
                               self.houses_ui.hover(pos)
                            except Exception:
                                pass 
                        else:
                            for player in self.Board_Player_Objects: # to check if mouse over player board cards
                                player.click(event, pos)


                        if event.type == pygame.MOUSEBUTTONDOWN: 
                            if self.display_property: # handles choosing property stuff
                                if self.exit_button.isOver(pos):
                                    self.display_property = False
                                    self.exit_button.set_outline()
                                    self.current_displayed_property.set_outline_bypass()
                                self.current_displayed_property.stacked_select() # to check (if mouse on display prop buttons) whether to select or rotate cards
                            else:
                                if self.buying_houses_mode: # handles buying houses stuff
                                    pass #TODO CONTINUE WITH CLICKING OF BUTTONS
                                for button in self.buttons_list + self.act_comms_buttons:
                                    if button.isOver(pos):
                                        # if self.buttons == ['Choose street', 'Exit']:
                                        #     if button.get_text() == 'Exit':
                                        #         pass
                                        if button in self.act_comms_buttons:
                                            if button.get_text() == 'Confirm mortgage' or button.get_text() == 'Confirm unmortgage':
                                                if self.morg_displayed_property.get_selected_property() == []:
                                                    self.network.send('no prop')
                                                else:
                                                    self.network.send(self.morg_displayed_property.get_selected_property())
                                                self.morg_displayed_property.reset()
                                            else:
                                                #print(button.get_text())
                                                self.network.send(button.get_text())

                                        elif button == self.prop_button:
                                            self.display_property = True
                                            self.current_displayed_property = self.all_displayed_property

                                        elif button == self.choose_prop_button:
                                            self.display_property = True
                                            self.current_displayed_property = self.morg_displayed_property

                                        elif button == self.msg_button:
                                            button.set_click_counter((button.click_counter + 1) % 4)
                                            button.set_text(self.msg_button_options[button.get_click_counter()])

                                        elif button == self.time_button: 
                                            if self.buttons == ['Roll', 'Houses', 'Trade', 'Mortgage']:
                                                print(button.get_text())
                                                self.network.send('End Go')

                                        elif button == self.turbo_button:
                                            print(button.get_text())
                                            if self.game.get_delay() == 0.25:
                                                self.voted_turbo = not self.voted_turbo
                                                if self.voted_turbo:
                                                    self.network.send('TURBO +1')
                                                else:
                                                    self.network.send('TURBO -1')
                                            else:
                                                self.network.send('TURBO -1')


                        if event.type == pygame.MOUSEMOTION:
                            if self.display_property:
                                if self.exit_button.isOver(pos):
                                    self.exit_button.set_outline(self.OUTLINE*3, self.RED, True)
                                    self.current_displayed_property.set_outline_bypass(self.OUTLINE*2, self.RED, True)
                                else:
                                    self.exit_button.set_outline()
                                    self.current_displayed_property.set_outline_bypass()
                            else:
                                for button in self.buttons_list + self.act_comms_buttons:
                                    if button.isOver(pos):
                                        button.set_colour(self.GREEN)
                                    else:
                                        if button == self.prop_button:
                                            button.set_colour(self.RED)
                                        else:
                                            button.set_colour(self.WHITE)


                        if event.type == self.dice_event:
                            self.dice1.randomise()
                            self.dice2.randomise()


                        if event.type == self.turbo_event:
                            if self.game.get_delay() != 0 and self.game.get_delay() != 0.15:
                                if not self.voted_turbo:
                                    if self.turbo_button_options[0] == 'TURBO OFF':
                                        self.turbo_button_options[0] = str(self.game.get_num_voted_turbo()) + ' voted for TURBO'
                                    else:
                                        self.turbo_button_options[0] = 'TURBO OFF'
                                else:
                                    if self.turbo_button_options[0] == 'Voted for TURBO':
                                        self.turbo_button_options[0] = str(self.game.get_num_voted_turbo()) + ' voted for TURBO'
                                    else:
                                        self.turbo_button_options[0] = 'Voted for TURBO'
                        
                        if event.type == self.icon_event:
                            for player in self.Board_Player_Objects:
                                player.set_position()
                            



            elif not started:
                print("Game not started")
            else:
                print("error with checking game starting")





if __name__ == '__main__':
    board = Board()


# %% 
