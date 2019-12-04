

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f'{self.name}'

    def on_take(self):
        print(f'You pick up {self.name}')
        return True

    def on_drop(self):
        print(f'You drop {self.name}')
        return True



