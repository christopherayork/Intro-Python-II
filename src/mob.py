# from room import Room


class Mob:
    def __init__(self, name, desc, room):
        self.name = name
        self.room = room
        self.desc = desc
        self.items = []
        self.Level = 1
        self.EXP = 0
        self.HP = 1
        self.MaxHP = 1
        self.Strength = 1
        self.Durability = 1
        self.Speed = 1
        self.Accuracy = 1
        self.Evasion = 1

    def set_stats(self, dict):
        for stat in dict:
            if hasattr(self, stat):
                setattr(self, dict[stat])

    def mult_stats(self, mult):
        self.HP *= mult
        self.MaxHP *= mult
        self.Strength *= mult
        self.Durability *= mult
        self.Speed *= mult
        self.Accuracy *= mult
        self.Evasion *= mult

    def move(self, d):
        if not isinstance(d, str):
            return False
        findRoom = getattr(self.room, f'{d[0:1]}_to')
        from room import Room
        if not isinstance(findRoom, Room):
            print('You can\'t move that way.')
            return False
        findRoom.enter(self)
        return True

    def move_to(self, room):
        from room import Room
        if not isinstance(room, Room):
            return False
        self.room = room
        return True

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


class Player(Mob):
    def __init__(self, name, desc, room):
        Mob.__init__(self, name, desc, room)

    def inventory(self):
        print('### Your inventory ###')
        for i in self.items:
            print(i)