'''
 A class for representing a computer player in the Invitation Game
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''

from Player import Player
from GameTreeNode import GameTreeNode


class ComputerPlayer(Player):
    '''
    An abstract computer player class
    '''

    def __init__(self, compatibility_score_set):
        '''
        Constructor
        :param compatibility_score_set:
        '''
        super(ComputerPlayer, self).__init__(compatibility_score_set)
        self.name = "Comp"

    # Finds the best possible candidate to select and selects him
    def make_move(self, game_status):
        '''
        Use an algorithm to find a good candidate move
        :param game_status:
        :return:
        '''
        selected_candidate_idx = self.select_candidate(game_status)
        self.move(game_status, selected_candidate_idx)

    def select_candidate(self, game_status):
        '''
        Runs alfa beta search to find candidate
        :param game_status:
        :return:
        '''
        root = GameTreeNode(game_status)
        root.computer_player = self
        root.search()

        return root.best_move

    def evaluate_game_status(self, game_status): pass
    '''
    method to be implemented in each subclass
    '''

