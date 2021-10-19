'''
    Abstract class representing a player and its behaviour in the Invitation Game
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''

from abc import ABC
import copy


class Player(ABC):
    '''
    Abstract class that represents a plyer, either human or machine
    '''

    def __init__(self, compatibility_score_set):
        '''
        constructor using a compatability_score_set as parameter
        :param compatibility_score_set:
        '''
        self.chosen = []
        self.compatibility_score_set = compatibility_score_set
        self.name = ""

    def score(self):
        '''
        Evaluates the current score of a player
        :return: current score of player
        '''
        sum = 0
        for candidate in self.chosen:
            sum += candidate.score(self.compatibility_score_set)
        return sum

    def chosen_to_string(self):
        '''
        :return: a string representation of the chosen participants for the player
        '''
        string = ""
        for candidate in self.chosen:
            string += candidate.name
            string += "(" + str(candidate.score(self.compatibility_score_set)) + ") "
        return string

    def move(self, game_status, i):
        '''
        Computes a possible move for this player and modifies the game status
        :param game_status: current status of game
        :param i: candidate list 1 or 2
        :return: nothing
        '''
        candidate = copy.deepcopy(game_status.remaining_candidates.pop(i))
        self.chosen.append(candidate)
        game_status.to_move = game_status.other
        game_status.other = self

    def print_move(self, game_status, index):
        '''
        Prints the selected move
        :param game_status:
        :param index:
        :return:
        '''
        print(str(self.name) + " chose " + str(index) + " " + str(game_status.remaining_candidates[index].name) + "("
              + str(game_status.remaining_candidates[index].score(self.compatibility_score_set)) + ")\n")

    def make_move(self, game_status): pass
    '''
    Abstract method
    '''

    def copy(self): pass
    '''
    Abstract method
    '''


