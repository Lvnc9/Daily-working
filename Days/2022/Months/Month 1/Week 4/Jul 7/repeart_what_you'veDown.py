#! python3.10.4
# Start
# repeating __str__ part of the chess game


BLACK, WHITE = ('BLACK', 'WHITE')
class AbstractBoard:

    def __init__(self, rows, columns):
        self.board = [[None for _ in range (rows)] for _ in range(rows)]
        self.populate_board()

    def populate_board(self):
        raise NotImplementedError()
    
    def __str__(self):
        squares = []
        for y,row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            square.append("\n")
        return "".join(square)



# End