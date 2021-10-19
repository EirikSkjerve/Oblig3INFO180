'''
 More advanced implementation of a computer player
 @Auth Eirik Skjerve 
'''
from ComputerPlayer import ComputerPlayer
import copy



class AdvancedComputerPlayer(ComputerPlayer):
    '''
    A simple AI checking the game's staus and selecting the move according to own evaluate_game_status-method
    '''

    def __init__(self, compatibility_score_set):
        super(AdvancedComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "AdvancedComp"


    def evaluate_game_status(self, game_status):
        '''
        Heuristic function to evaluate the current state of the game
        :param game_status:
        :return: the difference in the scores for each player
        I tillegg har jeg lagt til forskjellen i compatibility for at heurestikken skal bli bedre
        '''
        return (game_status.to_move.score() - game_status.other.score()) + (
            game_status.remaining_compatibility(game_status.to_move) - game_status.remaining_compatibility(game_status.other))
        
        
        #return game_status.to_move.score() - game_status.other.score()

    def copy(self):
        '''
        A copy method
        :return:
        '''
        result = AdvancedComputerPlayer(self.compatibility_score_set)
        result.chosen = copy.deepcopy(self.chosen)
        return result
