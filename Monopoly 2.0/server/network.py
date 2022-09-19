import socket, pickle

class Network:
    def __init__(self):
        print("\nNETWORK CREATED\n")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server =  '127.0.0.1'   #'10.34.196.211'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()
        self.game = self.send('get')#   TODO GET GAME & BOARD

    def get_player(self):
        return self.player

    def get_game(self):
        return self.game
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            # if data != 'get':
            #     print("sent - " + str(data))
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(10000)) #was 2048
        except socket.error as e:
            print(e)