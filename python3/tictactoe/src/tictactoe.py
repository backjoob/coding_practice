#!/usr/bin/python3

from array import array


class TicTacToeException(Exception):
    """
    Parent exception for TicTacToe errors
    """

class InvalidMoveException(TicTacToeException):
    """
    Denotes that an invalid move has been attempted
    """

class InvalidPlayerException(TicTacToeException):
    """
    Denotes that a player attempted to play out of turn
    """

class TicTacToe:
    """
    Maintains state for a Tic Tac Toe game.
    Defines mutators on state.
    """

    NUM_PLAYERS = 2
    NUM_ROWS = 3
    NUM_COLS = 3

    @property
    def num_spaces(self):
        return self.NUM_ROWS * self.NUM_COLS

    def __init__(self):
        """Initialize a new Tic Tac Toe object"""
        # Initialize an empty board state where empty board states are represented by -1
        self.boardstate = array("b", [-1] * (self.NUM_ROWS * self.NUM_COLS))
        # Initialize first player
        self.current_player = 0
        # Initialize history
        self.history = []

    @classmethod
    def i_to_rc(cls, index):
        """Convert an index to rows and cols"""
        return (index // cls.NUM_COLS, index % cls.NUM_COLS)

    @classmethod
    def rc_to_i(cls, indices):
        """Convert rows and cols to an index"""
        row, column = indices
        return row * cls.NUM_COLS + column

    def play(self, player, indices):
        """Play for `player` at position `index`.

        Args:
            player: The player attempting to make a move.
            indices: A tuple containing a row and column.

        Returns:
            None

        Raises:
            InvalidPlayerException: It is not `player`'s turn.
            InvalidMoveException: The space at `indices` is not empty.
        """
        if player != self.current_player:
            raise InvalidPlayerException(
                f"Attempting to move for {player}, but it is {self.current_player}'s turn."
            )
        index = self.rc_to_i(indices)
        if self.boardstate[index] != -1:
            raise InvalidMoveException(
                f"There is already a {self.boardstate[index]} in position {indices}."
            )
        self.boardstate[index] = self.current_player
        self.current_player = (self.current_player + 1) % self.NUM_PLAYERS

    def __str__(self):
        return "\n".join(
            "\t".join(map(str, self.boardstate[i : i + self.NUM_COLS]))
            for i in range(0, self.num_spaces, self.NUM_COLS)
        )


def main():
    t = TicTacToe()
    print(t)
    print()
    for i in range(t.num_spaces):
        t.play(i % 2, t.i_to_rc(i))
    print(t)


if __name__ == "__main__":
    main()
