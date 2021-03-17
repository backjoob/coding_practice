#!/usr/bin/python3

from array import array

class InvalidMoveException(Exception):
    """
    Denotes that an invalid move has been attempted.
    """

class TicTacToe:
    '''
    Maintains state for a Tic Tac Toe game.
    Defines mutators on state.
    '''
    NUM_PLAYERS = 2
    NUM_ROWS = 3
    NUM_COLS = 3

    @property
    def num_spaces(self):
        return self.NUM_ROWS * self.NUM_COLS

    def __init__(self):
        # Initialize an empty board state where empty board states are represented by -1
        self.boardstate = array('b', [-1] * (self.NUM_ROWS * self.NUM_COLS))
        # Initialize first player
        self.current_player = 0
        # Initialize history
        #self.history = []

    def play(self, index):
        if self.boardstate[index] == -1:
            self.boardstate[index] = self.current_player
            self.current_player = (self.current_player + 1) % self.NUM_PLAYERS
        else:
            raise InvalidMoveException(
                f"There is already a {self.boardstate[index]} in index {index}.")

    def __str__(self):
        return "\n".join("\t".join(map(str, self.boardstate[i:i+self.NUM_COLS]))
            for i in range(0, self.num_spaces, self.NUM_COLS))

def main():
    t = TicTacToe()
    print(t)
    print()
    for i in range(t.num_spaces):
        t.play(i)
    print(t)



if __name__ == '__main__':
    main()
