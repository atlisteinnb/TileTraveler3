class Player():
    def __init__(self, player_pos, gold = 3):
        self.gold = gold
        self.player_pos = player_pos

class Grid():
    def __init__(self, dimension):
        self.dimension = dimension

class Room():
    def __init__(self, move_info, coins):
        self.row = 0
        self.column = 0
        self.validDirections = []
        self.lever = bool
        self.coins