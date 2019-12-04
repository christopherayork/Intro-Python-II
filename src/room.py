# Implement a class to hold room information. This should have name and
# description attributes.
from mob import Mob


class Room(Mob):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.mobs = []
        self.items = []
        self.n_to = False
        self.e_to = False
        self.s_to = False
        self.w_to = False

    def __str__(self):
        items = ''
        for item in self.items:
            items += f'{item}\n'
        return f'''
# You have entered {self.name}
# {self.desc}
# It contains
{items}
        '''

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def enter(self, mob):
        if not isinstance(mob, Mob):
            return False
        self.entered(mob)

    def entered(self, mob):
        allowed = mob.move_to(self)
        if not allowed:
            return False
        self.mobs.append(mob)
        return True

    def exit(self, mob):
        self.exited(mob)
        return True

    def exited(self, mob):
        return True
