'''
 Class represnting the "machine" that runs the human vs. comptuer player'
    Written originally in Java by Bjørnar Tessem
    Translated to python by Sondre Bolland
'''
from GameStatus import GameStatus
from HumanPlayer import HumanPlayer
from SimpleComputerPlayer import SimpleComputerPlayer
from AdvancedComputerPlayer import AdvancedComputerPlayer


# Class to select candidates
class SelectParty:

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.game_status = GameStatus()

    def select_starter(self):
        '''
        Asking the human player who shall start
        :return:
        '''
        while self.game_status.to_move is None:
            answer = input("Do you want to start? (Y/N)")
            if answer == "Y" or answer == "y":
                self.player1 = HumanPlayer(1)
                self.player2 = AdvancedComputerPlayer(2)
                self.game_status.to_move = self.player1
                self.game_status.other = self.player2

            if answer == "N" or answer == "n":
                self.player1 = HumanPlayer(2)
                self.player2 = AdvancedComputerPlayer(1)
                self.game_status.to_move = self.player2
                self.game_status.other = self.player1


    def select_move(self):
        '''
        Allowint the one who is to move to do the actual move
        :return:
        '''
        self.game_status.to_move.make_move(self.game_status)

    def finished(self):
        '''
        Is game finished
        :return:
        '''
        return self.game_status.finished()

    def print_result(self):
        '''
        Prints the final result of the game
        :return:
        '''
        if self.player1.score() > self.player2.score():
            print(self.player1.name + " WON! ")
        elif self.player1.score() < self.player2.score():
            print(self.player2.name + " WON! ")
        else:
            print("DRAW")

        print(self.player1.name, " chose: ", self.player1.chosen_to_string())
        print("Score: ", self.player1.score())

        print(self.player2.name, " chose: ")
        print(self.player2.chosen_to_string())
        print("Score: ", self.player2.score())

    def print_status(self):
        '''
        Prints status of the game
        :return:
        '''
        if self.game_status.to_move == self.player1:
            print("To move: " + self.game_status.to_move.name)
            print("Selected: " + self.game_status.to_move.chosen_to_string())
            print("Score: ", self.game_status.to_move.score())
            print("")

            print("To move: " + self.game_status.other.name)
            print("Selected: " + self.game_status.other.chosen_to_string())
            print("Score: ", self.game_status.other.score())
            print("")
            print(self.game_status.remaining_to_string())

