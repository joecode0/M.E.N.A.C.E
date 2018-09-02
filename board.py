from errors import InvalidMoveError


class Board(object):

    def __init__(self):
        self.state = [0]*9
        self.moves_count = 0

    def check_finished(self, p):
        """Quick Function to check if game is finished (3 in a row or draw)
        Args:
            p (int): Last Player: 1 = Player 1, 2 = Player 2
        Returns:
            Winner (int): 0 = Game Unfinished, 1 = Player 1, 2 = Player 2, 3 = Draw
        """
        if self.moves_count > 4:
            s = self.state
            # Game can't have finished in under 5 moves
            if s[4] == p:  # i.e, if player p has played in position 4 in Board.state
                # Half 3 in a rows include middle square
                if (s[0] == p and s[8] == p) or (s[2] == p and s[6] == p):
                    return p
                elif (s[1] == p and s[7] == p) or (s[3] == p and s[5] == p):
                    return p
            # No 3 in a row through middle
            if s[0] == p:
                if (s[6] == p and s[3] == p) or (s[1] == p and s[2] == p):
                    return p
            elif s[8] == p:
                if (s[6] == p and s[7] == p) or (s[2] == p and s[5] == p):
                    return p
            # No 3 in a row
            elif self.moves_count == 8:
                # Board must be full
                return 3
        return 0

    def play_move(self, pos, player):
        """Attempts to put [player] into [pos] of [self.state]
        Args:
            pos (int): Index of Board position to play in
            player (int): Either Player 1 or Player 2
        Raises:
            InvalidMove: Returns list of valid moves as indices into state
        Returns:
           Winner (int): 0 = Game Unfinished, 1 = Player 1, 2 = Player 2, 3 = Draw
        """
        if self.state[pos] == 0:
            self.state[pos] = player
            self.moves_count += 1
            return self.check_finished(player)
        else:
            valid_moves = self.get_valid_moves()
            raise InvalidMoveError(valid_moves)

    def get_valid_moves(self):
        return [i for i in range(9) if self.state[i] is 0]

    def terminal_board_print(self, next_player):
        print("Make your move Player {}...".format(next_player))
        print()
        padding = "     "
        dashes = "---------"

        print("{}---------------".format(padding))
        print("{}|             |".format(padding))
        print("{}|  {} | {} | {}  |".format(
            padding, self.state[0], self.state[1], self.state[2]))
        print("{}|  {}  |".format(padding, dashes))
        print("{}|  {} | {} | {}  |".format(
            padding, self.state[3], self.state[4], self.state[5]))
        print("{}|  {}  |".format(padding, dashes))
        print("{}|  {} | {} | {}  |".format(
            padding, self.state[6], self.state[7], self.state[8]))

        print("{}|             |".format(padding))
        print("{}---------------".format(padding))

    def reset_board(self):
        self.state = [0]*9
