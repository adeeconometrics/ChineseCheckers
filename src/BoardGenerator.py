from __future__ import annotations
from typing import List, Tuple, Union
import os

class BoardMatrix:
    """Representation of the Board Matrix for the Chinese Checkers.

    This object is an iterable which can also be indexed for assigning
    values and getting items. This is a friendly API for representing 
    Matrix as list of list. 
    """    
    mat:List[List[Union[None, str]]]
    row:int
    col:int

    def __init__(self, row:int, col:int) -> None:
        self.col, self.row = col, row
        self.__current = 0
        self.max = row
        self.mat = [[None for _ in range(col)] for _ in range(row)]
    
    def __str__(self) -> str: 
        str_lst = [list(map(lambda x: ' ' if x is None else x, y)) for y in self.mat]
        return '\n'.join('|'.join(f' {x} ' for x in y) + '\n' + (self.max - 1)*'---+' for y in str_lst)
        
    def __repr__(self) -> str:
        return f'{self.mat}'

    def __getitem__(self, index:Tuple[int, int]): 
        r, c = index
        if r < self.row or c < self.col:
            return self.mat[r][c]
        raise IndexError('invalid index')

    def __setitem__(self, key:Tuple[int, int], value):
        r,c = key
        self.mat[r][c] = value

    def __iter__(self) -> BoardMatrix: 
        return self

    def __next__(self): 
        self.__current += 1
        if self.__current < self.max:
            return self.mat[self.__current]
        raise StopIteration

    def __len__(self) -> int:
        return len(self.mat)

    def update_mat(self, mat: List[List[Union[None, str]]]) -> None:
        self.mat = mat

class Player:
    score: int
    moves: int

    def __init__(self, name:str) -> None:
        self.name = name
        self.score = self.moves = 0
    
    def __str__(self) -> str:
        return f"{self.name}'s score : {self.score} \n{self.name}'s moves: {self.moves}"

    def get_score(self) -> int:
        return self.score
    
    def add_score(self) -> None:
        self.score += 1
class BoardGenerator:
    """This object represents the interface visible to the user. 
    This has dependencies to the BoardMatrix objects which serves 
    as the basis for drawing the Chinese Checkers board.
    """    
    def __init__(self, row:int, col:int, 
                p1_name:str = 'Player1', p2_name:str = 'Pleyer2') -> None: 

        if not (row, col) in ((7,6),(8,7)):
            raise ValueError('Incorrect input')

        self.p1 = Player(p1_name)
        self.p2 = Player(p2_name)
        
        self.limit = 5 if (row,col) == (8,7) else 4
        self.__board = BoardMatrix(row, col)
        self.row, self.col = row, col
    
    def __str__(self) -> str: 
        return f'{self.__board.__str__()}\n{self.p1.__str__()}\n\n{self.p2.__str__()}'

    def save_game(self, fname:str) -> None:
        """saves the state of the game with player score and formatted board matrix

        Args:
            fname (str): filename without extension
        """        
        dirname = os.path.dirname(__file__)
        fname_path = os.path.join(dirname, f'{fname}.txt')

        with open(fname_path, 'w') as f:
            f.write(str(self))

    def save_raw(self, fname:str) -> None:
        """saves the state of the game in raw format that is represented with List[List[str | None]]

        Args:
            fname (str): filename without extension
        """        
        dirname = os.path.dirname(__file__)
        fname_path = os.path.join(dirname, f'{fname}.txt')

        with open(fname_path, 'w') as f:
            f.write(repr(self.__board))

    def parse_file(self, fname:str) -> None:
        """reads the raw state of a saved game and performs an update to the board matrix

        Args:
            fname (str): filename without extension
        """        
        dirname = os.path.dirname(__file__)
        fname_path = os.path.join(dirname, f'{fname}.txt')
        f = open(fname_path, 'r')
        f_str = f.read()
        f.close()
        self.__board.update_mat(eval(f_str))

    def __getitem__(self, index: Tuple[int, int]):
        r, c = index
        if r < self.row or c < self.col:
            return self.__board[r,c]
        raise IndexError('invalid index')

    def __setitem__(self, key: Tuple[int, int], value):
        r, c = key
        self.__board[r,c] = value
    
    def get_score(self) -> Tuple[int, int]: 
        """
        Returns:
            Tuple[int, int]: score of player 1 and player 2
        """        
        return self.p1.get_score(), self.p2.get_score()


if __name__ == '__main__':
    bg = BoardGenerator(8,7)
    # bg = BoardMatrix(5,5)
    bg[0,0]='x'
    bg[3,4]='o'
    # bg[1,2]='x'
    # bg[1,3]='o'
    # bg[2,2]='x'
    # # print(bg)
    # # bg.save_raw('gameraw')
    # # bg.parse_file('gameraw')
    print(bg)
    # p1 = A()
    # print(p1)
