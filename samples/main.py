from ships_models import *
from player import Player
from match import *
player_one = Player('Julio')
player_two = Player('Carlos')
player_one.create_ship(Destroyer('3A'))
player_one.create_ship(PortaAvioes('10C'))
player_one.create_ship(Encouracado('4D '))
print("---------------------------------")
player_two.launch_bomb('3A')
player_two.launch_bomb('3A')
player_two.launch_bomb('5A')
player_two.launch_bomb('4D')

game = Match(player_one, player_two)
