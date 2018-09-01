class InvalidMoveError(ValueError):
    '''Raise when an attempted move is invalid'''

    def __init__(self, valid_moves):
        self.valid_moves = valid_moves
        super(InvalidMoveError, self).__init__(valid_moves)
