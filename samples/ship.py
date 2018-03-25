class Ship():

    def __init__(self, structure):
        self.head = structure['head']
        self.name = structure['name']
        self.size = structure['size']
        self.generate_structure()
        self.status = self.Verify_If_All_Positions_Are_Right()

    def generate_structure(self):
        self.positions = []
        head_column = self.head[1]
        head_row = self.head[0]
        for position in range(self.size):
            ship_next_row = int(head_row) + position
            ship_body = str(ship_next_row) + head_column
            self.positions.append(ship_body)
        self.structure = {position : 0 for position in self.positions}


    def Verify_If_All_Positions_Are_Right(self):
        self.board = self.Set_all_right_positions()
        if all(x in self.board for x in self.positions):
            return 0
            #print("the ship is in a right position")
        else:
            print("Ship {} placed is out of the game border".format(self.ship))
            return 1

    def Set_all_right_positions(self):
        board_size = 5
        rows_numbers = range(1, board_size + 1)
        columns_letters = "ABCDEFGHIJKLMNOPQRSTUVXZ"[:board_size]
        board_positions = []
        for row in rows_numbers:
            for columns in columns_letters:
                position = str(row) + columns
                board_positions.append(position)
        return board_positions
