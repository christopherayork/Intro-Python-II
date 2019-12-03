# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def move(self, d):
        if not isinstance(d, str):
            return False
        elif d == 'n' or d == 'north':
            if self.room.n_to:
                self.room = self.room.n_to
                return True
        elif d == 'e' or d == 'east':
            if self.room.e_to:
                self.room = self.room.e_to
                return True
        elif d == 's' or d == 'south':
            if self.room.s_to:
                self.room = self.room.s_to
                return True
        elif d == 'w' or d == 'west':
            if self.room.w_to:
                self.room = self.room.w_to
                return True
        return False

    def grab(self, query):
        found = False
        for item in self.room.items:
            if query == item:
                found = True
                self.items.append(item)
                print(f'You pick up {item}')
                self.room.remove_item(item)
                break
        if not found:
            print('Invalid item')

    def drop(self, query):
        found = False
        for item in self.items:
            if query == item:
                found = True
                self.items.remove(item)
                print(f'You drop {item}')
                self.room.add_item(item)
                break
        if not found:
            print('Invalid item')
