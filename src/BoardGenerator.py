from __future__ import annotations
from typing import List, Tuple, Union, Optional

class BoardMatrix:
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
        return ''.join(''.join(f'| {x} |' for x in y) + '\n' for y in str_lst)
        
    def __repr__(self) -> str: 
        str_lst = [list(map(lambda x: ' ' if x is None else x, y)) for y in self.mat]
        return ''.join(''.join(f'| {x} |' for x in y) + '\n' for y in str_lst)

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
    p1:int = 0
    p2:int = 0

    def __init__(self, row:int, col:int) -> None: 
        if not (row, col) in ((7,6),(8,7)):
            raise ValueError('Incorrect input')
        
        self.limit = 5 if row == 8 else 4
        self.row, self.col = row, col
    
    def __str__(self) -> str: 
        ...
    def __repr__(self) -> str: ...

    def save_game(self) -> None: ...
    def update(self, row:int, col:int) -> None: ...
    def get_score(self) -> Tuple[int, int]: ...

if __name__ == '__main__':
    # bg = BoardGenerator(6,8)
    bm = BoardMatrix(4,5)
    bm[1,2] = 'x'
    bm[1,3] = 'o'
    bm[2,2] = 'x'
    print(bm)