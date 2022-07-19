#! python3.19.4
# Start
# Factory Method Pattern getting started passes the builder pattern
# Honestly That was a damnly Headache but to be honest again,
# now i feel relived x) ###
""" Chess game not Written yet the more information will be added
as soon as possible """
# Modules
'''not imported yet!'''

BLACK, WHITE = ("BLACK", "WHITE")


class AbstractBoard:

    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()

    def populate_board(self):
        raise NotImplementedError()

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                # console return a string representation on the given background color
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)


class CheckersBoard(AbstractBoard):
    """ inheriates from AbstractBoard to show all bullshitlically pashmaki
    damn what im saying idk my mind isn't working but will implement
    the chess methods and if dont impolement any of the parent class
    will raise a NotImplementedError! """

    def __init__(self):
        super().__init__(10, 10)

    def populate_board(self):
        super().populate_board()
        for x in range(0, 9, 2):
            for row in range(4):
                column = x + ((row + 2) % 2)
                self.board[row][column] = BlackDraught()
                self.board[row + 6][column] = WhiteDraught()

    def populate_board(self):
        for x in range(0, 9, 2):
            for y in range(4):
                column = x + ((y +1) % 2)
                for row, color in ((y, "black"), (y + 6, 'white')):
                    self.board[row][column] = create_piece("draught", color)

class ChessBoard(AbstractBoard):
    """ the Chessboard it self
    inheriating from AbstractBoard
    working for drawing chess board """

    def __init__(self):
        super().__init__(8, 8)
    
    def populate_board(self):
        super().populate_board()
        self.board[0][0] = BlackChessRock()
        self.board[0][1] = BlackChessKnight()
        self.board[0][2] = BlackChessBishop()
        self.board[0][3] = BlackChessKing()
        self.board[0][4] = BlackChessQueen()
        self.board[0][5] = BlackChessBishop()
        self.board[0][6] = BlackChessKnight()
        self.board[0][7] = BlackChessRock()
        self.board[6][0] = WhiteChessRock()
        self.board[6][1] = WhiteChessKnight()
        self.board[6][2] = WhiteChessBishop()
        self.board[6][3] = WhiteChessKing()
        self.board[6][4] = WhiteChessQueen()
        self.board[6][5] = WhiteChessBishop()
        self.board[6][6] = WhiteChessKnight()
        self.board[6][7] = WhiteChessRock()

class Piece(str):
    __slots__ = ()

class BlackDraught(Piece):
    __slots__ = ()

    def __new__(cls):
        return super().__new__(cls, "\N{black draughts man}")

class WhiteDraught(Piece):
    __slots__ = ()
    
    def __new__(cls):
        return super().__new__(cls, "\N{black draughts man}")



class WhiteChessKing(Piece):
    __slots__ = ()

    def __new__(cls):
        return super().__new__(cls, "\N{white chess king}")


def main():
    checkers = CheckrsBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess)


# End
