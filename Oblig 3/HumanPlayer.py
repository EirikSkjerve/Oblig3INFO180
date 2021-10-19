'''
 Class implementing a human player in theinvitation game
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''

from Player import Player
import copy


class HumanPlayer(Player):
    '''
        Implementation of human player
    '''

    def __init__(self, compatibility_score_set):
        '''
        constructor
        :param compatibility_score_set:
        '''
        super(HumanPlayer, self).__init__(compatibility_score_set)
        self.name = "You"

    # Lets a player give input to choose candidates
    def make_move(self, game_status):
        '''
        code for allowing human player to enter candidate
        :param game_status:
        :return:
        '''
        accepted = False

        while not accepted:
            answer = input("Choose move (integer) > ")
            try:
                index = int(answer)
            except:
                print(answer, " is not a number")
                continue

            if index < len(game_status.remaining_candidates):
                accepted = True
            else:
                print(answer, " illegal move!")
        self.print_move(game_status, index)
        self.move(game_status, index)

    def copy(self):
        '''
        A copy method for self
        :return:
        '''
        result = copy.deepcopy(self)
        return result
