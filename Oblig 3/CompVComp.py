

from SimpleComputerPlayer import SimpleComputerPlayer
from AdvancedComputerPlayer import AdvancedComputerPlayer
from SelectPartyComps import SelectPartyComps
from Candidate import Candidate


if __name__ == "__main__":  
    advanced_score = 0
    simple_score = 0
    for i in range(100):
        game = SelectPartyComps()
        Candidate.random_assignment()
        while not(game.finished()):
            game.select_move()
        advanced_score += game.player1.score()
        simple_score += game.player2.score()
    print("Advanced Computer score over 100 games: " + str(advanced_score))
    print("Simple Computer score over 100 games: " + str(simple_score))

    print("Average for advanced: " + str(advanced_score/100))
    print("Average for simple: " + str(simple_score/100))

        