from board import Board
import utils as u


class MENACE(object):

    def __init__(self, player):
        self.player = player
        self.generate_new_data_dict()

    def generate_new_data_dict(self):
        state_list = self.generate_all_possible_states()
        board_list = []
        data_dict = dict()
        for state in state_list:
            b = Board(state)
            board_list.append(Board(state))
            valid_moves = 5  # TODO

    def generate_all_possible_states(self):
        all_states = []
        if self.player == 1:
            all_states.append([0]*9)
            all_states.extend(u.perms([1, 2] + [0]*7))
            all_states.extend(u.perms([1, 2]*2 + [0]*5))
            all_states.extend(u.perms([1, 2]*3 + [0]*3))
            all_states.extend(u.perms([1, 2]*4 + [0]))
        elif self.player == 2:
            all_states.extend(u.perms([1] + [0]*8))
            all_states.extend(u.perms([1]*2 + [2] + [0]*6))
            all_states.extend(u.perms([1]*3 + [2]*2 + [0]*4))
            all_states.extend(u.perms([1]*4 + [2]*3 + [0]*2))
        return all_states
