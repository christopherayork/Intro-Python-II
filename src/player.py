# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room

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
