class Match():


    def __init__(self, player_one, player_two):
        #receive all data from the match
        self.player_one = player_one
        self.player_two = player_two

    def place_bombs(self, player):
        if self.player_one.name == player.name:
            for ship in self.player_two._ships:
                for bomb in self.player_one._bombs_positions:
                    if bomb in self.player_two.ship.structure:
                        ship.structure[bomb] = 1

        elif self.player_two.name == player.name:
            for ship in self.player_one._ships:
                for bomb in self.player_two._bombs_positions:
                    if bomb in ship.structure:
                        ship.structure[bomb] = 1

    def launch_bomb(self, player, bomb_position):

        if self.player_one.name == player.name:
            if bomb_position in self.player_one._bombs_positions:
                print("Position {} Already Bombed".format(bomb_position))
            else:
                self.player_one._bombs_positions.append(bomb_position)
            self.place_bombs(self.player_one)
        elif self.player_two.name == player.name:
            if bomb_position in self.player_two._bombs_positions:
                print("Position {} Already Bombed".format(bomb_position))
            else:
                self.player_two._bombs_positions.append(bomb_position)
            self.place_bombs(self.player_two)

    def verify_ships_status(self):
        #plot ship into the board
            print("After this round, this are the status of player one ships")
            for ship in self.player_one._ships:

                if all(ship.structure[position] == 1 for position in ship.positions):
                    print ("ship {} defeated".format(ship.name))

                elif any(ship.structure[position] == 1 for position in ship.positions):
                    print ("ship {} damaged".format(ship.name))

                else:
                    print ("ship {} survived with no damage ".format(ship.name))

            print("After this round, this are the status of player two ships")

            for ship in self.player_two._ships:
                if all(ship.structure[position] == 1 for position in ship.positions):
                    print ("ship {} defeated".format(ship.name))

                elif any(ship.structure[position] == 1 for position in ship.positions):
                    print ("ship {} damaged".format(ship.name))

                else:
                    print ("ship {} survived with no damage ".format(ship.name))
