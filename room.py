class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.item = None
        self.character = None
        self.direction = []

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.direction = direction
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        tot = 0
        print(f"You're in the {self.name}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"({direction} you can find the {room.get_name()})")
        print("\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

