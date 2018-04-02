class Match():

    def __init__(self, ship_owner, bomb_owner):
        #receive all data from the match
        self.ship_owner = ship_owner
        self.bomb_owner = bomb_owner
        self.ships = ship_owner._ships
        self.bombs_positions = bomb_owner.bombs_position
        self.place_bombs()

    def place_bombs(self):
        for ship in self.ships:
            for bomb in self.bombs_positions:
                if bomb in ship.positions:
                    ship.structure[bomb] = 1


        print("-------------------------")
        self.verify_ships_status()

    def verify_ships_status(self):
        #plot ship into the board
        for ship in self.ships:
            if all(ship.structure[position] == 1 for position in ship.positions):
                print ("ship {} defeated".format(ship.name))

            elif any(ship.structure[position] == 1 for position in ship.positions):
                print ("ship {} damaged".format(ship.name))

            else:
                print ("ship {} survived with no damage ".format(ship.name))
