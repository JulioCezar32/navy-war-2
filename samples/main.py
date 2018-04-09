from ships_models import *
from player import Player
from match import *
player_one = Player('Julio')
player_two = Player('Carlos')
player_one.create_ship(Destroyer('3A'))
player_one.create_ship(PortaAvioes('10C'))
player_one.create_ship(Encouracado('4D '))
print("---------------------------------")
match_one = Match(player_one, player_two)
match_one.launch_bomb(player_two,'3A')
match_one.launch_bomb(player_two,'3A')
