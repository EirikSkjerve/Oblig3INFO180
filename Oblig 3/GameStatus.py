'''
 A representation of the current status of the Invitation game
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''

import copy
from Candidate import Candidate


class GameStatus:

    def __init__(self, game_status=None):
        '''
        Constructor
        :param game_status:
        '''
        if game_status is not None:
            # create game status as copy of games
            self.to_move = game_status.to_move.copy()
            self.other = game_status.other.copy()
            self.remaining_candidates = copy.deepcopy(game_status.remaining_candidates)
        else:
            # create an initial game status
            self.to_move = None
            self.other = None
            self.remaining_candidates = copy.deepcopy(Candidate.candidates)

    def finished(self):
        '''
        Checks if game is finished
        :return:
        '''
        return len(self.remaining_candidates) <= 0

    def remaining_compatibility(self, player):
        '''
        The remaining compatibility for player (either 1 or 2)
        :param player:
        :return:
        '''
        sum = 0
        if player.compatibility_score_set == 1:
            for c in self.remaining_candidates:
                sum += c.compatibility1
        elif player.compatibility_score_set == 2:
            for c in self.remaining_candidates:
                sum += c.compatibility2
        return sum

    def current_score(self):
        '''
        Value of score is own score - opponent's score
        :return:
        '''
        return self.to_move.score() - self.other.score()

    def remaining_to_string(self):
        '''
        A string representation of candidates
        :return:
        '''
        string = ""
        string += "Remaining players to choose from\n"
        string += "      \t\tCompatibility\n"
        string += "No\tCand.\t"+ str(self.to_move.name) + "\t" + str(self.other.name) + "\n"
        for i in range(len(self.remaining_candidates)):
            c = self.remaining_candidates[i]
            if self.to_move.compatibility_score_set == 1:
                to_move_comp = c.compatibility1
                other_comp = c.compatibility2
            else:
                to_move_comp = c.compatibility2
                other_comp = c.compatibility1
            string += str(i) + "\t" + str(c.name) + "\t" + str(to_move_comp) + "\t" + str(other_comp) + "\n"

        string += "\tSum\t" + str(self.remaining_compatibility(self.to_move)) + "\t" + str(self.remaining_compatibility(self.other))
        return string

    def move(self, i):
        '''
        Doing a move is by allowing the one to move to select a move by its own method
        :param i:
        :return:
        '''
        self.to_move.move(self, i)

