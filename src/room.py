# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

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
