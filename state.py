import chess


class State(object):
    def __int__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bits according to README
        pass

    def value(self):
        # TODO : Add neural net here
        return 1  # all board positions are equal

    def edges(self):
        return list(self.board.legal_moves)


if __name__ == '__main__':
    s = State()
    print(s.edges())
