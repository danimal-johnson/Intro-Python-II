# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return "{} is in the room {}".format(self.name, self.current_room.name)

    def collect_item(self, item):
        self.inventory.add(item)
