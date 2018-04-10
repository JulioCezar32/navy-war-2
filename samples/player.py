class Player():

    def __init__(self, name):
        self.name = name
        self._ships = []
        self._ships_positions = []
        self._board_position_validation = []
        self._bombs_positions = []

    def create_ship(self, ship):
        ship_status = self.is_some_ship_overlaid(ship)
        if ship_status == 0:
            self._ships.append(ship)
            self._ships_positions.append(ship.structure)
            message = "Ship {} inserted correctly".format(ship.name)
        else:
            message = "The Ship {} was inserted into a wrong position".format(ship.name)
            #perguntar sobre esse tipo de mensagem retornada ao usuário, deve ser escrita
            #dentro do código ou chamar uma função que tem a função de criar a mensagem.
        print(message)

    def is_some_ship_overlaid(self, ship):
        if any(x in self._board_position_validation for x in ship.positions):
            return 1
            #returning 0 or 1 is the best way to say about the overlay?
        else:
            self._board_position_validation.extend(ship.positions)
            return 0
