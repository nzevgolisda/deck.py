

class Card:
    def __init__(self, No, Se):
        self.No = No
        self.season = Se
        
    def __str__(self):
        return str([self.No, self.season])