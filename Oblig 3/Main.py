'''
 A python file for running the Invitation Game
    @auth Eirik Skjerve
'''


from Candidate import Candidate
from SelectParty import SelectParty


Candidate.random_assignment()
game = SelectParty()
game.select_starter()

while not(game.finished()):
    game.print_status()
    game.select_move()

game.print_result()