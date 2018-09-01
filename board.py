class Board(object):

    def __init__(self):
        self.state = [0]*9
        self.finished = False
        self.moves_count = 0

    def check_finished(self, player):
        """Quick Function to check if game is finished (3 in a row or draw)
        Args:
            player (int): Returns player: 1 = Player 1, 2 = Player 2
        Returns:
            [int]: Returns winner. Either 0: Game Unfinished, 1: Player 1, 2: Player 2, 3: Draw
        """

        if self.moves_count > 4:
            # Game can't have finished in under 5 moves
            if self.state[4] == player:
                # Half 3 in a rows include middle square
                if self.state[0] == player and self.state[8] == player:
                    self.finished = True
                    return player
                elif self.state[2] == player and self.state[6] == player:
                    self.finished = True
                    return player
                elif self.state[1] == player and self.state[7] == player:
                    self.finished = True
                    return player
                elif self.state[3] == player and self.state[5] == player:
                    self.finished = True
                    return player
            # No 3 in a row through middle
            if self.state[0] == player:
                if self.state[6] == player and self.state[3] == player:
                    self.finished = True
                    return player
                elif self.state[1] == player and self.state[2] == player:
                    self.finished = True
                    return player
            elif self.state[8] == player:
                if self.state[6] == player and self.state[7] == player:
                    self.finished = True
                    return player
                elif self.state[2] == player and self.state[5] == player:
                    self.finished = True
                    return player
            # No 3 in a row
            elif self.moves_count == 8:
                # Board must be full
                self.finished = True
                return 3
        return 0
