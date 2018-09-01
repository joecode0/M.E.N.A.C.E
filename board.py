class Board(object):

    def __init__(self):
        self.state = [0]*9
        self.finished = False
        self.moves_count = 0

    def check_finished(self, player):
        if self.moves_count > 4:
            # Game can't have finished in under 5 moves
            if self.state[4] == player:
                # Half 3 in a rows include middle square
                if self.state[0] == player and self.state[8] == player:
                    self.finished = True
                    return
                elif self.state[2] == player and self.state[6] == player:
                    self.finished = True
                    return
                elif self.state[1] == player and self.state[7] == player:
                    self.finished = True
                    return
                elif self.state[3] == player and self.state[5] == player:
                    self.finished = True
                    return
            # No 3 in a row through middle
            if self.state[0] == player:
                if self.state[6] == player and self.state[3] == player:
                    self.finished = True
                    return
                elif self.state[1] == player and self.state[2] == player:
                    self.finished = True
                    return
            elif self.state[8] == player:
                if self.state[6] == player and self.state[7] == player:
                    self.finished = True
                    return
                elif self.state[2] == player and self.state[5] == player:
                    self.finished = True
                    return
            # No 3 in a row
            else:
                for i in range(9):
                    if self.state[i] == 0:
                        return
                # Board must be full
                self.finished = True
                return
