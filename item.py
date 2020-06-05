class Item:

    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.power = {}
        self.location = {}

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_power(self, item_power):
        self.power = item_power

    def get_power(self):
        return self.power

