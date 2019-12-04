# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def inventory(self):
        print('### Your inventory ###')
        for i in self.items:
            print(i)

    def move(self, d):
        if not isinstance(d, str):
            return False
        elif d == 'n' or d == 'north':
            if isinstance(self.room.n_to, Room):
                self.room = self.room.n_to
                return True
            else:
                print('You can\'t move that way.')
        elif d == 'e' or d == 'east':
            if isinstance(self.room.e_to, Room):
                self.room = self.room.e_to
                return True
            else:
                print('You can\'t move that way.')
        elif d == 's' or d == 'south':
            if isinstance(self.room.s_to, Room):
                self.room = self.room.s_to
                return True
            else:
                print('You can\'t move that way.')
        elif d == 'w' or d == 'west':
            if isinstance(self.room.w_to, Room):
                self.room = self.room.w_to
                return True
            else:
                print('You can\'t move that way.')
        return False

    def grab(self, query):
        found = False
        for item in self.room.items:
            if query == item.name:
                found = True
                grabbed = item.on_take()
                if not grabbed:
                    return False
                self.items.append(item)
                self.room.remove_item(item)
                break
        if not found:
            print('Invalid item')

    def drop(self, query):
        found = False
        for item in self.items:
            if query == item.name:
                found = True
                dropped = item.on_drop()
                if not dropped:
                    return False
                self.items.remove(item)
                self.room.add_item(item)
                break
        if not found:
            print('Invalid item')
