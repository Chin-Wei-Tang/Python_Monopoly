import time, random, string

class Player:
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money
        self.property = {}
        self.streets = []
        self.jail_turns = 0
        self.jail_card = 0

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
    
    def set_position(self, position):
        self.position = position
        return

    def get_money(self):
        return self.money

    def change_money(self, change):
        self.money += change
        return self.money

    def get_property(self, property = ''):
        '''
        returns property of the player or number of houses for a property
        input: property - int
        returns: dict or int
        '''
        if property == '':
            return self.property
        else:
            return self.property[property]

    def set_property(self, property, houses, dict):
        '''
        adds new property to player's property list, changes number of houses or replaces property dictionary with new one
        input: property- int ; houses- int ; dict- dict
        output: None
        '''
        if dict == '':
            self.property[property] = houses
        else:
            self.property = dict
        return

    def remove_property(self, property):
        self.property.pop(property)
        return

    def get_streets(self):
        return self.streets

    def set_streets(self, street, list):
        '''
        adds new completed street or replaces streets list with a new one
        input: street- str ; list- list
        '''
        if street != '':
            self.streets.append(street)
        if list != '':
            self.streets = list
        return

    def remove_streets(self, street):
        self.streets.pop(street)
        return

    def get_jail_turns(self):
        return self.jail_turns

    def set_jail_turns(self, number):
        self.jail_turns = number
        return

    def get_jail_card(self):
        return self.jail_card

    def set_jail_card(self, number):
        '''
        adds/ removes that number of jail cards
        input: number- int
        returns: None
        '''
        self.jail_card += number
        return
