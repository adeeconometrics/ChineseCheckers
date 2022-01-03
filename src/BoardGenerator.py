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
        return '\n'.join('|'.join(f' {x} ' for x in y) + '\n' + (self.max -1)*'---+' for y in str_lst)
        
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


class BoardGenerator:
    """This object represents the interface visible to the user. 
    This has dependencies to the BoardMatrix objects which serves 
    as the basis for drawing the Chinese Checkers board.
    """    

    p1:int = 0
    p2:int = 0

    def __init__(self, row:int, col:int) -> None: 
        if not (row, col) in ((7,6),(8,7)):
            raise ValueError('Incorrect input')
        
        self.limit = 5 if (row,col) == (8,7) else 4
        self.__board = BoardMatrix(row, col)
        self.row, self.col = row, col
    
    def __str__(self) -> str: 
        return self.__board.__str__()

    def save_game(self, fname:str) -> None:
        dirname = os.path.dirname(__file__)
        fname_path = os.path.join(dirname, f'{fname}.txt')
        with open(fname_path, 'a') as f:
            f.write(str(self))

    def __getitem__(self, index: Tuple[int, int]):
        r, c = index
        if r < self.row or c < self.col:
            return self.__board[r,c]
        raise IndexError('invalid index')

    def __setitem__(self, key: Tuple[int, int], value):
        r, c = key
        self.__board[r,c] = value

    def __update_p1(self) -> None: 
        self.p1 += 1 
    
    def __update_p2(self) -> None: 
        self.p2 += 1
    
    def get_score(self) -> Tuple[int, int]: 
        return self.p1, self.p2


if __name__ == '__main__':
    bg = BoardGenerator(8,7)
    # bg = BoardMatrix(4,5)
    bg[0,0]='x'
    bg[3,4]='o'
    bg[1,2]='x'
    bg[1,3]='o'
    bg[2,2]='x'
    print(bg)
    bg.save_game('game')
