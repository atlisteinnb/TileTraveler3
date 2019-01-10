class Player():
    def __init__(self, player_pos, gold = 3):
        self.gold = gold
        self.player_pos = player_pos

    def __repr__(self):
        return '{}'.format(Player())

    def player_move(self):
        pass

    def get_gold(self):
        pass

    def 

    

class Grid():
    def __init__(self, dimensions, room_list):
        self.__grid = []
        index = 0
        for row in range(0, dimensions):
            room_row_list = []
            for column in range(0,dimensions):
                room_row_list.append(room_list[index])
                index += 1
            self.__grid.append(room_row_list)

    def __str__(self):
        return_string = ''
        for item in self.__grid:
            return_string += str(item) + ' '
        return return_string

room_list = [1,2,3,4,5,6,7,8,9]
level1 = Grid(3, room_list)
print(level1)


class Room():
    def __init__(self, move_info, coins):
        self.row = 0
        self.column = 0
        self.validDirections = []
        self.lever = bool
        self.coins
    
    def pull_lever(self):
        pass

    def lever_position(self):
        pass


    