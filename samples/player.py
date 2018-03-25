class Player():

    def __init__(self, name):
        self.name = name
        self._ships = []
        self.ships_positions = []
        self._board_position_validation = []
        self.bombs_position = []

    def create_ship(self, ship):
        ship_status = self.verify_if_ship_will_be_choked(ship)
        if ship_status == 0:
            self._ships.append(ship)
            self.ships_positions.append(ship.structure)
            message = "Ship {} inserted correctly".format(ship.name)
        else:
            message = "The Ship {} was inserted into a wrong position".format(ship.name)
        print(message)

    def launch_bomb(self, position):
        if position in self.bombs_position:
            print("Position {} Already Bombed".format(position))
        else:
            self.bombs_position.append(position)

    def verify_if_ship_will_be_choked(self, ship):
        if any(x in self._board_position_validation for x in ship.positions):
            return 1
        else:
            self._board_position_validation.extend(ship.positions)
            return 0
