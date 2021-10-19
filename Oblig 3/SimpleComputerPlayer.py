'''
 A concret implementation of a simple computer player
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''
from ComputerPlayer import ComputerPlayer
import copy



class SimpleComputerPlayer(ComputerPlayer):
    '''
    A simple AI checking the game's staus and selecting the move according to own evaluate_game_status-method
    '''

    def __init__(self, compatibility_score_set):
        super(SimpleComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "SimpleComp"


    def evaluate_game_status(self, game_status):
        '''
        Heuristic function to evaluate the current state of the game
        :param game_status:
        :return: the difference in the scores for each player
        '''
        return game_status.to_move.score() - game_status.other.score()

    def copy(self):
        '''
        A copy method
        :return:
        '''
        result = SimpleComputerPlayer(self.compatibility_score_set)
        result.chosen = copy.deepcopy(self.chosen)
        return result
