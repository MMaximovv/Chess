"""Chess"""

def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board


def display_board(board):
    for row in board:
        print(' '.join(row))


def main():
    board = initialize_board()
    while True:
        display_board(board)
        move = input("Введите ход (например e2-e4): ").strip()
        if move == "quit":
            break
        start, end = move.split('-')
        start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
        end_x, end_y = ord(end[0]) - ord('a'), int(end[1]) - 1
        board[end_y][end_x] = board[start_y][start_x]
        board[start_y][start_x] = '.'

if __name__ == '__main__':
    main()
