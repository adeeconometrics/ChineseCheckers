from typing import Dict, List, Union
from os import system

menu: str = "________________________________________\n\
    \nChoose an action: \n\
    \n[1] Play 7 x 6 board\
    \n[2] Play 8 x 7 board\
    \n[3] How to Play\
    \n[4] Exit\n\
_________________________________________\n"

instructions: str = "There are two types of board sizes, namely 7x6 and 8x7. \
                    Players alternately put their discs. Outsmart your opponent \
                    by making 4 consecutive lines of discs horizontally, vertically \
                    or diagonally in 7x6 and 5 discs in 8x7 board size."

meta = {
    'screenboard': [[]], 
    'player_1': {
        'score': 0,
        'moves': 0
    },
    'player_2': {
        'score': 0,
        'moves': 0
    }, 
    
    'dims': {
        'row': 0,
        'col': 0
    }
}


def create_board(row:int, col:int):
    global meta
    meta['screenboard'] = [[None for _ in range(col)] for _ in range(row)]
    meta['dims']['row'] = row
    meta['dims']['col'] = col


def start_game(meta: Dict[str, Union[List[List[Union[str, None]]], Dict[str, int]]]):
    turn: int = 0
    row, col = meta['dims']['row'], meta['dims']['col']

    if (row, col) == (6, 7):
        while not winning_move1(row, col):
            if turn == 0:
                choice = int(input("Player 1: Enter desired column: "))
                drop_piece(choice, "V", row)
                print(to_string(meta['screenboard']))

                meta['player_1']['moves'] += 1
                is_save = input("Save current game? Press [1] if YES")

                if is_save == '1':
                    save_file('saved_game')

                if winning_move1(row, col):
                    print("Player 1 wins!")
                print(f"Total number of moves:  {meta['player_1']['moves'] }")

            else:
                choice = int(input("Player 2: Enter desired column: "))
                drop_piece(choice, "O", row)
                print(to_string(meta['screenboard']))

                meta['player_2']['moves'] += 1
                is_save = input("Save current game? Press [1] if YES")

                if is_save == '1':
                    save_file('saved_game')

                if winning_move1(row, col):
                    print("Player 2 wins!")
                print(f"Total number of moves:  {meta['player_2']['moves'] }")

            turn += 1
            turn = turn % 2

    elif (row, col) == (7, 8):
        while not winning_move2(row, col):
            if turn == 0:
                choice = int(input("Player 1: Enter desired column: "))
                drop_piece(choice, "V", row)
                print(to_string(meta['screenboard']))
                meta['player_1']['moves'] += 1

                if winning_move2(row, col):
                    print("Player 1 wins!")

                print(f"Total number of moves: {meta['player_1']['moves'] }")

            else:
                choice = int(input("Player 2: Enter desired column: "))
                drop_piece(choice, "O", row)
                print(to_string(meta['screenboard']))
                meta['player_2']['move'] += 1

                if winning_move2(row, col):
                    print("Player 2 wins!")
                print(f"Total number of moves: {meta['player_1']['moves'] }")

            turn += 1
            turn = turn % 2


def drop_piece(col: int, piece: str, row: int,
             screenboard: List[List] = meta['screenboard']) -> None:
    """
    checks if the cell is none; if so, adds element
    """
    col = col - 1
    for rows in range(row-1, -1, -1):
        if screenboard[rows][col] is None:
            print('legal move')  # REMOVE THIS LATER
            screenboard[rows][col] = piece
            break


def winning_move1(row: int, col: int,
             screenboard: List[List] = meta['screenboard']) -> bool:

    #DIAGONAL WIN
    for i in range(3, row):
        for j in range(4):
            if screenboard[i][j] is not None:
                if screenboard[i][j] == screenboard[i-1][j+1] == \
                        screenboard[i-2][j+2] == screenboard[i-3][j+3]:
                    return True
    #HORIZONTAL WIN
    for i in range(row):
        for j in range(4):
            if screenboard[i][j] is not None:
                if screenboard[i][j] == screenboard[i][j+1] == \
                        screenboard[i][j+2] == screenboard[i][j+3]:
                    return True
    #VERTICAL WIN
    for i in range(3):
        for j in range(col):
            if screenboard[i][j] is not None:
                if screenboard[i][j] == screenboard[i+1][j] == \
                        screenboard[i+2][j] == screenboard[i+3][j]:
                    return True
    #DIAGONAL WIN
    for i in range(3):
        for j in range(4):
            if screenboard[i][j] is not None:
                if screenboard[i][j] == screenboard[i+1][j+1] == \
                        screenboard[i+2][j+2] == screenboard[i+3][j+3]:
                    return True
    return False


def winning_move2(row: int, col: int,
             screenboard: List[List] = meta['screenboard']) -> bool:

        #DIAGONAL WIN
        for i in range(4, row):
            for j in range(4):
                if screenboard[i][j] is not None:
                    if screenboard[i][j] == screenboard[i-1][j+1] == \
                            screenboard[i-2][j+2] == screenboard[i-3][j+3] ==\
                            screenboard[i-4][j+4]:
                        return True
        #HORIZONTAL WIN
        for i in range(row):
            for j in range(4):
                if screenboard[i][j] is not None:
                    if screenboard[i][j] == screenboard[i][j+1] == \
                            screenboard[i][j+2] == screenboard[i][j+3] ==\
                            screenboard[i][j+4]:
                        return True
        #VERTICAL WIN
        for i in range(3):
            for j in range(col):
                if screenboard[i][j] is not None:
                    if screenboard[i][j] == screenboard[i+1][j] == \
                            screenboard[i+2][j] == screenboard[i+3][j] ==\
                            screenboard[i-4][j]:
                        return True
        #DIAGONAL WIN
        for i in range(3):
            for j in range(4):
                if screenboard[i][j] is not None:
                    if screenboard[i][j] == screenboard[i+1][j+1] == \
                            screenboard[i+2][j+2] == screenboard[i+3][j+3] ==\
                            screenboard[i+4][j+4]:
                        return True
        return False


def initialize_meta() -> None:
    global meta

    meta = {
        'screenboard': [[]],
        'player_1': {
            'score': 0,
            'moves': 0
        },
        'player_2': {
            'score': 0,
            'moves': 0
        },

        'dims': {
            'row': 0,
            'col': 0
        }
    }


def to_string(mat: List[List]):
    _max = len(mat)
    str_list = [list(map(lambda x: ' ' if x is None else x, y)) for y in mat]
    return '\n'.join('|'.join(f' {x} ' for x in y) +
                     '\n' + (_max - 1) * '---+' for y in str_list)


def save_file(meta: dict, fname: str) -> None:
    with open(f'{fname}', 'w') as filehandle:
        filehandle.write(str(meta))
    print("Succesfully saved game.")


def load_file(fname: str) -> dict:
    f_str = ''
    with open(f'{fname}', 'r') as f:
        f_str = f.read()
    return eval(f_str)

if __name__ == '__main__':
    
    while True:

        print(menu)
        selection = int(input("Enter your choice: "))
        if selection == 1:
            load_or_not = input("Continue your last saved game? (Enter Y to continue)")
            if load_or_not.lower() == 'y':
                #LoadGame()
                load_file('saved_game')
            else:
                create_board(6,7)
                print(to_string(meta['screenboard']))
                start_game(meta)
            system('cls')

        if selection == 2:
            pass

        if selection == 3:
            print(instructions)
        
        if selection == 4:
            print("Thank you for playing!")
            break

        elif selection > 5:
            print("Please enter only numbers from 1-4!")